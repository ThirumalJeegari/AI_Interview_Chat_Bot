# AI Interview Chat Bot

## Project Overview

This project is an AI-powered Interview Chat Bot built using:

* Streamlit (Frontend)
* FastAPI (Backend)
* OpenAI / Groq API (AI Model)

The application generates interview questions based on:

* Programming Language
* Topic
* Difficulty Level
* Question Type

---

# Technologies Used

## Frontend

* Streamlit

## Backend

* FastAPI

## AI Model

* OpenAI SDK
* Llama 3.1 8B Instant Model

---

# Project Structure

```text
ai_interview_chat_bot/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml
```

---

# Frontend Explanation (`app.py`)

The frontend is created using Streamlit.

It collects user input such as:

* Language
* Topic
* Difficulty Level
* Question Type

Then it sends the prompt to the AI model and displays the generated questions.

---

## Important Components

### Import Libraries

```python
import streamlit as st
from openai import OpenAI
```

* `streamlit` is used for UI
* `OpenAI` is used to connect with the AI model

---

### Streamlit Form

```python
with st.form("Details"):
```

This creates a form for user inputs.

---

### Input Fields

```python
Lang = st.text_input("Enter the Language")
Topic = st.text_input("Enter the Topic")
```

These fields collect text input from the user.

---

### Dropdown Selection

```python
Level = st.selectbox(...)
Type = st.selectbox(...)
```

Used for selecting difficulty and question type.

---

### AI Prompt

```python
prompt = f"""
Give me Questions in {Lang} Language ...
"""
```

This prompt is sent to the AI model.

---

### AI Response

```python
response = client.chat.completions.create(...)
```

This sends the prompt to the AI model and receives the response.

---

### Display Output

```python
st.write(response.choices[0].message.content)
```

Displays generated interview questions.

---

# Backend Explanation (`main.py`)

The backend is built using FastAPI.

It receives API requests and returns JSON responses.

---

## Import Libraries

```python
from fastapi import FastAPI, Request
```

---

## Create FastAPI App

```python
app = FastAPI()
```

Creates the FastAPI application.

---

## Home Route

```python
@app.get("/")
def home():
```

This route checks whether the backend server is running.

Output:

```json
{
  "message": "Backend Running Successfully"
}
```

---

## Questions API

```python
@app.post("/Qustions")
```

This API accepts POST requests.

It receives JSON data from the frontend.

Example:

```json
{
  "prompt": "Java OOP Questions"
}
```

---

## Read Request Data

```python
data = await req.json()
```

Reads incoming JSON data.

---

## Extract Prompt

```python
prompt = data["prompt"]
```

Gets the prompt value from JSON.

---

## Return Response

```python
return {
    "message": "Promt received",
    "prompt": prompt
}
```

Returns response back to frontend.

---

# How to Run the Project

## Step 1 — Create Virtual Environment

```bash
python -m venv .venv
```

---

## Step 2 — Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

---

## Step 3 — Install Packages

```bash
pip install streamlit fastapi uvicorn openai
```

---

# Run Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Run Frontend

```bash
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# Deploy Backend on Render

1. Push project to GitHub
2. Open Render
3. Create New Web Service
4. Connect GitHub Repository
5. Add Commands

## Build Command

```text
pip install -r requirements.txt
```

## Start Command

```text
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

# Deploy Frontend on Streamlit Cloud

1. Push project to GitHub
2. Open Streamlit Cloud
3. Select Repository
4. Deploy `app.py`

---

# Example Output

* Java MCQs
* Python Theory Questions
* SQL Coding Questions
* JavaScript Interview Questions

---

# Future Improvements

* Add Authentication
* Add Chat History
* Save Questions in Database
* Add Voice Input
* Add PDF Download Feature

---

# Author

Jeegari Thirumal

