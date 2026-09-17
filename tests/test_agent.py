"""
Unit Tests for Executive Productivity Agent.
Covers:
1. Thursday 9:30 AM Calendar Collision detection.
2. Vendor List commitment delinquency over time.
3. Inbound deliverable delivery tracking (Divya's report).
4. Meridian Logistics rescheduling and fulfillment.
5. Mumbai Office lease renewal risk escalation.
6. Strict grounding / hallucination defense.
"""

import unittest
from datetime import datetime
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.temporal_state import TemporalState
from engine.conflict_detector import ConflictDetector
from engine.commitment_tracker import CommitmentTracker
from engine.risk_radar import RiskRadar
from engine.qa_engine import QAEngine
from engine.models import CommitmentStatus, Severity

class TestExecutiveProductivityAgent(unittest.TestCase):

    def test_thursday_calendar_collision(self):
        """Verify the Thursday 9:30 AM clash between Board Prep and Neha's Deck Review is detected."""
        # Simulated at Thursday 8:30 AM
        state = TemporalState(datetime(2026, 9, 24, 8, 30))
        detector = ConflictDetector(state)
        conflicts = detector.detect_conflicts()

        self.assertGreater(len(conflicts), 0, "Should detect at least one calendar conflict on Thursday")
        clash = conflicts[0]
        self.assertIn("Board Prep", clash.title)
        self.assertIn("Deck Review", clash.title)
        self.assertEqual(clash.day, "Thu 24 Sep")
        self.assertIn("9:30 AM", clash.explanation)

    def test_vendor_list_commitment_delinquency(self):
        """Verify vendor list commitment transitions from PENDING to OVERDUE."""
        # Mon morning: pending
        state_mon = TemporalState(datetime(2026, 9, 21, 10, 0))
        tracker_mon = CommitmentTracker(state_mon)
        comm_mon = next(c for c in tracker_mon.get_outbound() if c.id == "comm_vendor_list")
        self.assertEqual(comm_mon.status, CommitmentStatus.PENDING)

        # Wed afternoon: overdue
        state_wed = TemporalState(datetime(2026, 9, 23, 14, 0))
        tracker_wed = CommitmentTracker(state_wed)
        comm_wed = next(c for c in tracker_wed.get_outbound() if c.id == "comm_vendor_list")
        self.assertEqual(comm_wed.status, CommitmentStatus.OVERDUE)

    def test_expense_report_fulfillment(self):
        """Verify Divya's expense report is PENDING before Wed 6 PM and FULFILLED after."""
        # Wed 10 AM: pending
        state_pre = TemporalState(datetime(2026, 9, 23, 10, 0))
        tracker_pre = CommitmentTracker(state_pre)
        comm_pre = next(c for c in tracker_pre.get_inbound() if c.id == "comm_expense_report")
        self.assertEqual(comm_pre.status, CommitmentStatus.PENDING)

        # Wed 7 PM: fulfilled
        state_post = TemporalState(datetime(2026, 9, 23, 19, 0))
        tracker_post = CommitmentTracker(state_post)
        comm_post = next(c for c in tracker_post.get_inbound() if c.id == "comm_expense_report")
        self.assertEqual(comm_post.status, CommitmentStatus.FULFILLED)

    def test_meridian_logistics_call_completion(self):
        """Verify Meridian Logistics call is fulfilled after Wednesday 3:30 PM."""
        state_wed_pm = TemporalState(datetime(2026, 9, 23, 16, 0))
        tracker = CommitmentTracker(state_wed_pm)
        comm = next(c for c in tracker.get_outbound() if c.id == "comm_meridian_call")
        self.assertEqual(comm.status, CommitmentStatus.FULFILLED)

    def test_mumbai_lease_risk_escalation(self):
        """Verify Mumbai Lease renewal is flagged and escalates to CRITICAL on Thursday afternoon."""
        # Mon morning post-announcement
        state_mon = TemporalState(datetime(2026, 9, 21, 11, 0))
        radar_mon = RiskRadar(state_mon)
        risks_mon = radar_mon.detect_risks()
        self.assertGreater(len(risks_mon), 0)

        # Thu 5 PM (1 day out and unowned)
        state_thu = TemporalState(datetime(2026, 9, 24, 17, 0))
        radar_thu = RiskRadar(state_thu)
        risks_thu = radar_thu.detect_risks()
        self.assertEqual(risks_thu[0].severity, Severity.CRITICAL)
        self.assertIn("1 Day to Deadline", risks_thu[0].status)

    def test_strict_grounding_defense(self):
        """Verify the agent refuses to fabricate facts not in the Data Pack."""
        state = TemporalState(datetime(2026, 9, 24, 9, 0))
        qa = QAEngine(state)

        # Out-of-scope question
        res = qa.answer_query("What is our projected Q4 sales revenue target?")
        self.assertFalse(res["grounded"])
        self.assertIn("Strict Grounding Defense", res["answer"])

        # In-scope question
        res_valid = qa.answer_query("What do I owe Raghav?")
        self.assertTrue(res_valid["grounded"])
        self.assertIn("vendor list", res_valid["answer"].lower())
        self.assertGreater(len(res_valid["citations"]), 0)

    def test_directory_and_voice_memo_queries(self):
        """Verify people directory and personal voice memos are accurately retrieved and grounded."""
        state = TemporalState(datetime(2026, 9, 24, 9, 0))
        qa = QAEngine(state)

        # People query
        res_priya = qa.answer_query("Who is Priya Nair?")
        self.assertTrue(res_priya["grounded"])
        self.assertIn("Meridian Logistics", res_priya["answer"])

        # Voice memo query
        res_memo = qa.answer_query("What did Arjun record in the cab?")
        self.assertTrue(res_memo["grounded"])
        self.assertIn("vendor list", res_memo["answer"].lower())

if __name__ == "__main__":
    unittest.main()
