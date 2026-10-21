# Cynbit Lead Qualification Agent (PoC)

A small Streamlit + Groq proof of concept for reviewing incoming project inquiries. It extracts the stated need, category, budget/timeline (only when explicitly mentioned), missing information, follow-up questions, and a suggested next action. A transparent Python rubric assigns a priority label.

## Why this idea?

Cynbit's public website describes custom AI/software services, a project inquiry flow, and autonomous agents that can manage leads and coordination. This prototype explores one possible way to support that workflow. It is a proposed opportunity, not a claim that Cynbit currently has this internal problem or uses this system.

## Features

- Paste a prospective customer's inquiry or try one of the sample examples.
- Use Groq to extract structured information as JSON.
- Do not infer budget or timeline if the inquiry doesn't state them.
- Score priority with explicit Python rules (not a score invented by the LLM).
- Show why a priority was assigned, missing information, and suggested follow-up questions.
- Download the result as JSON.

## Run locally

1. Install Python 3.10+.
2. Create and activate a virtual environment (recommended).
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and add your Groq API key. Never commit `.env`.
5. Run:

   ```bash
   streamlit run app.py
   ```

## Priority rubric

- +2: specific project need and category identified
- +2: budget explicitly stated
- +2: timeline explicitly stated
- +1: customer clearly requests a next step/contact
- High: 5–7; Medium: 3–4; Low: 0–2

This rubric is a transparent demo heuristic, not a trained ML model, a sales prediction, or a validated business rule. Cynbit's sales team should review and calibrate it before any real use.

## Architecture

1. User pastes an inquiry in Streamlit.
2. The app sends the inquiry to Groq with a strict extraction prompt and requests JSON.
3. The app displays the extracted fields.
4. Python applies the fixed priority rubric.
5. The user can download a JSON record.

## Limitations and responsible use

- Use fictional/sample text for the assessment demo; do not submit confidential client information.
- Groq processes the inquiry text, so users should obtain authorization before sending real customer data.
- The LLM may misinterpret text; check the original inquiry before acting.
- No CRM integration, automatic outreach, persistent database, or production authentication is included.
- Priority indicates completeness/readiness signals only; it does not determine a person's worth or guarantee conversion.
- Budget/timeline are reported only if the inquiry explicitly states them; no cost or duration is invented.

## Assessment deliverables

- `AI_Opportunity_Report.md`
- `Technical_Approach_Report.md`
- `app.py` — working PoC

## Public sources reviewed

- Cynbit services: https://www.cynbit.in/services
- Cynbit inquiry page: https://www.cynbit.in/contact
- Cynbit homepage: https://www.cynbit.in/
