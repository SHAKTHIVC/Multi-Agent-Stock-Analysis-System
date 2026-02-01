# 📈 Multi-Agent Stock Analysis & Trading System

An AI-powered stock market analysis system that uses **multiple autonomous agents** to analyze live market data and generate **Buy / Sell / Hold** recommendations.  
Built using **CrewAI**, **LiteLLM**, **Yahoo Finance**, and **Streamlit**.

---

## 🚀 Project Overview

The **Multi-Agent Stock Analysis & Trading System** leverages collaborative AI agents to simulate real-world financial analysis.  
Each agent is assigned a specialized role—such as market analysis and trading strategy—to collectively evaluate stock performance and assist users in making informed trading decisions.

The system fetches **real-time stock data**, analyzes trends, and presents a clear, human-readable verdict through an interactive web interface.

---

## 🎯 Key Features

- 🤖 **Multi-Agent Architecture** using CrewAI  
- 📊 **Live Stock Data** via Yahoo Finance  
- 📈 **Buy / Sell / Hold Recommendations**
- 🧠 Role-based agents (Analyst & Trader)
- 🌐 **Interactive Streamlit UI**
- 🔌 Modular & scalable design
- 🧪 Error-handled and production-safe setup

---

## 🧠 System Architecture

### Agents Used:
1. **Financial Market Analyst**
   - Analyzes current stock price and daily changes
   - Identifies trends and short-term market behavior

2. **Strategic Stock Trader**
   - Uses analysis results
   - Recommends Buy / Sell / Hold based on momentum and risk outlook

### Workflow:
User Input → Analyst Agent → Trading Agent → Final Recommendation


---

## 🛠️ Tech Stack

- **Python 3.10+**
- **CrewAI** – Multi-agent orchestration
- **LiteLLM** – LLM abstraction layer
- **Groq / OpenAI models** – Language models
- **Yahoo Finance (yfinance)** – Live stock data
- **Streamlit** – Web UI
- **dotenv** – Environment variable management

---

## 📂 Project Structure

CREWAI-MULTIAGENT/
│
├── agents/
│ ├── analyst_agent.py
│ └── trader_agent.py
│
├── tasks/
│ ├── analyse_task.py
│ └── trade_task.py
│
├── tools/
│ └── stock_research_tool.py
│
├── crew.py
├── main.py
├── requirements.txt
├── .env
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/multi-agent-stock-analysis.git
cd multi-agent-stock-analysis
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
