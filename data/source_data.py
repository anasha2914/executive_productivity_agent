"""
Source Data Pack - Assignment 1: Executive Productivity Agent
Week of Monday, 21 September 2026 – Friday, 25 September 2026.
Target Executive: Arjun Malhotra (VP Sales, Veridian Corp)
"""

PEOPLE = {
    "arjun": {
        "name": "Arjun Malhotra",
        "role": "VP Sales (Agent's User)",
        "email": "arjun.malhotra@veridian-corp.example",
        "is_user": True
    },
    "neha": {
        "name": "Neha Kapoor",
        "role": "Marketing Lead",
        "email": "neha.kapoor@veridian-corp.example",
        "is_user": False
    },
    "raghav": {
        "name": "Raghav Sethi",
        "role": "Ops Manager",
        "email": "raghav.sethi@veridian-corp.example",
        "is_user": False
    },
    "divya": {
        "name": "Divya Rao",
        "role": "Finance",
        "email": "divya.rao@veridian-corp.example",
        "is_user": False
    },
    "priya": {
        "name": "Priya Nair",
        "role": "Meridian Logistics (External Client)",
        "email": "priya.nair@meridianlogistics.example",
        "is_user": False
    },
    "facilities": {
        "name": "Facilities",
        "role": "Internal distribution list",
        "email": "facilities@veridian-corp.example",
        "is_user": False
    }
}

LEADERSHIP_SYNC_TRANSCRIPT = {
    "title": "Leadership Sync",
    "datetime": "2026-09-21T09:00:00",
    "end_datetime": "2026-09-21T09:35:00",
    "attendees": ["Arjun Malhotra", "Neha Kapoor", "Raghav Sethi", "Divya Rao"],
    "utterances": [
        {
            "speaker": "Arjun Malhotra",
            "text": "Let's keep this quick. Neha, where are we on the Q3 campaign deck?"
        },
        {
            "speaker": "Neha Kapoor",
            "text": "Draft is 80% done. I'll send it to Arjun for review by Wednesday."
        },
        {
            "speaker": "Arjun Malhotra",
            "text": "Good. Also, remind me — I told Raghav I'd send him the updated vendor list. I'll get that to him by end of day tomorrow."
        },
        {
            "speaker": "Raghav Sethi",
            "text": "Appreciated. Separately, the Mumbai office renewal paperwork needs someone to sign off this week. Not sure whose desk that's on right now."
        },
        {
            "speaker": "Divya Rao",
            "text": "I think that's supposed to be Facilities, but I haven't seen anyone pick it up."
        },
        {
            "speaker": "Arjun Malhotra",
            "text": "Okay, flag it, don't assume. Divya, can you also pull the July expense variance report before Thursday's board prep?"
        },
        {
            "speaker": "Divya Rao",
            "text": "Yes, I'll have it ready Wednesday evening."
        },
        {
            "speaker": "Arjun Malhotra",
            "text": "One more thing — client call with Meridian Logistics got pushed. I need to reconfirm the new time with their team myself."
        },
        {
            "speaker": "Neha Kapoor",
            "text": "Also, just a reminder, the campaign deck review — I said Wednesday, but realistically Thursday morning is safer."
        },
        {
            "speaker": "Arjun Malhotra",
            "text": "Noted. Let's close here."
        }
    ]
}

CALENDARS = {
    "arjun": [
        {"day": "Mon 21 Sep", "start": "2026-09-21T09:00:00", "end": "2026-09-21T09:35:00", "event": "Leadership Sync"},
        {"day": "Mon 21 Sep", "start": "2026-09-21T14:00:00", "end": "2026-09-21T14:30:00", "event": "1:1 with Neha"},
        {"day": "Mon 21 Sep", "start": "2026-09-21T16:00:00", "end": "2026-09-21T17:00:00", "event": "Blocked"},
        {"day": "Tue 22 Sep", "start": "2026-09-22T11:00:00", "end": "2026-09-22T12:00:00", "event": "Internal Budget Review"},
        {"day": "Tue 22 Sep", "start": "2026-09-22T15:00:00", "end": "2026-09-22T15:30:00", "event": "Blocked"},
        {"day": "Wed 23 Sep", "start": "2026-09-23T15:00:00", "end": "2026-09-23T15:30:00", "event": "Call — Meridian Logistics"},
        {"day": "Wed 23 Sep", "start": "2026-09-23T18:00:00", "end": "2026-09-23T18:15:00", "event": "Blocked"},
        {"day": "Thu 24 Sep", "start": "2026-09-24T09:00:00", "end": "2026-09-24T10:00:00", "event": "Board Prep Session"},
        {"day": "Thu 24 Sep", "start": "2026-09-24T16:00:00", "end": "2026-09-24T17:00:00", "event": "Hiring Panel — Sales Associate"},
        {"day": "Fri 25 Sep", "start": "2026-09-25T10:00:00", "end": "2026-09-25T10:30:00", "event": "Facilities Check-in"},
        {"day": "Fri 25 Sep", "start": "2026-09-25T13:00:00", "end": "2026-09-25T14:00:00", "event": "Blocked"},
    ],
    "neha": [
        {"day": "Mon 21 Sep", "start": "2026-09-21T10:00:00", "end": "2026-09-21T11:00:00", "event": "Blocked"},
        {"day": "Mon 21 Sep", "start": "2026-09-21T14:00:00", "end": "2026-09-21T14:30:00", "event": "1:1 with Arjun"},
        {"day": "Tue 22 Sep", "start": "2026-09-22T13:00:00", "end": "2026-09-22T14:00:00", "event": "Campaign Vendor Call"},
        {"day": "Wed 23 Sep", "start": "2026-09-23T10:00:00", "end": "2026-09-23T10:30:00", "event": "Deck Prep"},
        {"day": "Wed 23 Sep", "start": "2026-09-23T13:00:00", "end": "2026-09-23T15:00:00", "event": "Blocked"},
        {"day": "Thu 24 Sep", "start": "2026-09-24T09:30:00", "end": "2026-09-24T10:00:00", "event": "Deck Review with Arjun"},
        {"day": "Fri 25 Sep", "start": "2026-09-25T11:00:00", "end": "2026-09-25T12:00:00", "event": "Blocked"},
    ],
    "raghav": [
        {"day": "Mon 21 Sep", "start": "2026-09-21T09:00:00", "end": "2026-09-21T09:35:00", "event": "Leadership Sync"},
        {"day": "Mon 21 Sep", "start": "2026-09-21T13:00:00", "end": "2026-09-21T14:00:00", "event": "Blocked"},
        {"day": "Tue 22 Sep", "start": "2026-09-22T11:00:00", "end": "2026-09-22T12:00:00", "event": "Internal Budget Review"},
        {"day": "Tue 22 Sep", "start": "2026-09-22T15:30:00", "end": "2026-09-22T16:00:00", "event": "Ops Standup"},
        {"day": "Wed 23 Sep", "start": "2026-09-23T09:00:00", "end": "2026-09-23T11:00:00", "event": "Blocked"},
        {"day": "Thu 24 Sep", "start": "2026-09-24T14:00:00", "end": "2026-09-24T15:00:00", "event": "Blocked"},
        {"day": "Fri 25 Sep", "start": "2026-09-25T10:00:00", "end": "2026-09-25T10:30:00", "event": "Facilities Check-in"},
        {"day": "Fri 25 Sep", "start": "2026-09-25T15:00:00", "end": "2026-09-25T16:00:00", "event": "Blocked"},
    ],
    "divya": [
        {"day": "Mon 21 Sep", "start": "2026-09-21T14:30:00", "end": "2026-09-21T15:00:00", "event": "Budget Prep"},
        {"day": "Mon 21 Sep", "start": "2026-09-21T16:00:00", "end": "2026-09-21T17:00:00", "event": "Blocked"},
        {"day": "Tue 22 Sep", "start": "2026-09-22T09:00:00", "end": "2026-09-22T09:15:00", "event": "Quick Call with Arjun"},
        {"day": "Tue 22 Sep", "start": "2026-09-22T11:00:00", "end": "2026-09-22T12:00:00", "event": "Internal Budget Review"},
        {"day": "Wed 23 Sep", "start": "2026-09-23T13:00:00", "end": "2026-09-23T14:00:00", "event": "Blocked"},
        {"day": "Thu 24 Sep", "start": "2026-09-24T09:00:00", "end": "2026-09-24T10:00:00", "event": "Board Prep Session"},
        {"day": "Thu 24 Sep", "start": "2026-09-24T14:00:00", "end": "2026-09-24T15:00:00", "event": "Blocked"},
        {"day": "Fri 25 Sep", "start": "2026-09-25T10:00:00", "end": "2026-09-25T11:00:00", "event": "Blocked"},
    ]
}

EMAIL_THREADS = [
    {
        "id": "thread_1",
        "subject": "Vendor List",
        "category": "outbound_commitment",
        "emails": [
            {
                "id": "t1_e1",
                "timestamp": "2026-09-21T09:50:00",
                "sender": "raghav.sethi@veridian-corp.example",
                "sender_name": "Raghav Sethi",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Following up from the sync — can you send the updated vendor list today?"
            },
            {
                "id": "t1_e2",
                "timestamp": "2026-09-21T17:40:00",
                "sender": "arjun.malhotra@veridian-corp.example",
                "sender_name": "Arjun Malhotra",
                "recipients": ["raghav.sethi@veridian-corp.example"],
                "body": "Running behind, will send first thing tomorrow morning instead."
            },
            {
                "id": "t1_e3",
                "timestamp": "2026-09-22T09:15:00",
                "sender": "raghav.sethi@veridian-corp.example",
                "sender_name": "Raghav Sethi",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "No worries, whenever you get a chance today works."
            },
            {
                "id": "t1_e4",
                "timestamp": "2026-09-22T18:30:00",
                "sender": "arjun.malhotra@veridian-corp.example",
                "sender_name": "Arjun Malhotra",
                "recipients": ["raghav.sethi@veridian-corp.example"],
                "body": "Sorry, got pulled into board prep — will send by tomorrow (Wednesday) morning for sure."
            },
            {
                "id": "t1_e5",
                "timestamp": "2026-09-23T08:45:00",
                "sender": "raghav.sethi@veridian-corp.example",
                "sender_name": "Raghav Sethi",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Just checking — still good for this morning?"
            }
        ]
    },
    {
        "id": "thread_2",
        "subject": "Q3 Campaign Deck",
        "category": "inbound_deliverable_and_schedule",
        "emails": [
            {
                "id": "t2_e1",
                "timestamp": "2026-09-21T11:00:00",
                "sender": "neha.kapoor@veridian-corp.example",
                "sender_name": "Neha Kapoor",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Deck’s coming together, still targeting Wednesday for your review."
            },
            {
                "id": "t2_e2",
                "timestamp": "2026-09-22T16:15:00",
                "sender": "neha.kapoor@veridian-corp.example",
                "sender_name": "Neha Kapoor",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Heads up — shifting the review to Thursday morning instead of Wednesday, need one more day on the data slides."
            },
            {
                "id": "t2_e3",
                "timestamp": "2026-09-23T10:00:00",
                "sender": "arjun.malhotra@veridian-corp.example",
                "sender_name": "Arjun Malhotra",
                "recipients": ["neha.kapoor@veridian-corp.example"],
                "body": "Understood, Thursday morning works. What time exactly?"
            },
            {
                "id": "t2_e4",
                "timestamp": "2026-09-23T10:20:00",
                "sender": "neha.kapoor@veridian-corp.example",
                "sender_name": "Neha Kapoor",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Let’s say 9:30 AM Thursday, before your board prep block."
            },
            {
                "id": "t2_e5",
                "timestamp": "2026-09-24T08:00:00",
                "sender": "neha.kapoor@veridian-corp.example",
                "sender_name": "Neha Kapoor",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Deck is ready, attaching the draft ahead of our 9:30 review."
            }
        ]
    },
    {
        "id": "thread_3",
        "subject": "Call Reschedule",
        "category": "client_call",
        "emails": [
            {
                "id": "t3_e1",
                "timestamp": "2026-09-21T13:00:00",
                "sender": "priya.nair@meridianlogistics.example",
                "sender_name": "Priya Nair",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Our scheduled call this week got bumped from our side — can you propose a new time? We’re flexible Tuesday–Thursday afternoons."
            },
            {
                "id": "t3_e2",
                "timestamp": "2026-09-22T15:00:00",
                "sender": "arjun.malhotra@veridian-corp.example",
                "sender_name": "Arjun Malhotra",
                "recipients": ["priya.nair@meridianlogistics.example"],
                "body": "Apologies for the delay — how about Wednesday 3:00 PM?"
            },
            {
                "id": "t3_e3",
                "timestamp": "2026-09-22T17:45:00",
                "sender": "priya.nair@meridianlogistics.example",
                "sender_name": "Priya Nair",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Wednesday 3 PM works on our end, confirmed."
            },
            {
                "id": "t3_e4",
                "timestamp": "2026-09-23T13:30:00",
                "sender": "priya.nair@meridianlogistics.example",
                "sender_name": "Priya Nair",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Quick check — still on for 3 PM today?"
            },
            {
                "id": "t3_e5",
                "timestamp": "2026-09-23T14:00:00",
                "sender": "arjun.malhotra@veridian-corp.example",
                "sender_name": "Arjun Malhotra",
                "recipients": ["priya.nair@meridianlogistics.example"],
                "body": "Yes, confirmed, see you at 3."
            }
        ]
    },
    {
        "id": "thread_4",
        "subject": "Expense Variance Report",
        "category": "inbound_deliverable",
        "emails": [
            {
                "id": "t4_e1",
                "timestamp": "2026-09-21T14:30:00",
                "sender": "divya.rao@veridian-corp.example",
                "sender_name": "Divya Rao",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Starting on the July variance numbers, targeting Thursday morning for board prep as discussed."
            },
            {
                "id": "t4_e2",
                "timestamp": "2026-09-22T09:00:00",
                "sender": "arjun.malhotra@veridian-corp.example",
                "sender_name": "Arjun Malhotra",
                "recipients": ["divya.rao@veridian-corp.example"],
                "body": "Actually, can I get it by Wednesday evening instead? Want time to review before Thursday."
            },
            {
                "id": "t4_e3",
                "timestamp": "2026-09-22T09:40:00",
                "sender": "divya.rao@veridian-corp.example",
                "sender_name": "Divya Rao",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Wednesday evening is tight but doable, I’ll prioritize it."
            },
            {
                "id": "t4_e4",
                "timestamp": "2026-09-23T18:00:00",
                "sender": "divya.rao@veridian-corp.example",
                "sender_name": "Divya Rao",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "Report attached, sent as promised."
            },
            {
                "id": "t4_e5",
                "timestamp": "2026-09-23T18:10:00",
                "sender": "arjun.malhotra@veridian-corp.example",
                "sender_name": "Arjun Malhotra",
                "recipients": ["divya.rao@veridian-corp.example"],
                "body": "Got it, thank you — exactly what I needed before tomorrow."
            }
        ]
    },
    {
        "id": "thread_5",
        "subject": "Mumbai Office Lease Renewal",
        "category": "unowned_corporate_risk",
        "emails": [
            {
                "id": "t5_e1",
                "timestamp": "2026-09-21T10:15:00",
                "sender": "facilities@veridian-corp.example",
                "sender_name": "Facilities",
                "recipients": ["All Staff"],
                "body": "Reminder: the Mumbai office lease renewal requires an authorized signature by Friday, 25 September."
            },
            {
                "id": "t5_e2",
                "timestamp": "2026-09-22T11:00:00",
                "sender": "raghav.sethi@veridian-corp.example",
                "sender_name": "Raghav Sethi",
                "recipients": ["arjun.malhotra@veridian-corp.example", "divya.rao@veridian-corp.example"],
                "body": "Following up from the sync — has anyone confirmed who’s signing off on the Mumbai renewal? Don’t think it’s been assigned."
            },
            {
                "id": "t5_e3",
                "timestamp": "2026-09-23T09:30:00",
                "sender": "divya.rao@veridian-corp.example",
                "sender_name": "Divya Rao",
                "recipients": ["raghav.sethi@veridian-corp.example", "arjun.malhotra@veridian-corp.example"],
                "body": "Not on my end — I believe this typically sits with Facilities directly, not us."
            },
            {
                "id": "t5_e4",
                "timestamp": "2026-09-24T16:00:00",
                "sender": "facilities@veridian-corp.example",
                "sender_name": "Facilities",
                "recipients": ["All Staff"],
                "body": "Second reminder: signature is still pending. Deadline is Friday, 25 September, end of day."
            },
            {
                "id": "t5_e5",
                "timestamp": "2026-09-24T16:45:00",
                "sender": "raghav.sethi@veridian-corp.example",
                "sender_name": "Raghav Sethi",
                "recipients": ["arjun.malhotra@veridian-corp.example"],
                "body": "This is now one day out and still unowned — can you confirm who’s handling it?"
            }
        ]
    }
]

VOICE_NOTES = [
    {
        "id": "vn_1",
        "timestamp": "2026-09-21T18:40:00",
        "location": "recorded in cab",
        "author": "Arjun Malhotra",
        "text": "Quick note to self — need to get Raghav that vendor list, I think I said today but it might slip to tomorrow morning, remind me. Also still haven’t heard back on the Mumbai lease thing, someone needs to own that, I don’t think it’s me."
    },
    {
        "id": "vn_2",
        "timestamp": "2026-09-23T08:15:00",
        "location": "personal memo",
        "author": "Arjun Malhotra",
        "text": "Reminder — expense variance report from Divya needs to be in my hands by Wednesday evening, not Thursday, I want time to go through it before board prep. Also Meridian call — I owe Priya a time, need to lock that in today."
    }
]
