# AI Interview Chat Bot

## Overview

AI Interview Chat Bot is a web application that generates interview questions using AI.

Users can select:

* Programming Language
* Topic
* Difficulty Level
* Question Type

The application uses:

* Streamlit for Frontend
* FastAPI for Backend
* Groq/OpenAI API for AI responses

---

# Technologies Used

## Frontend

* Streamlit
* Requests

## Backend

* FastAPI
* Uvicorn

## AI Model

* OpenAI SDK
* Llama 3.1 8B Instant Model

---

# Project Architecture

```text id="pm8on7"
Frontend (Streamlit)
        ↓
Backend (FastAPI)
        ↓
Groq/OpenAI API
```

---

# Project Structure

```text id="18f7eg"
AI_Interview_Chat_Bot/
│
├── Backend/
│   ├── main.py
│   └── requirements.txt
│
├── Frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── .streamlit/
│       └── secrets.toml
│
└── README.md
```

---

# Backend Code Explanation

## `main.py`

The backend is created using FastAPI.

It receives prompts from the frontend and sends them to the AI model.

---

## Import Libraries

```python id="1s1drq"
from fastapi import FastAPI, Request
from openai import OpenAI
import os
```

---

## Create FastAPI App

```python id="5drwfc"
app = FastAPI()
```

---

## Connect AI Model

```python id="7fjlwm"
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)
```

Environment variables are used for security.

---

## Home Route

```python id="j2yb44"
@app.get("/")
```

Checks whether backend is running.

---

## Questions API

```python id="72rtt0"
@app.post("/questions")
```

Receives user prompt and generates interview questions.

---

# Frontend Code Explanation

## `app.py`

Frontend is built using Streamlit.

It collects user input and sends it to the backend.

---

## Import Libraries

```python id="3nbnn9"
import streamlit as st
import requests
```

---

## Backend URL

```python id="1a0wpx"
server_url = st.secrets["backend_url"]
```

Reads backend URL from secrets file.

---

## User Inputs

```python id="t34lc5"
Lang = st.text_input()
Topic = st.text_input()
```

Collects language and topic.

---

## Dropdown Options

```python id="jlwmvr"
Level = st.selectbox(...)
Type = st.selectbox(...)
```

Selects difficulty and question type.

---

## Send Request to Backend

```python id="r9dv6n"
response = requests.post(
    server_url,
    json={
        "prompt": prompt
    }
)
```

Sends prompt to FastAPI backend.

---

## Display AI Response

```python id="x6grd7"
st.write(data["response"])
```

Displays generated interview questions.

---

# Installation

## Clone Repository

```bash id="rgo8h7"
git clone https://github.com/your-username/AI_Interview_Chat_Bot.git
```

---

# Backend Setup

## Move to Backend Folder

```bash id="gsh07q"
cd Backend
```

---

## Create Virtual Environment

```bash id="jlwm0w"
python -m venv .venv
```

---

## Activate Environment

### Windows

```bash id="7k8drg"
.venv\Scripts\activate
```

---

## Install Packages

```bash id="67m08n"
pip install -r requirements.txt
```

---

## Backend `requirements.txt`

```text id="i7fpkq"
fastapi
uvicorn
openai
python-dotenv
```

---

## Run Backend

```bash id="k4drvc"
uvicorn main:app --reload
```

Backend URL:

```text id="34rymg"
http://127.0.0.1:8000
```

Swagger Docs:

```text id="qmk4k7"
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## Move to Frontend Folder

```bash id="dt4t76"
cd Frontend
```

---

## Install Packages

```bash id="g8sy1g"
pip install -r requirements.txt
```

---

## Frontend `requirements.txt`

```text id="rv6x7m"
streamlit
requests
```

---

# Configure Streamlit Secrets

Create file:

```text id="nht7iy"
.streamlit/secrets.toml
```

Add:

```toml id="jlwmn2"
backend_url = "https://your-render-url.onrender.com/questions"
```

---

# Run Frontend

```bash id="t3l3ew"
streamlit run app.py
```

Frontend URL:

```text id="jlwmqe"
http://localhost:8501
```

---

# Deploy Backend on Render

## Steps

1. Push Backend Code to GitHub
2. Open Render
3. Create New Web Service
4. Connect GitHub Repository

---

## Build Command

```text id="3m2zy2"
pip install -r requirements.txt
```

---

## Start Command

```text id="jlwmu6"
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## Add Environment Variables

| Key      | Value                          |
| -------- | ------------------------------ |
| API_KEY  | Your API Key                   |
| BASE_URL | https://api.groq.com/openai/v1 |

---

# Deploy Frontend on Streamlit Cloud

1. Push Frontend Code to GitHub
2. Open Streamlit Cloud
3. Select Repository
4. Deploy `app.py`

---

# Features

* AI-generated interview questions
* Multiple difficulty levels
* MCQs and Coding Questions
* FastAPI backend
* Streamlit UI
* Cloud deployment support

---

# Future Improvements

* Add Authentication
* Save Chat History
* Add Voice Input
* Add PDF Export
* Add Dark Mode
* Add Multiple AI Models

---

# Author

Jeegari Thirumal
