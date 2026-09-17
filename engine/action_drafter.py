"""
Action Drafter Module.
Generates tailored, high-context email drafts for Arjun to resolve conflicts,
unblock deliverables, and neutralize corporate risks.
"""
from datetime import datetime
from typing import List, Dict, Any
from .temporal_state import TemporalState

class ActionDrafter:
    def __init__(self, state: TemporalState):
        self.state = state

    def get_recommended_drafts(self) -> List[Dict[str, Any]]:
        drafts = []
        now = self.state.current_time

        # 1. Reschedule Neha's Deck Review (Thursday Clash)
        if now >= datetime(2026, 9, 23, 10, 20):
            drafts.append({
                "id": "draft_reschedule_neha",
                "title": "Resolve Calendar Clash with Neha Kapoor (Thursday Deck Review)",
                "to": "neha.kapoor@veridian-corp.example",
                "subject": "Re: Q3 Campaign Deck Review — Rescheduling from 9:30 AM",
                "urgency": "High",
                "rationale": (
                    "Neha scheduled the review for 9:30 AM Thursday, but Arjun has Board Prep Session "
                    "with Divya scheduled from 9:00 AM to 10:00 AM."
                ),
                "body": (
                    "Hi Neha,\n\n"
                    "Thanks for sharing the update. I have our Board Prep Session scheduled with Divya from 9:00 to 10:00 AM "
                    "on Thursday, so 9:30 AM will clash directly.\n\n"
                    "Could we push our deck review to 10:00–10:30 AM right after Board Prep, or alternatively between "
                    "2:00 PM and 3:30 PM Thursday afternoon?\n\n"
                    "Let me know what works best for you so I can adjust the calendar invite.\n\n"
                    "Best regards,\n"
                    "Arjun Malhotra\n"
                    "VP Sales | Veridian Corp"
                )
            })

        # 2. Overdue Vendor List to Raghav
        if now >= datetime(2026, 9, 22, 9, 0):
            drafts.append({
                "id": "draft_vendor_list_raghav",
                "title": "Deliver / Status Update on Vendor List to Raghav Sethi",
                "to": "raghav.sethi@veridian-corp.example",
                "subject": "Re: Updated Vendor List",
                "urgency": "Critical (Overdue)",
                "rationale": (
                    "Arjun promised the vendor list across Monday and Tuesday; Raghav followed up on Wednesday morning. "
                    "Sending this email closes the open commitment."
                ),
                "body": (
                    "Hi Raghav,\n\n"
                    "Apologies for the delay on this — between the board prep deliverables and client rescheduling, "
                    "it slipped past my original timeline.\n\n"
                    "I am finalizing the updated vendor list now and attaching the latest revision to this note. "
                    "Please review the revised supplier terms and let me know if you need any adjustments before Ops sign-off.\n\n"
                    "Thanks for your patience!\n\n"
                    "Best,\n"
                    "Arjun"
                )
            })

        # 3. Resolve Mumbai Office Lease Renewal Sign-off
        if now >= datetime(2026, 9, 22, 11, 0):
            drafts.append({
                "id": "draft_mumbai_lease_raghav_facilities",
                "title": "Address Mumbai Lease Renewal Ownership & Sign-off",
                "to": "raghav.sethi@veridian-corp.example",
                "cc": "divya.rao@veridian-corp.example, facilities@veridian-corp.example",
                "subject": "Re: Mumbai Office Lease Renewal — Ownership & Execution for Friday Deadline",
                "urgency": "Critical (Deadline Friday 25 Sep)",
                "rationale": (
                    "The Mumbai lease requires an authorized signature by Friday 25 Sep end-of-day. "
                    "It has remained unassigned all week despite two Facilities reminders and two emails from Raghav. "
                    "Arjun and Raghav have a Facilities Check-in on Friday at 10:00 AM."
                ),
                "body": (
                    "Hi Raghav (looping Divya and Facilities),\n\n"
                    "Thanks for flagging this. We cannot let the Mumbai lease renewal lapse past Friday's deadline.\n\n"
                    "I see we have the Facilities Check-in scheduled for Friday from 10:00 to 10:30 AM. "
                    "Let's make signing and submission of the Mumbai renewal the first agenda item for that meeting. "
                    "Facilities team — please bring the final lease document ready for authorized sign-off so we can execute it on the spot.\n\n"
                    "If executive authority from Sales/VP is required today, send the signature portal link directly to me and I will execute it.\n\n"
                    "Best regards,\n"
                    "Arjun Malhotra\n"
                    "VP Sales | Veridian Corp"
                )
            })

        return drafts
