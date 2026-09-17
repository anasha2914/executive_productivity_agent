"""
Executive Productivity Agent — Zero-Dependency CLI Demo
Allows running and reviewing the agent in any standard Python environment without Streamlit.
"""

import sys
import os
from datetime import datetime

# Configure UTF-8 encoding for Windows standard output
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from data.source_data import PEOPLE
from engine.temporal_state import TemporalState, SIMULATION_CHECKPOINTS
from engine.briefing_generator import BriefingGenerator
from engine.conflict_detector import ConflictDetector
from engine.commitment_tracker import CommitmentTracker
from engine.risk_radar import RiskRadar
from engine.action_drafter import ActionDrafter
from engine.qa_engine import QAEngine

def print_separator(title=""):
    if title:
        print(f"\n{'='*25} {title.upper()} {'='*25}")
    else:
        print(f"{'='*60}")

def clean_str(text: str) -> str:
    """Safely format string for any console encoding."""
    return text.encode(sys.stdout.encoding or 'utf-8', errors='replace').decode(sys.stdout.encoding or 'utf-8')

def main():
    print_separator("EXECUTIVE PRODUCTIVITY AGENT (ARJUN MALHOTRA)")
    print("Assessment Benchmark: Week of 21-25 September 2026")
    print("User: Arjun Malhotra (VP Sales, Veridian Corp)")

    # Default checkpoint: Thursday 08:30 AM (Acute conflict & overdue commitments)
    sim_time = datetime(2026, 9, 24, 8, 30)
    print(f"\nActive Simulated Time: {sim_time.strftime('%A, %d %B %Y at %I:%M %p')}")

    state = TemporalState(sim_time)
    briefing_gen = BriefingGenerator(state)
    conflict_detector = ConflictDetector(state)
    commitment_tracker = CommitmentTracker(state)
    risk_radar = RiskRadar(state)
    action_drafter = ActionDrafter(state)
    qa_engine = QAEngine(state)

    # 1. Briefing
    briefing = briefing_gen.generate_briefing()
    print_separator("1. MORNING EXECUTIVE BRIEFING")
    print(clean_str(briefing.greeting))
    print("\nTop Priorities:")
    for p in briefing.top_priorities:
        print(clean_str(f"  * {p}"))

    print(f"\nToday's Schedule ({briefing.day_name}):")
    for ev in briefing.todays_schedule:
        print(clean_str(f"  [{ev.start.strftime('%I:%M %p')} - {ev.end.strftime('%I:%M %p')}] {ev.event}"))

    # 2. Conflicts
    conflicts = conflict_detector.detect_conflicts()
    print_separator("2. DETECTED SCHEDULE COLLISIONS")
    if not conflicts:
        print("  No collisions detected.")
    else:
        for c in conflicts:
            print(clean_str(f"  [CLASH] [{c.severity.value}] {c.title}"))
            print(clean_str(f"     Explanation: {c.explanation}"))
            print(clean_str(f"     Recommended Fix: {c.suggested_action}"))

    # 3. Commitments
    print_separator("3. COMMITMENT STATUS")
    outbound = commitment_tracker.get_outbound()
    for o in outbound:
        print(clean_str(f"  [{o.status.value}] {o.title}"))
        print(clean_str(f"    Debtor: {o.debtor} -> Creditor: {o.creditor}"))
        print(clean_str(f"    Current Deadline: {o.current_deadline}"))
        print(clean_str(f"    Notes: {o.notes}"))

    # 4. Corporate Risks
    risks = risk_radar.detect_risks()
    print_separator("4. CORPORATE RISKS & UNOWNED LIABILITIES")
    for r in risks:
        print(clean_str(f"  [RISK] [{r.status}] {r.title}"))
        print(clean_str(f"     Deadline: {r.deadline}"))
        print(clean_str(f"     Action: {r.recommended_action}"))

    # 5. Proactive Drafts
    drafts = action_drafter.get_recommended_drafts()
    print_separator("5. ACTION CENTER: PROACTIVE DRAFTS")
    for d in drafts:
        print(clean_str(f"\n  [DRAFT] {d['title']}"))
        print(clean_str(f"      To: {d['to']}"))
        print(clean_str(f"      Subject: {d['subject']}"))
        print(clean_str(f"      Rationale: {d['rationale']}"))
        print("      --- Body Snippet ---")
        lines = d['body'].split('\n')
        print(clean_str("      " + "\n      ".join(lines[:4]) + "..."))

    # 6. Sample Grounded Q&A
    print_separator("6. SAMPLE GROUNDED Q&A TESTS")
    test_queries = [
        "What do I owe Raghav?",
        "Do I have any calendar conflicts on Thursday?",
        "Did Divya send the expense variance report?",
        "Who is signing the Mumbai office lease?",
        "What is our projected Q4 sales target?"  # Strict Hallucination test
    ]

    for q in test_queries:
        print(clean_str(f"\nQ: {q}"))
        res = qa_engine.answer_query(q)
        print(clean_str(f"A: {res['answer'].splitlines()[0]}"))
        print(clean_str(f"   [Grounded: {res['grounded']} | Citations: {', '.join(res['citations'][:2])}]"))

    print_separator("DEMO COMPLETE")
    print("To launch the full graphical web dashboard, run: streamlit run app.py\n")

if __name__ == "__main__":
    main()
