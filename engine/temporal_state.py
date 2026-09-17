"""
Temporal State Manager.
Allows time-travel simulation across the week of Sep 21 - Sep 25, 2026.
The agent strictly reasons using information available up to the given simulated timestamp.
"""
from datetime import datetime
from typing import List, Dict, Any
from data.source_data import (
    PEOPLE,
    LEADERSHIP_SYNC_TRANSCRIPT,
    CALENDARS,
    EMAIL_THREADS,
    VOICE_NOTES
)
from .models import CalendarEvent, EmailItem

# Standard key evaluation milestones during the week
SIMULATION_CHECKPOINTS = {
    "Mon 21 Sep, 09:35 AM (Post-Leadership Sync)": datetime(2026, 9, 21, 9, 35),
    "Mon 21 Sep, 07:00 PM (End of Day 1 / Post Voice Note 1)": datetime(2026, 9, 21, 19, 0),
    "Tue 22 Sep, 10:00 AM (Morning Day 2 / Raghav & Divya emails)": datetime(2026, 9, 22, 10, 0),
    "Tue 22 Sep, 07:00 PM (End of Day 2 / Vendor list pushed again)": datetime(2026, 9, 22, 19, 0),
    "Wed 23 Sep, 08:30 AM (Morning Day 3 / Voice Note 2 & Raghav follow-up)": datetime(2026, 9, 23, 8, 30),
    "Wed 23 Sep, 10:30 AM (Neha proposes Thursday 9:30 AM deck review)": datetime(2026, 9, 23, 10, 30),
    "Wed 23 Sep, 06:30 PM (Divya delivers expense report / Meridian call done)": datetime(2026, 9, 23, 18, 30),
    "Thu 24 Sep, 08:30 AM (Thursday Morning / Before Board Prep & Clash)": datetime(2026, 9, 24, 8, 30),
    "Thu 24 Sep, 05:00 PM (Raghav urgent warning on unowned Mumbai lease)": datetime(2026, 9, 24, 17, 0),
    "Fri 25 Sep, 09:00 AM (Friday Morning / Mumbai Lease Deadline Day)": datetime(2026, 9, 25, 9, 0),
    "Fri 25 Sep, 05:00 PM (End of Week Summary)": datetime(2026, 9, 25, 17, 0),
}

class TemporalState:
    def __init__(self, current_time: datetime):
        self.current_time = current_time

    def is_transcript_available(self) -> bool:
        transcript_dt = datetime.fromisoformat(LEADERSHIP_SYNC_TRANSCRIPT["end_datetime"])
        return self.current_time >= transcript_dt

    def get_transcript(self) -> Dict[str, Any]:
        if self.is_transcript_available():
            return LEADERSHIP_SYNC_TRANSCRIPT
        return {}

    def get_visible_emails(self) -> List[EmailItem]:
        visible = []
        for thread in EMAIL_THREADS:
            for em in thread["emails"]:
                em_time = datetime.fromisoformat(em["timestamp"])
                if em_time <= self.current_time:
                    visible.append(EmailItem(
                        thread_id=thread["id"],
                        email_id=em["id"],
                        timestamp=em_time,
                        sender=em["sender"],
                        sender_name=em["sender_name"],
                        recipients=em["recipients"],
                        subject=thread["subject"],
                        body=em["body"]
                    ))
        return sorted(visible, key=lambda x: x.timestamp)

    def get_visible_voice_notes(self) -> List[Dict[str, Any]]:
        visible = []
        for vn in VOICE_NOTES:
            vn_time = datetime.fromisoformat(vn["timestamp"])
            if vn_time <= self.current_time:
                visible.append(vn)
        return visible

    def get_calendar_events(self, person: str = "arjun") -> List[CalendarEvent]:
        events = []
        raw_events = CALENDARS.get(person, [])
        for ev in raw_events:
            start_dt = datetime.fromisoformat(ev["start"])
            end_dt = datetime.fromisoformat(ev["end"])
            events.append(CalendarEvent(
                person=person,
                day=ev["day"],
                start=start_dt,
                end=end_dt,
                event=ev["event"]
            ))
        return events

    def get_events_for_day(self, person: str, date_str: str) -> List[CalendarEvent]:
        events = self.get_calendar_events(person)
        return [e for e in events if e.day.startswith(date_str)]

    def get_todays_events(self, person: str = "arjun") -> List[CalendarEvent]:
        events = self.get_calendar_events(person)
        return [e for e in events if e.start.date() == self.current_time.date()]
