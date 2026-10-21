# Technical Approach Report: Lead Qualification Assistant

## 1. Objective

The goal of this project is to help a sales team understand customer inquiries and decide which leads need attention first. The app uses AI to extract information and Python to calculate a lead score.

This is a proof of concept, not a production-ready system.

## 2. Technologies Used

- **Python:** Handles the application logic and lead scoring.
- **Streamlit:** Creates the web interface.
- **Groq API:** Uses an LLM to understand customer inquiries.
- **JSON:** Stores the extracted information and allows users to download results.
- **python-dotenv:** Loads the API key from a local `.env` file.

The model name can be changed using the `GROQ_MODEL` environment variable.

## 3. How It Works

1. The user enters a customer inquiry or selects a sample.
2. The app checks that the input is not empty or too short.
3. The inquiry is sent to Groq, which extracts the project details and returns JSON.
4. Python calculates the lead score using fixed rules.
5. The app displays the score, priority, requirements, budget, timeline, and missing information.
6. The user can download the result as a JSON file.

## 4. Lead Scoring

The app uses the following rules:

- Specific project requirements: +2 points
- Budget provided: +2 points
- Timeline provided: +2 points
- Customer requests contact or next steps: +1 point

Priority is assigned based on the total score:

- **High:** 5–7 points
- **Medium:** 3–4 points
- **Low:** 0–2 points

This scoring method is simple and easy to understand. It is based on fixed rules, not a trained machine learning model. The rules should be reviewed and tested before using them with real customers.

## 5. Prompt and Error Handling

The system prompt tells the model which information to extract and how to format its response.

It also instructs the model not to guess missing details or calculate the lead score. Python handles the scoring so that the same rules are applied to every inquiry.

The app handles missing input and API or JSON errors. Users should still check the results against the original inquiry because AI can make mistakes.

## 6. Privacy and Security

- The API key is stored in a local `.env` file.
- The `.env` file is excluded from Git using `.gitignore`.
- Sample inquiries are used for testing.
- Inquiry text is sent to Groq for analysis, so confidential customer data should not be used without proper authorization.
- The prototype does not include authentication, a database, or CRM integration.

## 7. Testing

The app should be tested with different types of inquiries, including:

- A detailed inquiry with a budget and timeline.
- An inquiry with missing information.
- A cloud or software development request.

Testing should also cover missing API keys, API errors, lead score calculation, and JSON downloads.

## 8. Running and Submitting the Project

1. Install the required Python packages.
2. Add the Groq API key to the local `.env` file.
3. Run the Streamlit application.
4. Test the sample inquiries and review the results.
5. Push the project to GitHub without uploading the API key.
6. Submit the repository URL and setup instructions.

## 9. Future Improvements

- Improve the scoring rules using feedback from the sales team.
- Test the app against reviewed sample inquiries.
- Add more automated tests.
- Add authentication and secure data storage.
