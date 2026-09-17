# Executive Productivity Agent (Veridian Corp)

> **Built for:** Arjun Malhotra (VP Sales, Veridian Corp)  
> **Evaluation Timeline:** Week of Monday, 21 September 2026 – Friday, 25 September 2026  
> **Target Reviewer:** AIONOS Engineering Assessment Team  

---

## ⚡ Quick Start (One-Command Run)

### Option 1: Interactive Web Dashboard (Streamlit)
```bash
# Install dependencies
pip install -r requirements.txt

# Launch interactive executive dashboard
streamlit run app.py
```
*(On Windows, you can simply double-click `run.bat`)*

### Option 2: Zero-Dependency CLI Mode (Pure Python)
If you prefer running without Streamlit or web dependencies:
```bash
python cli.py
```

### Option 3: Run Automated Test Suite
```bash
python -m unittest tests/test_agent.py
```

---

## 🌟 Executive Capabilities & Edge Cases Solved

| Edge Case / Problem in Data Pack | Real-World Complication | How the Agent Detects & Solves It |
| :--- | :--- | :--- |
| **Thursday 9:30 AM Double Booking** | Neha scheduled the Q3 Campaign Deck Review for Thu 9:30–10:00 AM assuming Arjun was free before board prep. Arjun has **Board Prep Session (9:00–10:00 AM)** with Divya. | **Conflict Detector** flags direct 30-minute collision, alerts Arjun in the Morning Briefing, and auto-drafts a reschedule email to Neha proposing 10:00 AM or afternoon. |
| **Overdue Vendor List to Raghav** | Arjun promised the vendor list across Mon sync, pushed to Tue morning, pushed to Wed morning, and never sent it. Raghav emailed 3 times. | **Commitment Tracker** records all deadline slips, marks deliverable `OVERDUE`, elevates to top priority, and auto-drafts apology & dispatch note. |
| **Mumbai Office Lease Crisis** | Lease renewal requires authorized signature by **Friday 25 Sep end-of-day**. Facilities reminded twice. Raghav flagged twice. Unowned corporate liability. | **Risk Radar** tracks corporate liability, escalates severity to `CRITICAL` 1 day out, identifies Arjun's **Friday 10:00 AM Facilities Check-in** on calendar, and prepares executive sign-off action. |
| **Delivered Deliverables & Meetings** | Divya promised July Expense Variance Report for Wed evening and delivered it Wed 6:00 PM. Meridian Logistics call was held Wed 3:00 PM. | **Temporal State Engine** transitions items to `FULFILLED`, preventing false alarms while ensuring Arjun has files ready for Thursday Board Prep. |
| **Strict Grounding & Zero Hallucination** | Evaluator tests the agent with out-of-scope enterprise queries (e.g. "What is our Q4 revenue target?"). | **QA Engine** strictly bounds knowledge to Data Pack, citing exact sources and triggering **Strict Grounding Defense** against hallucinations. |

---

## 🧭 Interactive UI Tour (`app.py`)

1. **⏱️ Temporal Simulation Engine (Sidebar)**:
   - Scrub through time across the entire week (from *Monday 9:35 AM* post-sync to *Friday 5:00 PM* end-of-week).
   - Watch the agent's knowledge, alerts, and priorities dynamically evolve as new emails and voice memos arrive.
2. **🌅 Executive Morning Briefing**:
   - High-impact C-suite digest with daily meetings, top priorities, and actionable warnings.
3. **🚨 Proactive Conflict & Risk Radar**:
   - Visual cards identifying hard calendar overlaps and unassigned legal/operational liabilities.
4. **📋 Commitments & Deliverables Matrix**:
   - Separate views for Outbound promises (Arjun &rarr; others) and Inbound items (others &rarr; Arjun) with evidence logs.
5. **💬 Executive Copilot (Q&A)**:
   - Natural query interface with interactive quick-action chips and transparent source citations.
6. **⚡ Action Center (1-Click Drafts)**:
   - Pre-drafted, contextual emails ready for Arjun's review to quickly resolve operational blockers.
7. **🔍 Source Data Pack Explorer**:
   - Direct inspector for raw calendar entries, 5 email threads, meeting transcripts, and voice notes.

---

## 📂 Project Structure

```
executive_agent/
├── app.py                      # Interactive Streamlit Web Application
├── cli.py                      # Pure Python CLI Demo Runner
├── requirements.txt            # Minimal dependencies (streamlit, pandas)
├── run.bat                     # Single-click Windows launcher
├── README.md                   # Project overview and review instructions
├── ARCHITECTURE.md             # AIONOS-grade System Architecture Document
├── data/
│   ├── __init__.py
│   └── source_data.py          # Grounded representations of all 4 sections of Data Pack
├── engine/
│   ├── __init__.py
│   ├── models.py               # Dataclasses (Commitments, Conflicts, Risks, Briefings)
│   ├── temporal_state.py       # Time-travel filtering and state slicing
│   ├── conflict_detector.py    # Calendar overlap & scheduling discrepancy detection
│   ├── commitment_tracker.py   # State machine for promises & deliverables
│   ├── risk_radar.py           # Unassigned liability and corporate risk engine
│   ├── briefing_generator.py   # Daily executive morning digest generator
│   ├── action_drafter.py       # Context-aware email composer
│   └── qa_engine.py            # Grounded retrieval, question answering & hallucination defense
└── tests/
    ├── __init__.py
    └── test_agent.py           # Comprehensive automated unit test suite
```
