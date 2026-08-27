# 🧠 SafeSpace AI

AI-powered mental health and medical support assistant built using:

* FastAPI
* Streamlit
* LangChain
* LangGraph
* OpenRouter
* Ollama/Nemotron
* Twilio

SafeSpace AI provides:

* Conversational AI support
* Mental health guidance
* Medical Q&A assistance
* Emergency alert escalation
* Doctor/specialist finder
* Modern web interface

---

# 🚀 Features

## ✅ AI Medical Assistant

SafeSpace AI can:

* Answer general medical questions
* Provide mental health support
* Suggest safe self-care steps
* Encourage professional medical consultation
* Avoid harmful or unsafe advice

---

## ✅ Emergency Detection

The system detects emergency-related messages such as:

* Suicide ideation
* Self-harm
* Severe chest pain
* Breathing problems
* Dangerous situations

When detected:

* Emergency SMS alerts are triggered automatically using Twilio
* The assistant encourages immediate professional help

---

## ✅ Specialist Finder

Users can ask for:

* Doctors
* Specialists
* Hospitals
* Mental health experts

The system returns demo specialist data based on city.

---

## ✅ Modern Chat UI

Built using Streamlit with:

* Chat interface
* Tool usage badges
* Sidebar settings
* Dark UI
* Session-based conversation history

---

# 🏗️ Tech Stack

| Layer            | Technology          |
| ---------------- | ------------------- |
| Frontend         | Streamlit           |
| Backend API      | FastAPI             |
| AI Framework     | LangChain           |
| Agent Framework  | LangGraph           |
| LLM Provider     | OpenRouter          |
| Medical Model    | Nemotron via Ollama |
| Emergency Alerts | Twilio              |
| HTTP Server      | Uvicorn             |

---

# 📁 Project Structure

```bash
MEDICAL_1/
│
├── backend/
│   ├── ai_agent.py
│   ├── tools.py
│   ├── main.py
│   ├── config.py
│
├── frontend.py
├── requirements.txt
├── README.md
│
└── .venv/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd MEDICAL_1
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

OR using uv:

```bash
uv pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create `config.py`

```python
OPENROUTER_API_KEY = "your_openrouter_api_key"

TWILIO_ACCOUNT_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_FROM_NUMBER = "+1xxxxxxxxxx"

EMERGENCY_NUMBER = "+91xxxxxxxxxx"
```

---

# 🤖 OpenRouter Setup

## Create OpenRouter API Key

1. Visit:

[https://openrouter.ai](https://openrouter.ai)

2. Login
3. Create API key
4. Copy key into `config.py`

---

# 📱 Twilio Setup

## Create Twilio Account

1. Visit:

[https://www.twilio.com](https://www.twilio.com)

2. Create account
3. Get:

* Account SID
* Auth Token
* Twilio phone number

4. Add them into `config.py`

---

# ▶️ Running the Backend

Start FastAPI server:

```bash
uv run backend/main.py
```

Backend runs on:

```bash
http://localhost:8000
```

---

# ▶️ Running the Frontend

Start Streamlit app:

```bash
uv run streamlit run frontend.py
```

Frontend opens at:

```bash
http://localhost:8501
```

---

# 🧠 AI Agent Architecture

## System Flow

```text
User Input
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
LangGraph ReAct Agent
    ↓
OpenRouter LLM
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
Parsed Response
    ↓
Frontend Display
```

---

# 🛠️ Tools

## 1. ask_medgemma

Purpose:

* Medical and mental health responses

Uses:

* Nemotron/OpenRouter/Ollama model

---

## 2. trigger_emergency_alert

Purpose:

* Sends emergency SMS alerts

Uses:

* Twilio API

---

## 3. expert_finder

Purpose:

* Finds nearby doctors and specialists

Current implementation:

* Demo database

Future enhancement:

* Real hospital APIs
* Maps integration
* Geo-location support

---

# 🧩 FastAPI Endpoints

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

## Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "user_message": "I have anxiety"
}
```

Response:

```json
{
  "response": "AI response here",
  "tool_used": "ask_medgemma"
}
```

---

# 🧠 Response Parser

The parser extracts:

* Tool used
* Final AI response

This allows:

* Better frontend rendering
* Tool visibility
* Cleaner UI
* Easier debugging

---

# 🎨 Streamlit Frontend Features

## Included Features

* Chat history
* Real-time messaging
* Tool badges
* Backend status check
* Sidebar settings
* Session state memory
* Error handling
* Timeout handling

---

# 🔐 Safety Features

SafeSpace AI includes:

* Safe prompting
* Medical disclaimers
* Emergency escalation
* Restricted harmful advice
* Professional help encouragement

---

# ⚠️ Limitations

This is a demo system.

Current limitations:

* Not a licensed medical system
* Demo doctor database
* Free-tier LLM limitations
* OpenRouter free model rate limits
* No persistent database
* No authentication system

---

# 🔮 Future Improvements

Potential future upgrades:

* User authentication
* Conversation memory
* Real hospital APIs
* Voice interaction
* Multi-language support
* AI emotion detection
* PDF report generation
* Medical history tracking
* Appointment booking
* Vector database memory
* RAG architecture
* Analytics dashboard
* Docker deployment
* Kubernetes scaling

---

# 🐳 Docker Deployment (Future)

Example:

```bash
docker build -t safespace-ai .
```

```bash
docker run -p 8000:8000 safespace-ai
```

---

# ☁️ Deployment Options

## Frontend

* Streamlit Cloud
* Vercel
* Netlify

## Backend

* Render
* Railway
* AWS
* GCP
* Azure
* DigitalOcean

---

# 🧪 Example Queries

## Mental Health

```text
I feel anxious and unable to sleep
```

## Medical

```text
I have a headache for 3 days
```

## Emergency

```text
I want to harm myself
```

## Specialist Finder

```text
Find a psychiatrist in Mumbai
```

---

# 📌 Requirements

Example dependencies:

```text
fastapi
uvicorn
streamlit
requests
langchain
langgraph
langchain-openai
openai
twilio
ollama
pydantic
```

---

# 🧑‍💻 Developer Notes

Important observations during development:

* Free LLM providers may rate-limit requests
* Tool calling with some providers can be unstable
* Deterministic routing is safer for medical systems
* ReAct agents increase token usage significantly
* Nested LLM calls may cause latency

---

# 📄 License

This project is intended for:

* Educational use
* Research
* Hackathons
* AI experimentation

Not intended for:

* Real clinical diagnosis
* Emergency healthcare replacement

---

# 🙌 Acknowledgements

Technologies used:

* FastAPI
* Streamlit
* LangChain
* LangGraph
* OpenRouter
* Twilio
* Ollama

---

# 📬 Contact

For questions, contributions, or collaboration:
