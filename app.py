"""
Executive Productivity Agent — Interactive Prototype
Built for: Arjun Malhotra (VP Sales, Veridian Corp)
AIONOS Technical Assessment — Week of 21–25 September 2026
"""

import streamlit as st
from datetime import datetime
import pandas as pd

from data.source_data import PEOPLE, LEADERSHIP_SYNC_TRANSCRIPT, CALENDARS, EMAIL_THREADS, VOICE_NOTES
from engine.temporal_state import TemporalState, SIMULATION_CHECKPOINTS
from engine.briefing_generator import BriefingGenerator
from engine.conflict_detector import ConflictDetector
from engine.commitment_tracker import CommitmentTracker
from engine.risk_radar import RiskRadar
from engine.action_drafter import ActionDrafter
from engine.qa_engine import QAEngine
from engine.models import CommitmentStatus, Severity

# Page Configuration
st.set_page_config(
    page_title="Executive Productivity Agent | Arjun Malhotra",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for modern executive aesthetic
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0F172A;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .alert-critical {
        background-color: #FEF2F2;
        border-left: 5px solid #EF4444;
        padding: 14px 18px;
        border-radius: 6px;
        margin-bottom: 12px;
    }
    .alert-warning {
        background-color: #FFFBEB;
        border-left: 5px solid #F59E0B;
        padding: 14px 18px;
        border-radius: 6px;
        margin-bottom: 12px;
    }
    .alert-success {
        background-color: #F0FDF4;
        border-left: 5px solid #10B981;
        padding: 14px 18px;
        border-radius: 6px;
        margin-bottom: 12px;
    }
    .citation-box {
        font-size: 0.82rem;
        color: #475569;
        background-color: #F1F5F9;
        border-radius: 6px;
        padding: 8px 12px;
        margin-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar - Temporal Controller & Profile
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80", width=80)
    st.markdown("### Arjun Malhotra")
    st.markdown("**VP of Sales** — Veridian Corp")
    st.caption("📧 `arjun.malhotra@veridian-corp.example`")
    st.divider()

    st.markdown("### ⏱️ Temporal Simulation Engine")
    st.caption("Change simulated time to evaluate what the agent detects at each milestone during the week:")

    checkpoint_labels = list(SIMULATION_CHECKPOINTS.keys())
    # Default to Thursday 08:30 AM where key conflict and pending tasks are most acute
    default_index = 7 if len(checkpoint_labels) > 7 else 0
    selected_label = st.selectbox("Select Simulated Time Checkpoint:", checkpoint_labels, index=default_index)
    simulated_dt = SIMULATION_CHECKPOINTS[selected_label]

    st.info(f"📅 **Current Simulated Time:**\n\n`{simulated_dt.strftime('%A, %d %B %Y - %I:%M %p')}`")

    st.divider()
    st.markdown("### 👥 Key Contacts")
    for key, p in PEOPLE.items():
        if not p.get("is_user"):
            st.markdown(f"**{p['name']}**  \n*{p['role']}*  \n`{p['email']}`")
            st.write("")

# Initialize Agent Engine at selected simulated time
state = TemporalState(simulated_dt)
briefing_gen = BriefingGenerator(state)
conflict_detector = ConflictDetector(state)
commitment_tracker = CommitmentTracker(state)
risk_radar = RiskRadar(state)
action_drafter = ActionDrafter(state)
qa_engine = QAEngine(state)

briefing = briefing_gen.generate_briefing()
conflicts = conflict_detector.detect_conflicts()
outbound_commitments = commitment_tracker.get_outbound()
inbound_commitments = commitment_tracker.get_inbound()
risks = risk_radar.detect_risks()
drafts = action_drafter.get_recommended_drafts()

# Main Header
st.markdown('<div class="main-header">Executive Productivity Agent</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-header">AI-Powered Executive Intelligence for Arjun Malhotra | Week of September 21–25, 2026</div>', unsafe_allow_html=True)

# Metric Bar
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{len(briefing.todays_schedule)}</div>
        <div class="metric-label">Today's Meetings</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    overdue_count = sum(1 for c in outbound_commitments if c.status == CommitmentStatus.OVERDUE)
    color_class = "style='color:#EF4444;'" if overdue_count > 0 else ""
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" {color_class}>{overdue_count}</div>
        <div class="metric-label">Overdue Commitments</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color:{'#EF4444' if len(conflicts) > 0 else '#10B981'};">{len(conflicts)}</div>
        <div class="metric-label">Schedule Collisions</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    critical_risks = sum(1 for r in risks if "CRITICAL" in r.status or "HIGH" in r.status)
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color:{'#EF4444' if critical_risks > 0 else '#64748B'};">{critical_risks}</div>
        <div class="metric-label">Unowned Corporate Risks</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Navigation Tabs
tab_briefing, tab_radar, tab_commitments, tab_copilot, tab_actions, tab_inspector = st.tabs([
    "🌅 Executive Briefing",
    "🚨 Conflict & Risk Radar",
    "📋 Commitments Matrix",
    "💬 Executive Copilot (Q&A)",
    "⚡ Action Center (Drafts)",
    "🔍 Source Data Pack"
])

# -------------------------------------------------------------
# TAB 1: EXECUTIVE BRIEFING
# -------------------------------------------------------------
with tab_briefing:
    st.subheader(f"☀️ Morning Intelligence Digest — {briefing.day_name}")
    st.markdown(f"*{briefing.greeting}*")

    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.markdown("#### 🎯 Top Executive Priorities")
        for p in briefing.top_priorities:
            st.markdown(f"- {p}")

        st.write("")
        st.markdown("#### 💡 Proactive Agent Suggestions")
        for s in briefing.proactive_suggestions:
            st.info(f"👉 **Action Item:** {s}")

    with col_right:
        st.markdown("#### 📅 Today's Agenda")
        if not briefing.todays_schedule:
            st.caption(f"No meetings scheduled for {briefing.day_name}.")
        else:
            for ev in briefing.todays_schedule:
                with st.container():
                    st.markdown(f"**{ev.start.strftime('%I:%M %p')} – {ev.end.strftime('%I:%M %p')}**")
                    st.markdown(f"`{ev.event}`")
                    st.divider()

# -------------------------------------------------------------
# TAB 2: CONFLICT & RISK RADAR
# -------------------------------------------------------------
with tab_radar:
    st.subheader("🚨 Proactive Conflict & Corporate Risk Radar")
    st.caption("Continuously monitors calendar overlaps, mismatched email expectations, and unassigned corporate deadlines.")

    col_conf, col_risk = st.columns(2)

    with col_conf:
        st.markdown("### 🗓️ Calendar & Scheduling Collisions")
        if not conflicts:
            st.success("✅ No calendar collisions detected for the selected period.")
        else:
            for c in conflicts:
                st.markdown(f"""
                <div class="alert-critical">
                    <h4 style="margin:0 0 8px 0; color:#B91C1C;">{c.title}</h4>
                    <p style="margin:0 0 6px 0; font-size:0.9rem;"><strong>Day:</strong> {c.day} | <strong>Severity:</strong> {c.severity.value}</p>
                    <p style="margin:0 0 6px 0; font-size:0.92rem;">{c.explanation}</p>
                    <p style="margin:0 0 4px 0; font-size:0.88rem; color:#1E293B;"><strong>Recommended Fix:</strong> {c.suggested_action}</p>
                </div>
                """, unsafe_allow_html=True)
                with st.expander("🔎 View Grounded Evidence & Conflicting Events"):
                    for ev in c.conflicting_events:
                        st.markdown(f"- **{ev['owner']}**: `{ev['event']}` ({ev['time']}) — *{ev['status']}*")
                    st.caption(f"**Source Evidence:** {c.source_evidence}")

    with col_risk:
        st.markdown("### 🏢 Unowned Corporate Liabilities & Risks")
        if not risks:
            st.success("✅ No unowned corporate risks active at this timestamp.")
        else:
            for r in risks:
                st.markdown(f"""
                <div class="alert-warning">
                    <h4 style="margin:0 0 8px 0; color:#B45309;">{r.title}</h4>
                    <p style="margin:0 0 6px 0; font-size:0.9rem;"><strong>Status:</strong> {r.status} | <strong>Deadline:</strong> {r.deadline}</p>
                    <p style="margin:0 0 6px 0; font-size:0.92rem;">{r.description}</p>
                    <p style="margin:0 0 4px 0; font-size:0.88rem; color:#1E293B;"><strong>Executive Action:</strong> {r.recommended_action}</p>
                </div>
                """, unsafe_allow_html=True)
                with st.expander("🔎 View Communication Paper Trail"):
                    st.caption(f"**Paper Trail:** {r.source_evidence}")

# -------------------------------------------------------------
# TAB 3: COMMITMENTS MATRIX
# -------------------------------------------------------------
with tab_commitments:
    st.subheader("📋 Executive Commitment & Deliverables Matrix")
    st.caption("Tracks promises made by Arjun (Outbound) and deliverables owed to Arjun (Inbound).")

    st.markdown("### 📤 Outbound Commitments (What Arjun Owes)")
    for comm in outbound_commitments:
        status_color = "🔴" if comm.status == CommitmentStatus.OVERDUE else ("🟢" if comm.status == CommitmentStatus.FULFILLED else "🟡")
        with st.expander(f"{status_color} {comm.title} — Status: {comm.status.value}", expanded=(comm.status == CommitmentStatus.OVERDUE)):
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f"**Creditor:** {comm.creditor}")
                st.markdown(f"**Initial Deadline:** {comm.initial_deadline}")
                st.markdown(f"**Current Deadline:** {comm.current_deadline}")
                st.markdown(f"**Status:** `{comm.status.value}`")
            with c2:
                st.markdown(f"**Notes:** {comm.notes}")
                st.markdown("**Evidence Trail:**")
                for e in comm.evidence:
                    st.markdown(f"- {e}")

    st.write("")
    st.markdown("### 📥 Inbound Deliverables (What Others Owe Arjun)")
    for comm in inbound_commitments:
        status_color = "🟢" if comm.status == CommitmentStatus.FULFILLED else "🟡"
        with st.expander(f"{status_color} {comm.title} — Status: {comm.status.value}", expanded=(comm.status != CommitmentStatus.FULFILLED)):
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f"**Debtor:** {comm.debtor}")
                st.markdown(f"**Agreed Deadline:** {comm.current_deadline}")
                st.markdown(f"**Status:** `{comm.status.value}`")
            with c2:
                st.markdown(f"**Notes:** {comm.notes}")
                st.markdown("**Evidence Trail:**")
                for e in comm.evidence:
                    st.markdown(f"- {e}")

# -------------------------------------------------------------
# TAB 4: EXECUTIVE COPILOT (GROUNDED Q&A)
# -------------------------------------------------------------
with tab_copilot:
    st.subheader("💬 Executive Assistant Copilot")
    st.caption("Ask questions about your commitments, schedule, team deliverables, and meetings. Grounded strictly in verified sources.")

    # Quick prompt chips
    st.markdown("**Quick Inquiries (Click to run):**")
    chip_cols = st.columns(4)
    preset_query = None

    if chip_cols[0].button("📦 What do I owe Raghav?"):
        preset_query = "What do I owe Raghav?"
    if chip_cols[1].button("🚨 Any clashes on Thursday?"):
        preset_query = "Do I have any calendar conflicts on Thursday?"
    if chip_cols[2].button("📊 Did Divya send the report?"):
        preset_query = "Did Divya send the expense variance report?"
    if chip_cols[3].button("🏢 Who is signing Mumbai lease?"):
        preset_query = "Who is signing the Mumbai office lease?"

    chip_cols_2 = st.columns(4)
    if chip_cols_2[0].button("📞 When is Meridian call?"):
        preset_query = "When is my call with Meridian Logistics?"
    if chip_cols_2[1].button("🎙️ What were my voice notes?"):
        preset_query = "What were my voice notes about?"
    if chip_cols_2[2].button("👥 Monday Leadership Sync summary"):
        preset_query = "What did we discuss in the Leadership Sync on Monday?"
    if chip_cols_2[3].button("🛡️ Test: What is Q4 Revenue?"):
        preset_query = "What is our Q4 revenue target?"

    user_query = st.text_input("Enter your executive question:", value=preset_query or "", placeholder="e.g. What commitments are overdue?")

    if user_query:
        with st.spinner("Analyzing emails, calendars, transcripts, and voice notes..."):
            response = qa_engine.answer_query(user_query)

        st.markdown(response["answer"])

        if response.get("citations"):
            st.markdown("##### 📌 Grounded Source Citations")
            for cit in response["citations"]:
                st.markdown(f"- `{cit}`")

# -------------------------------------------------------------
# TAB 5: ACTION CENTER (EMAIL DRAFTS)
# -------------------------------------------------------------
with tab_actions:
    st.subheader("⚡ Executive Action Center — One-Click Proactive Drafts")
    st.caption("Pre-drafted, contextual emails ready for Arjun's review to quickly resolve operational blockers.")

    if not drafts:
        st.info("No urgent actions required at this simulated timestamp.")
    else:
        for d in drafts:
            with st.container():
                st.markdown(f"#### ✉️ {d['title']}")
                st.caption(f"**Urgency:** `{d['urgency']}` | **Rationale:** {d['rationale']}")
                
                c_meta1, c_meta2 = st.columns(2)
                with c_meta1:
                    st.text_input("To:", value=d["to"], key=f"to_{d['id']}", disabled=True)
                with c_meta2:
                    st.text_input("Subject:", value=d["subject"], key=f"sub_{d['id']}", disabled=True)

                email_body = st.text_area("Message Body (Editable):", value=d["body"], height=200, key=f"body_{d['id']}")

                b_col1, b_col2 = st.columns([1, 4])
                with b_col1:
                    if st.button(f"Copy Draft", key=f"btn_send_{d['id']}"):
                        st.success("Draft ready for dispatch!")
                st.divider()

# -------------------------------------------------------------
# TAB 6: SOURCE DATA PACK INSPECTOR
# -------------------------------------------------------------
with tab_inspector:
    st.subheader("🔍 Grounded Source Data Pack Explorer")
    st.caption("Transparent access to the raw material grounding the agent's reasoning.")

    data_view = st.radio("Choose Source Data Category:", ["Calendars", "Email Threads", "Meeting Transcript", "Voice Notes"], horizontal=True)

    if data_view == "Calendars":
        person_select = st.selectbox("Select Person Calendar:", ["arjun", "neha", "raghav", "divya"])
        raw_cals = CALENDARS.get(person_select, [])
        df_cal = pd.DataFrame(raw_cals)
        st.dataframe(df_cal, use_container_width=True)

    elif data_view == "Email Threads":
        for th in EMAIL_THREADS:
            with st.expander(f"✉️ Thread: {th['subject']} ({len(th['emails'])} messages)"):
                for em in th["emails"]:
                    st.markdown(f"**[{em['timestamp']}] From: `{em['sender']}` &rarr; To: `{em['recipients']}`**")
                    st.markdown(f"> *{em['body']}*")
                    st.divider()

    elif data_view == "Meeting Transcript":
        st.markdown(f"### {LEADERSHIP_SYNC_TRANSCRIPT['title']}")
        st.caption(f"Time: {LEADERSHIP_SYNC_TRANSCRIPT['datetime']} – {LEADERSHIP_SYNC_TRANSCRIPT['end_datetime']}")
        st.markdown(f"**Attendees:** {', '.join(LEADERSHIP_SYNC_TRANSCRIPT['attendees'])}")
        for u in LEADERSHIP_SYNC_TRANSCRIPT["utterances"]:
            st.markdown(f"**{u['speaker']}**: {u['text']}")

    elif data_view == "Voice Notes":
        for vn in VOICE_NOTES:
            st.markdown(f"**🎙️ {vn['timestamp']} ({vn['location']}) — Dictated by {vn['author']}**")
            st.info(f"\"{vn['text']}\"")
