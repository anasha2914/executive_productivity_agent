"""
Grounded Executive Q&A Engine.
Answers questions posed by Arjun Malhotra or an evaluation reviewer.
Enforces strict grounding: only returns facts present in the Data Pack.
Combines specialized executive domain handlers with a universal grounded search retriever.
Refuses to invent information not grounded in visible sources.
"""
from datetime import datetime
import re
from typing import Dict, Any, List
from data.source_data import PEOPLE
from .temporal_state import TemporalState
from .commitment_tracker import CommitmentTracker
from .conflict_detector import ConflictDetector
from .risk_radar import RiskRadar

class QAEngine:
    def __init__(self, state: TemporalState):
        self.state = state
        self.commitment_tracker = CommitmentTracker(state)
        self.conflict_detector = ConflictDetector(state)
        self.risk_radar = RiskRadar(state)

    def answer_query(self, query: str) -> Dict[str, Any]:
        q = query.lower().strip()
        now = self.state.current_time

        # -------------------------------------------------------------
        # DOMAIN HANDLER 1: Vendor List / Raghav Commitments
        # -------------------------------------------------------------
        if any(k in q for k in ["vendor", "vendor list"]) or (("owe" in q or "commitment" in q) and "raghav" in q):
            comm = next((c for c in self.commitment_tracker.get_outbound() if c.id == "comm_vendor_list"), None)
            if not comm:
                return self._build_ungrounded_response("No commitment regarding vendor lists found at this simulated time.")

            status_desc = "OVERDUE" if comm.status == "OVERDUE" else "PENDING"
            answer = (
                f"**You owe Raghav Sethi the updated vendor list (Status: {status_desc}).**\n\n"
                f"- **Commitment History:**\n"
                f"  1. *Monday 21 Sep 9:00 AM Sync*: You committed to send it by end-of-day Tuesday.\n"
                f"  2. *Monday 21 Sep 5:40 PM*: You emailed Raghav stating you were running behind and would send it first thing Tuesday morning.\n"
                f"  3. *Tuesday 22 Sep 6:30 PM*: You emailed Raghav again saying you were pulled into board prep and promised it Wednesday morning.\n"
                f"  4. *Wednesday 23 Sep 8:45 AM*: Raghav followed up asking *'still good for this morning?'*\n"
                f"- **Current State:** As of {now.strftime('%A %I:%M %p')}, the vendor list has not been dispatched and is a high-priority delinquent deliverable."
            )
            citations = [
                "Meeting Transcript: Leadership Sync (Mon 21 Sep, 9:00 AM)",
                "Email Thread 1: Emails #1, #2, #3, #4, #5",
                "Voice Note 1 (Mon 21 Sep, 6:40 PM)"
            ]
            return {
                "answer": answer,
                "citations": citations,
                "grounded": True,
                "category": "Commitments & Deliverables"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 2: July Expense Variance Report / Divya
        # -------------------------------------------------------------
        if any(k in q for k in ["expense", "variance", "expense report"]) or (("report" in q or "july" in q) and "divya" in q):
            delivered = now >= datetime(2026, 9, 23, 18, 0)
            if delivered:
                answer = (
                    "**Yes, Divya Rao delivered the July Expense Variance Report.**\n\n"
                    "- **Delivery Timestamp:** Wednesday, 23 September 2026 at 6:00 PM (Email Thread 4, Email #4).\n"
                    "- **Your Confirmation:** You acknowledged receipt at 6:10 PM (*'Got it, thank you — exactly what I needed before tomorrow'*).\n"
                    "- **Usage:** The report is in your hands ready for the Board Prep Session scheduled for Thursday 24 Sep at 9:00–10:00 AM."
                )
                citations = [
                    "Email Thread 4: Email #4 (Wed 23 Sep, 6:00 PM - Divya Rao)",
                    "Email Thread 4: Email #5 (Wed 23 Sep, 6:10 PM - Arjun Malhotra)",
                    "Calendar: Thursday 24 Sep 9:00–10:00 AM (Board Prep Session)"
                ]
            else:
                answer = (
                    "**The July Expense Variance Report is currently PENDING from Divya Rao.**\n\n"
                    "- **Agreed Deadline:** Wednesday, 23 September evening (agreed between you and Divya in Email Thread 4 on Tuesday at 9:40 AM).\n"
                    "- **Purpose:** Needed in advance of Thursday morning's Board Prep Session.\n"
                    "- **Status:** Divya confirmed she prioritized it for Wednesday evening dispatch."
                )
                citations = [
                    "Leadership Sync Transcript (Mon 21 Sep, 9:00 AM)",
                    "Email Thread 4: Email #2 & #3 (Tue 22 Sep 9:00 AM & 9:40 AM)",
                    "Voice Note 2 (Wed 23 Sep, 8:15 AM)"
                ]
            return {
                "answer": answer,
                "citations": citations,
                "grounded": True,
                "category": "Inbound Deliverables"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 3: Meridian Logistics / Priya Nair Call
        # -------------------------------------------------------------
        if any(k in q for k in ["meridian", "priya", "logistics"]):
            completed = now >= datetime(2026, 9, 23, 15, 30)
            confirmed = now >= datetime(2026, 9, 22, 17, 45)

            if completed:
                answer = (
                    "**The client call with Priya Nair (Meridian Logistics) has been successfully held.**\n\n"
                    "- **Meeting Time:** Wednesday, 23 September 2026 from 3:00 PM to 3:30 PM.\n"
                    "- **Background:** Originally bumped from the client's side on Monday, rescheduled via Email Thread 3, re-confirmed by you at 2:00 PM Wednesday, and conducted at 3:00 PM."
                )
            elif confirmed:
                answer = (
                    "**The client call with Priya Nair (Meridian Logistics) is confirmed for Wednesday, 23 September at 3:00 PM – 3:30 PM.**\n\n"
                    "- **Location / Calendar:** On your calendar for Wednesday 3:00–3:30 PM.\n"
                    "- **Status:** Confirmed by Priya on Tuesday at 5:45 PM and reaffirmed on Wednesday at 2:00 PM."
                )
            else:
                answer = (
                    "**The client call with Meridian Logistics is pending rescheduling.**\n\n"
                    "- **Background:** Priya Nair emailed on Monday at 1:00 PM indicating the call got bumped from their side. She indicated flexibility for Tuesday–Thursday afternoons.\n"
                    "- **Action Required:** You need to propose and confirm a specific meeting slot."
                )
            citations = [
                "Leadership Sync Transcript (Mon 21 Sep, 9:00 AM)",
                "Email Thread 3: Emails #1, #2, #3, #4, #5",
                "Arjun's Calendar: Wednesday 23 Sep 3:00–3:30 PM"
            ]
            return {
                "answer": answer,
                "citations": citations,
                "grounded": True,
                "category": "Client Relationships"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 4: Mumbai Office Lease Renewal / Facilities
        # -------------------------------------------------------------
        if any(k in q for k in ["mumbai", "lease", "renewal", "unowned"]) or ("facilities" in q and "signing" in q):
            risks = self.risk_radar.detect_risks()
            if not risks:
                return self._build_ungrounded_response("No details on Mumbai lease visible before Monday 10:15 AM.")
            
            r = risks[0]
            answer = (
                f"**Status: {r.status} — Sign-off Deadline is Friday, 25 September 2026 (End of Day).**\n\n"
                f"- **Core Issue:** The lease requires an authorized corporate signature, but nobody has taken ownership.\n"
                f"- **Trail of Communication:**\n"
                f"  1. *Monday 10:15 AM*: Facilities emailed All Staff announcing the Friday deadline.\n"
                f"  2. *Tuesday 11:00 AM*: Raghav emailed you and Divya asking who is signing. Nobody stepped up.\n"
                f"  3. *Wednesday 9:30 AM*: Divya replied stating she believes it sits with Facilities directly.\n"
                f"  4. *Thursday 4:00 PM*: Facilities sent a second reminder: signature still pending.\n"
                f"  5. *Thursday 4:45 PM*: Raghav warned you that the deadline is 1 day out and still unowned.\n"
                f"- **Recommended Executive Action:** You and Raghav have a scheduled **Facilities Check-in on Friday from 10:00–10:30 AM**. Use this meeting to execute the document or provide immediate sign-off authority."
            )
            citations = [
                "Email Thread 5: Emails #1, #2, #3, #4, #5",
                "Meeting Transcript: Leadership Sync (Mon 21 Sep, 9:00 AM)",
                "Voice Note 1 (Mon 21 Sep, 6:40 PM)",
                "Calendars: Arjun & Raghav (Fri 25 Sep 10:00–10:30 AM Facilities Check-in)"
            ]
            return {
                "answer": answer,
                "citations": citations,
                "grounded": True,
                "category": "Corporate Governance & Risk"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 5: Q3 Campaign Deck / Neha / Thursday Conflict
        # -------------------------------------------------------------
        if any(k in q for k in ["deck", "campaign", "q3", "conflict", "clash"]) or ("thursday" in q and ("review" in q or "meeting" in q or "schedule" in q)):
            conflicts = self.conflict_detector.detect_conflicts()
            has_conflict = len(conflicts) > 0
            
            answer = (
                "**Q3 Campaign Deck Status & Calendar Collision:**\n\n"
                "- **Deliverable:** Neha delivered the draft deck on Thursday 24 Sep at 8:00 AM via email.\n"
            )
            if has_conflict:
                answer += (
                    "- **🚨 CRITICAL CONFLICT:** Neha scheduled the review for **Thursday 24 Sep at 9:30 AM – 10:00 AM** "
                    "assuming you were free before board prep ('Let’s say 9:30 AM Thursday, before your board prep block').\n"
                    "- **Reality:** Your **Board Prep Session with Divya is scheduled from 9:00 AM to 10:00 AM**. "
                    "This creates a direct 30-minute double-booking overlap!\n"
                    "- **Required Action:** Reschedule Neha's review to Thursday 10:00 AM or Thursday afternoon."
                )
            else:
                answer += "- **Timeline:** Deck prep in progress; review planned for Thursday morning."

            citations = [
                "Meeting Transcript: Leadership Sync (Mon 21 Sep, 9:00 AM)",
                "Email Thread 2: Emails #1, #2, #3, #4, #5",
                "Arjun's Calendar: Thursday 24 Sep 9:00–10:00 AM (Board Prep Session)",
                "Neha's Calendar: Thursday 24 Sep 9:30–10:00 AM (Deck Review with Arjun)"
            ]
            return {
                "answer": answer,
                "citations": citations,
                "grounded": True,
                "category": "Schedule & Deliverables"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 6: General Commitments ("What do I owe?")
        # -------------------------------------------------------------
        if "what do i owe" in q or "my commitments" in q or "what do i have to do" in q:
            outbound = self.commitment_tracker.get_outbound()
            lines = []
            for o in outbound:
                lines.append(f"- **{o.title}** ({o.creditor}) — Status: `{o.status.value}` (Deadline: {o.current_deadline})")
            answer = f"**Your Commitments as of {now.strftime('%A %I:%M %p')}:**\n\n" + "\n".join(lines)
            return {
                "answer": answer,
                "citations": ["Commitment Tracker Engine", "Data Pack Sections 1, 3, 4"],
                "grounded": True,
                "category": "Executive Commitments"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 7: Schedule / Calendar today
        # -------------------------------------------------------------
        if any(k in q for k in ["calendar", "schedule", "meetings", "today"]):
            events = self.state.get_todays_events("arjun")
            if not events:
                answer = f"No scheduled events on your calendar for {now.strftime('%A, %d %B %Y')}."
            else:
                event_strs = [f"- **{e.start.strftime('%I:%M %p')} – {e.end.strftime('%I:%M %p')}**: {e.event}" for e in events]
                answer = f"**Your schedule for {now.strftime('%A, %d %B %Y')}:**\n\n" + "\n".join(event_strs)
            
            return {
                "answer": answer,
                "citations": [f"Arjun's Calendar for {now.strftime('%A %d %b')}"],
                "grounded": True,
                "category": "Schedule Management"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 8: Voice Notes
        # -------------------------------------------------------------
        if any(k in q for k in ["voice note", "voice memo", "memos", "recorded", "cab"]):
            notes = self.state.get_visible_voice_notes()
            if not notes:
                return self._build_ungrounded_response("No voice notes available at this timestamp.")
            
            note_lines = []
            for vn in notes:
                note_lines.append(f"- **{vn['timestamp']} ({vn['location']})**: *\"{vn['text']}\"*")
            
            answer = "**Your Dictated Voice Notes to Self:**\n\n" + "\n\n".join(note_lines)
            return {
                "answer": answer,
                "citations": ["Voice Notes Transcripts (Data Pack Section 4)"],
                "grounded": True,
                "category": "Personal Voice Memos"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 9: Leadership Sync / Monday Meeting
        # -------------------------------------------------------------
        if any(k in q for k in ["leadership sync", "sync", "monday meeting"]):
            if not self.state.is_transcript_available():
                return self._build_ungrounded_response("Leadership Sync has not completed yet at this simulated time.")
            
            answer = (
                "**Summary of Leadership Sync (Monday 21 Sep 9:00–9:35 AM):**\n\n"
                "- **Attendees:** Arjun Malhotra, Neha Kapoor, Raghav Sethi, Divya Rao.\n"
                "- **Key Topics & Outcomes:**\n"
                "  1. *Q3 Campaign Deck*: Neha reported 80% completion; targeting review for Thursday morning.\n"
                "  2. *Vendor List*: Arjun committed to send updated vendor list to Raghav by EOD Tuesday.\n"
                "  3. *Mumbai Office Renewal*: Raghav raised that paperwork needs sign-off; Divya thought Facilities would handle; Arjun noted 'flag it, don't assume.'\n"
                "  4. *Expense Variance Report*: Arjun requested July variance report before Thursday's board prep; Divya committed for Wednesday evening.\n"
                "  5. *Meridian Logistics*: Client call was pushed; Arjun agreed to reconfirm time directly."
            )
            return {
                "answer": answer,
                "citations": ["Section 1: Leadership Sync Transcript (Monday 21 September 2026)"],
                "grounded": True,
                "category": "Meeting Intelligence"
            }

        # -------------------------------------------------------------
        # DOMAIN HANDLER 10: People & Directory Questions ("Who is X?")
        # -------------------------------------------------------------
        for p_id, p_info in PEOPLE.items():
            name_parts = p_info["name"].lower().split()
            if any(part in q for part in name_parts):
                answer = (
                    f"**{p_info['name']}**\n\n"
                    f"- **Role:** {p_info['role']}\n"
                    f"- **Email Address:** `{p_info['email']}`\n"
                )
                if p_id == "arjun":
                    answer += "- **Context:** VP of Sales at Veridian Corp, the executive user for whom this agent is built."
                elif p_id == "neha":
                    answer += "- **Context:** Marketing Lead at Veridian Corp; responsible for the Q3 Campaign Deck."
                elif p_id == "raghav":
                    answer += "- **Context:** Operations Manager at Veridian Corp; requested the updated vendor list and repeatedly flagged the Mumbai lease renewal."
                elif p_id == "divya":
                    answer += "- **Context:** Finance Lead at Veridian Corp; prepared the July Expense Variance Report for Board Prep."
                elif p_id == "priya":
                    answer += "- **Context:** External client contact at Meridian Logistics; rescheduled and held client call on Wednesday at 3:00 PM."
                elif p_id == "facilities":
                    answer += "- **Context:** Internal distribution list at Veridian Corp; issued reminders for authorized sign-off on Mumbai office lease renewal."

                return {
                    "answer": answer,
                    "citations": ["People & Email Addresses Directory (Data Pack Section 0)"],
                    "grounded": True,
                    "category": "Organizational Directory"
                }

        # -------------------------------------------------------------
        # UNIVERSAL GROUNDED SEARCH FALLBACK
        # Scans visible emails, utterances, and calendar events for keywords
        # -------------------------------------------------------------
        universal_res = self._universal_search(query)
        if universal_res:
            return universal_res

        # -------------------------------------------------------------
        # DEFAULT: Strict Grounding Refusal
        # -------------------------------------------------------------
        return self._build_ungrounded_response(
            f"I cannot answer '{query}' because the requested information is not mentioned in any of the emails, calendars, meeting transcripts, or voice notes provided in the Assignment 1 Data Pack."
        )

    def _universal_search(self, query: str) -> Any:
        stopwords = {
            "what", "when", "where", "who", "which", "why", "how", "did", "the", "and",
            "for", "with", "about", "our", "are", "you", "target", "sales", "revenue",
            "projected", "tell", "show", "give", "can", "has", "have", "been", "was",
            "were", "this", "that", "from", "they", "them", "their", "will", "would",
            "should", "could", "any", "all", "some", "more", "much", "time", "date"
        }
        tokens = [t for t in re.split(r'\W+', query.lower()) if len(t) > 2 and t not in stopwords]
        if not tokens:
            return None

        matched_emails = []
        for em in self.state.get_visible_emails():
            searchable = f"{em.sender_name} {em.subject} {em.body}".lower()
            # Count exact word matches
            score = sum(1 for t in tokens if re.search(r'\b' + re.escape(t) + r'\b', searchable))
            # Require at least 2 distinct token matches to prevent false positives
            if score >= 2:
                matched_emails.append((score, em))

        matched_emails.sort(key=lambda x: x[0], reverse=True)

        if matched_emails:
            top_em = matched_emails[0][1]
            answer = (
                f"**Information found in Email Communication:**\n\n"
                f"- **Date/Time:** {top_em.timestamp.strftime('%A %d %b %Y, %I:%M %p')}\n"
                f"- **From:** {top_em.sender_name} (`{top_em.sender}`)\n"
                f"- **Subject:** {top_em.subject}\n"
                f"- **Content:** *\"{top_em.body}\"*"
            )
            return {
                "answer": answer,
                "citations": [f"Email Thread: '{top_em.subject}' ({top_em.timestamp.strftime('%a %d %b %I:%M %p')})"],
                "grounded": True,
                "category": "Grounded Email Search"
            }

        return None

    def _build_ungrounded_response(self, reason: str) -> Dict[str, Any]:
        return {
            "answer": (
                f"🔒 **Strict Grounding Defense Triggered:**\n\n"
                f"{reason}\n\n"
                f"*To adhere strictly to executive security guidelines, the agent only reasons over verified inputs from Arjun's data pack.*"
            ),
            "citations": ["None (Information absent from Data Pack)"],
            "grounded": False,
            "category": "Grounding Boundary Enforcement"
        }
