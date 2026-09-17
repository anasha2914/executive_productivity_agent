"""
Data models for the Executive Productivity Agent.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any
from enum import Enum

class CommitmentStatus(str, Enum):
    PENDING = "PENDING"
    OVERDUE = "OVERDUE"
    FULFILLED = "FULFILLED"
    FLAGGED = "FLAGGED"

class CommitmentDirection(str, Enum):
    OUTBOUND = "OUTBOUND"  # Arjun owes to someone
    INBOUND = "INBOUND"    # Someone owes to Arjun
    ORGANIZATIONAL = "ORGANIZATIONAL" # Team/corporate unassigned

class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

@dataclass
class CalendarEvent:
    person: str
    day: str
    start: datetime
    end: datetime
    event: str

@dataclass
class EmailItem:
    thread_id: str
    email_id: str
    timestamp: datetime
    sender: str
    sender_name: str
    recipients: List[str]
    subject: str
    body: str

@dataclass
class Commitment:
    id: str
    title: str
    direction: CommitmentDirection
    debtor: str  # Who owes it
    creditor: str  # Who it is owed to
    initial_deadline: str
    current_deadline: str
    status: CommitmentStatus
    evidence: List[str]
    notes: str
    action_needed: bool

@dataclass
class ScheduleConflict:
    id: str
    title: str
    day: str
    severity: Severity
    conflicting_events: List[Dict[str, Any]]
    explanation: str
    suggested_action: str
    source_evidence: str

@dataclass
class RiskItem:
    id: str
    title: str
    severity: Severity
    deadline: str
    owner: str
    status: str
    description: str
    source_evidence: str
    recommended_action: str

@dataclass
class ExecutiveBriefing:
    simulated_time: datetime
    day_name: str
    greeting: str
    top_priorities: List[str]
    todays_schedule: List[CalendarEvent]
    conflicts_detected: List[ScheduleConflict]
    outbound_commitments_due: List[Commitment]
    inbound_deliverables_expected: List[Commitment]
    active_risks: List[RiskItem]
    proactive_suggestions: List[str]
