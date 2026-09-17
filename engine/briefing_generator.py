"""
Briefing Generator Module.
Generates comprehensive Executive Daily Briefings for Arjun Malhotra.
"""
from datetime import datetime
from typing import List
from .models import ExecutiveBriefing, CommitmentStatus
from .temporal_state import TemporalState
from .conflict_detector import ConflictDetector
from .commitment_tracker import CommitmentTracker
from .risk_radar import RiskRadar

class BriefingGenerator:
    def __init__(self, state: TemporalState):
        self.state = state
        self.conflict_detector = ConflictDetector(state)
        self.commitment_tracker = CommitmentTracker(state)
        self.risk_radar = RiskRadar(state)

    def generate_briefing(self) -> ExecutiveBriefing:
        now = self.state.current_time
        day_str = now.strftime("%A, %d %B %Y (%I:%M %p)")
        day_name = now.strftime("%A")

        todays_events = self.state.get_todays_events("arjun")
        conflicts = self.conflict_detector.detect_conflicts()
        outbound = self.commitment_tracker.get_outbound()
        inbound = self.commitment_tracker.get_inbound()
        risks = self.risk_radar.detect_risks()

        # Build dynamic executive priorities
        priorities = []
        suggestions = []

        # Check vendor list status
        vendor_comm = next((c for c in outbound if c.id == "comm_vendor_list"), None)
        if vendor_comm:
            if vendor_comm.status == CommitmentStatus.OVERDUE:
                priorities.append("🔴 URGENT: Send Updated Vendor List to Raghav (Delayed 3 times; currently overdue).")
                suggestions.append("Send Raghav the vendor list immediately or notify him of the revised realistic dispatch time.")
            else:
                priorities.append("🟡 Fulfill commitment: Deliver updated vendor list to Raghav Sethi.")

        # Check schedule conflicts
        for conf in conflicts:
            priorities.append(f"🚨 CALENDAR CLASH: {conf.title}")
            suggestions.append(conf.suggested_action)

        # Check risks
        for r in risks:
            if "CRITICAL" in r.status or "HIGH" in r.status:
                priorities.append(f"⚠️ CORPORATE RISK: {r.title} (Deadline: {r.deadline})")
                suggestions.append(r.recommended_action)

        # Day-specific highlights
        if day_name == "Monday":
            priorities.append("Align with Neha on Q3 campaign deck and 1:1 sync at 2:00 PM.")
            priorities.append("Reconfirm new meeting time with Priya Nair (Meridian Logistics).")
        elif day_name == "Tuesday":
            priorities.append("Internal Budget Review at 11:00 AM.")
            priorities.append("Ensure July expense variance report timeline is locked with Divya for Wednesday evening.")
        elif day_name == "Wednesday":
            priorities.append("Client Call with Priya Nair (Meridian Logistics) at 3:00 PM.")
            priorities.append("Receive and review July Expense Variance Report from Divya at 6:00 PM ahead of tomorrow's Board Prep.")
        elif day_name == "Thursday":
            priorities.append("Board Prep Session from 9:00 AM–10:00 AM with Divya.")
            priorities.append("Sales Associate Hiring Panel at 4:00 PM.")
        elif day_name == "Friday":
            priorities.append("Facilities Check-in at 10:00 AM — Critical agenda: Execute Mumbai Office Lease Renewal.")

        greeting = f"Good morning, Arjun. Here is your Executive Intelligence Briefing for {day_name}."

        return ExecutiveBriefing(
            simulated_time=now,
            day_name=day_name,
            greeting=greeting,
            top_priorities=priorities,
            todays_schedule=todays_events,
            conflicts_detected=conflicts,
            outbound_commitments_due=outbound,
            inbound_deliverables_expected=inbound,
            active_risks=risks,
            proactive_suggestions=suggestions
        )
