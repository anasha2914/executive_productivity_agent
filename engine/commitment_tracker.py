"""
Commitment Tracker Module.
Tracks outbound commitments (what Arjun owes) and inbound deliverables (what others owe Arjun).
Calculates real-time status (PENDING, OVERDUE, FULFILLED) based on current simulated time.
"""
from datetime import datetime
from typing import List, Dict, Any
from .models import Commitment, CommitmentStatus, CommitmentDirection
from .temporal_state import TemporalState

class CommitmentTracker:
    def __init__(self, state: TemporalState):
        self.state = state

    def get_commitments(self) -> List[Commitment]:
        commitments = []
        now = self.state.current_time

        # -------------------------------------------------------------
        # 1. OUTBOUND: Vendor List to Raghav Sethi
        # -------------------------------------------------------------
        # Arjun repeatedly promised:
        # - Mon 9:00 AM sync: "end of day tomorrow" (Tue 22 Sep EOD)
        # - Mon 5:40 PM: "first thing tomorrow morning" (Tue 22 Sep ~9:00 AM)
        # - Tue 6:30 PM: "tomorrow (Wednesday) morning for sure" (Wed 23 Sep ~9:00 AM)
        # - Wed 8:45 AM: Raghav asks "still good for this morning?"
        # - Never sent in any subsequent email or event.
        if self.state.is_transcript_available():
            vendor_status = CommitmentStatus.PENDING
            current_deadline = "Tue 22 Sep, End of Day"
            evidence = [
                "Leadership Sync (Mon 9:00 AM): Arjun: 'I told Raghav I’d send him the updated vendor list. I’ll get that to him by end of day tomorrow.'"
            ]

            if now >= datetime(2026, 9, 21, 17, 40):
                evidence.append("Email Thread 1 (Mon 5:40 PM): Arjun: 'Running behind, will send first thing tomorrow morning instead.'")
                current_deadline = "Tue 22 Sep, 9:00 AM"

            if now >= datetime(2026, 9, 21, 18, 40):
                evidence.append("Voice Note 1 (Mon 6:40 PM): Arjun: 'need to get Raghav that vendor list... might slip to tomorrow morning, remind me.'")

            if now >= datetime(2026, 9, 22, 18, 30):
                evidence.append("Email Thread 1 (Tue 6:30 PM): Arjun: 'will send by tomorrow (Wednesday) morning for sure.'")
                current_deadline = "Wed 23 Sep, Morning (9:00 AM)"

            if now >= datetime(2026, 9, 23, 8, 45):
                evidence.append("Email Thread 1 (Wed 8:45 AM): Raghav: 'Just checking — still good for this morning?'")

            # Determine overdue status:
            if now > datetime(2026, 9, 23, 12, 0):
                vendor_status = CommitmentStatus.OVERDUE
            elif now > datetime(2026, 9, 22, 12, 0) and now < datetime(2026, 9, 22, 18, 30):
                vendor_status = CommitmentStatus.OVERDUE
            else:
                vendor_status = CommitmentStatus.PENDING

            commitments.append(Commitment(
                id="comm_vendor_list",
                title="Send Updated Vendor List to Raghav Sethi",
                direction=CommitmentDirection.OUTBOUND,
                debtor="Arjun Malhotra",
                creditor="Raghav Sethi (Ops Manager)",
                initial_deadline="Tue 22 Sep, End of Day",
                current_deadline=current_deadline,
                status=vendor_status,
                evidence=evidence,
                notes=(
                    "CRITICAL DELINQUENCY: Slipped 3 times (Mon EOD -> Tue morning -> Wed morning). "
                    "Raghav followed up on Wed 8:45 AM. Arjun has not sent the file yet."
                ),
                action_needed=True
            ))

        # -------------------------------------------------------------
        # 2. INBOUND: July Expense Variance Report from Divya Rao
        # -------------------------------------------------------------
        if self.state.is_transcript_available():
            report_status = CommitmentStatus.PENDING
            evidence = [
                "Leadership Sync (Mon 9:00 AM): Arjun asks Divya to pull report before Thursday's board prep. Divya: 'I'll have it ready Wednesday evening.'"
            ]

            if now >= datetime(2026, 9, 21, 14, 30):
                evidence.append("Email Thread 4 (Mon 2:30 PM): Divya targets Thursday morning.")

            if now >= datetime(2026, 9, 22, 9, 0):
                evidence.append("Email Thread 4 (Tue 9:00 AM): Arjun asks for Wednesday evening instead.")

            if now >= datetime(2026, 9, 22, 9, 40):
                evidence.append("Email Thread 4 (Tue 9:40 AM): Divya confirms Wednesday evening.")

            if now >= datetime(2026, 9, 23, 8, 15):
                evidence.append("Voice Note 2 (Wed 8:15 AM): Arjun reminds self expense report must be in hands Wednesday evening.")

            if now >= datetime(2026, 9, 23, 18, 0):
                evidence.append("Email Thread 4 (Wed 6:00 PM): Divya sends attached report.")
                evidence.append("Email Thread 4 (Wed 6:10 PM): Arjun confirms receipt: 'Got it, thank you — exactly what I needed before tomorrow.'")
                report_status = CommitmentStatus.FULFILLED

            commitments.append(Commitment(
                id="comm_expense_report",
                title="Receive July Expense Variance Report from Divya Rao",
                direction=CommitmentDirection.INBOUND,
                debtor="Divya Rao (Finance)",
                creditor="Arjun Malhotra",
                initial_deadline="Wed 23 Sep, Evening",
                current_deadline="Wed 23 Sep, 6:00 PM",
                status=report_status,
                evidence=evidence,
                notes="Delivered as promised on Wed 23 Sep at 6:00 PM. Ready for Board Prep on Thursday 9:00 AM." if report_status == CommitmentStatus.FULFILLED else "Required before Thursday 9:00 AM Board Prep Session.",
                action_needed=(report_status != CommitmentStatus.FULFILLED)
            ))

        # -------------------------------------------------------------
        # 3. INBOUND: Q3 Campaign Deck Draft from Neha Kapoor
        # -------------------------------------------------------------
        if self.state.is_transcript_available():
            deck_status = CommitmentStatus.PENDING
            evidence = [
                "Leadership Sync (Mon 9:00 AM): Neha: 'Draft is 80% done. I'll send it to Arjun for review by Wednesday... realistically Thursday morning is safer.'"
            ]

            if now >= datetime(2026, 9, 22, 16, 15):
                evidence.append("Email Thread 2 (Tue 4:15 PM): Neha shifts review to Thursday morning.")

            if now >= datetime(2026, 9, 24, 8, 0):
                evidence.append("Email Thread 2 (Thu 8:00 AM): Neha sends draft deck: 'Deck is ready, attaching the draft ahead of our 9:30 review.'")
                deck_status = CommitmentStatus.FULFILLED

            commitments.append(Commitment(
                id="comm_campaign_deck",
                title="Receive Q3 Campaign Deck Draft from Neha Kapoor",
                direction=CommitmentDirection.INBOUND,
                debtor="Neha Kapoor (Marketing Lead)",
                creditor="Arjun Malhotra",
                initial_deadline="Wed 23 Sep",
                current_deadline="Thu 24 Sep, 8:00 AM",
                status=deck_status,
                evidence=evidence,
                notes="Draft delivered Thursday 8:00 AM; however, the scheduled 9:30 AM review clashes with Arjun's Board Prep Session!" if deck_status == CommitmentStatus.FULFILLED else "Expected Thursday morning ahead of board reviews.",
                action_needed=(deck_status != CommitmentStatus.FULFILLED)
            ))

        # -------------------------------------------------------------
        # 4. OUTBOUND: Reschedule Client Call with Priya Nair (Meridian)
        # -------------------------------------------------------------
        if self.state.is_transcript_available():
            call_status = CommitmentStatus.PENDING
            evidence = [
                "Leadership Sync (Mon 9:00 AM): Arjun notes Meridian client call got pushed, must reconfirm new time."
            ]

            if now >= datetime(2026, 9, 21, 13, 0):
                evidence.append("Email Thread 3 (Mon 1:00 PM): Priya asks Arjun to propose new time (flexible Tue-Thu afternoons).")

            if now >= datetime(2026, 9, 22, 15, 0):
                evidence.append("Email Thread 3 (Tue 3:00 PM): Arjun proposes Wednesday 3:00 PM.")

            if now >= datetime(2026, 9, 22, 17, 45):
                evidence.append("Email Thread 3 (Tue 5:45 PM): Priya confirms Wednesday 3:00 PM.")

            if now >= datetime(2026, 9, 23, 14, 0):
                evidence.append("Email Thread 3 (Wed 2:00 PM): Arjun re-confirms 3 PM meeting.")

            if now >= datetime(2026, 9, 23, 15, 30):
                evidence.append("Calendar Event (Wed 3:00–3:30 PM): Call completed.")
                call_status = CommitmentStatus.FULFILLED

            commitments.append(Commitment(
                id="comm_meridian_call",
                title="Lock in & Attend Meridian Logistics Client Call (Priya Nair)",
                direction=CommitmentDirection.OUTBOUND,
                debtor="Arjun Malhotra",
                creditor="Priya Nair (Meridian Logistics)",
                initial_deadline="Tue-Thu afternoons",
                current_deadline="Wed 23 Sep, 3:00 PM",
                status=call_status,
                evidence=evidence,
                notes="Call successfully re-scheduled for Wednesday 3:00 PM and held." if call_status == CommitmentStatus.FULFILLED else "Awaiting confirmation with client.",
                action_needed=(call_status != CommitmentStatus.FULFILLED)
            ))

        return commitments

    def get_outbound(self) -> List[Commitment]:
        return [c for c in self.get_commitments() if c.direction == CommitmentDirection.OUTBOUND]

    def get_inbound(self) -> List[Commitment]:
        return [c for c in self.get_commitments() if c.direction == CommitmentDirection.INBOUND]
