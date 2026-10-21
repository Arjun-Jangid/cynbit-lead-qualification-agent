
from app import score_lead


def test_high_priority():
    data = {
        "requirements": ["Build an AI chatbot"],
        "project_category": "AI/ML",
        "budget": "₹2 lakh",
        "timeline": "Next month",
        "next_step_requested": True,
    }

    score, priority, reasons = score_lead(data)

    assert score == 7
    assert priority == "High"


def test_medium_priority():
    data = {
        "requirements": ["Build a website"],
        "project_category": "Web or Mobile Development",
        "budget": None,
        "timeline": None,
        "next_step_requested": True,
    }

    score, priority, reasons = score_lead(data)

    assert score == 3
    assert priority == "Medium"


def test_low_priority():
    data = {
        "requirements": [],
        "project_category": "Unclear",
        "budget": None,
        "timeline": None,
        "next_step_requested": False,
    }

    score, priority, reasons = score_lead(data)

    assert score == 0
    assert priority == "Low"
