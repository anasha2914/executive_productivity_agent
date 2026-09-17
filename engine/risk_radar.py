"""
Risk Radar Module.
Identifies unowned corporate risks, imminent deadlines, and organizational liabilities.
"""
from datetime import datetime
from typing import List
from .models import RiskItem, Severity
from .temporal_state import TemporalState

class RiskRadar:
    def __init__(self, state: TemporalState):
        self.state = state

    def detect_risks(self) -> List[RiskItem]:
        risks = []
        now = self.state.current_time

        # Check if Mumbai Lease issue is active
        # First announced Monday 21 Sep 10:15 AM
        if now >= datetime(2026, 9, 21, 10, 15):
            # Escalate severity over time
            if now >= datetime(2026, 9, 24, 16, 0): # After Thu second reminder
                sev = Severity.CRITICAL
                status = "CRITICAL / UNOWNED (1 Day to Deadline)"
            elif now >= datetime(2026, 9, 22, 11, 0): # Raghav flagged lack of ownership
                sev = Severity.HIGH
                status = "HIGH RISK / UNASSIGNED"
            else:
                sev = Severity.MEDIUM
                status = "PENDING SIGN-OFF"

            evidence_items = [
                "Email Thread 5 (Mon 10:15 AM): Facilities: 'Reminder: the Mumbai office lease renewal requires an authorized signature by Friday, 25 September.'"
            ]

            if now >= datetime(2026, 9, 21, 18, 40):
                evidence_items.append("Voice Note 1 (Mon 6:40 PM): Arjun: 'haven’t heard back on the Mumbai lease thing, someone needs to own that, I don’t think it’s me.'")

            if now >= datetime(2026, 9, 22, 11, 0):
                evidence_items.append("Email Thread 5 (Tue 11:00 AM): Raghav: 'has anyone confirmed who’s signing off on the Mumbai renewal? Don’t think it’s been assigned.'")

            if now >= datetime(2026, 9, 23, 9, 30):
                evidence_items.append("Email Thread 5 (Wed 9:30 AM): Divya: 'Not on my end — I believe this typically sits with Facilities directly, not us.'")

            if now >= datetime(2026, 9, 24, 16, 0):
                evidence_items.append("Email Thread 5 (Thu 4:00 PM): Facilities 2nd Reminder: 'signature is still pending. Deadline is Friday, 25 September, end of day.'")

            if now >= datetime(2026, 9, 24, 16, 45):
                evidence_items.append("Email Thread 5 (Thu 4:45 PM): Raghav to Arjun: 'This is now one day out and still unowned — can you confirm who’s handling it?'")

            risks.append(RiskItem(
                id="risk_mumbai_lease",
                title="Mumbai Office Lease Renewal: Unassigned Sign-Off at Risk of Lapse",
                severity=sev,
                deadline="Friday, 25 September 2026 (End of Day)",
                owner="UNASSIGNED (Nobody owns it)",
                status=status,
                description=(
                    "The Mumbai office lease renewal requires an authorized executive signature by Friday EOD. "
                    "Neither Ops (Raghav) nor Finance (Divya) claims ownership, assuming Facilities handles it. "
                    "Facilities sent a second company-wide reminder stating signature is still pending. "
                    "If unaddressed, the corporate lease will lapse."
                ),
                source_evidence="; ".join(evidence_items),
                recommended_action=(
                    "Arjun and Raghav have a scheduled 'Facilities Check-in' on Friday 25 Sep from 10:00–10:30 AM. "
                    "Arjun must immediately reply to Raghav's 4:45 PM email confirming they will resolve lease execution "
                    "during the Friday 10:00 AM check-in, or delegate authorized signing power to Raghav/Facilities right now."
                )
            ))

        return risks
