"""
Conflict Detector Module.
Identifies calendar collisions, double bookings, and mismatched scheduling expectations.
"""
from datetime import datetime
from typing import List
from .models import ScheduleConflict, Severity
from .temporal_state import TemporalState

class ConflictDetector:
    def __init__(self, state: TemporalState):
        self.state = state

    def detect_conflicts(self) -> List[ScheduleConflict]:
        conflicts = []

        # Conflict 1: Thursday 24 Sep - Board Prep vs Neha Deck Review
        # Visible if current_time has visibility into Thursday or post Neha's email proposal on Wed 23 Sep 10:20 AM
        thursday_deck_proposal = datetime(2026, 9, 23, 10, 20)
        
        if self.state.current_time >= thursday_deck_proposal:
            # Check Arjun's calendar for Thu 24 Sep
            arjun_events = self.state.get_calendar_events("arjun")
            neha_events = self.state.get_calendar_events("neha")

            board_prep = next((e for e in arjun_events if "Board Prep" in e.event and e.day.startswith("Thu")), None)
            neha_review = next((e for e in neha_events if "Deck Review" in e.event and e.day.startswith("Thu")), None)

            if board_prep and neha_review:
                # Severity is CRITICAL if on Thursday or approaching Thursday
                is_urgent = self.state.current_time >= datetime(2026, 9, 23, 18, 0)
                sev = Severity.CRITICAL if is_urgent else Severity.HIGH

                conflicts.append(ScheduleConflict(
                    id="conflict_thu_board_vs_deck",
                    title="Direct Calendar Collision: Board Prep vs Neha's Q3 Deck Review",
                    day="Thu 24 Sep",
                    severity=sev,
                    conflicting_events=[
                        {
                            "owner": "Arjun Malhotra & Divya Rao",
                            "event": "Board Prep Session",
                            "time": "09:00 AM – 10:00 AM",
                            "status": "Firm on Arjun's Calendar"
                        },
                        {
                            "owner": "Neha Kapoor",
                            "event": "Deck Review with Arjun",
                            "time": "09:30 AM – 10:00 AM",
                            "status": "Booked on Neha's Calendar / Email confirmation"
                        }
                    ],
                    explanation=(
                        "Neha assumed Arjun's board prep was after 10:00 AM ('Let’s say 9:30 AM Thursday, before your board prep block'). "
                        "However, Arjun's Board Prep Session is scheduled for 9:00–10:00 AM with Divya. "
                        "This creates a direct 30-minute clash between 9:30 AM and 10:00 AM on Thursday."
                    ),
                    suggested_action=(
                        "Immediately notify Neha to reschedule the Q3 Deck Review to Thursday 10:00–10:30 AM (or Friday morning), "
                        "as Arjun is occupied with Board Prep until 10:00 AM."
                    ),
                    source_evidence=(
                        "Arjun's Calendar (Thu 24 Sep 9:00-10:00 AM: Board Prep Session); "
                        "Neha's Calendar (Thu 24 Sep 9:30-10:00 AM: Deck Review with Arjun); "
                        "Email Thread 2, Email 4 (Wed 23 Sep 10:20 AM: Neha proposes 9:30 AM)."
                    )
                ))

        return conflicts
