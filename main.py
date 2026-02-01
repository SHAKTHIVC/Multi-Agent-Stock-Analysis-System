import os
import streamlit as st
from dotenv import load_dotenv
from crew import stock_crew

# ---------------- ENV FIXES ----------------
os.environ["LITELLM_LOG"] = "ERROR"
os.environ["LITELLM_LOGGING"] = "false"
os.environ["LITELLM_DISABLE_PROXY"] = "true"
os.environ["LITELLM_DISABLE_TELEMETRY"] = "true"

load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Stock Oracle",
    page_icon="📈",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("🤖 AI Stock Oracle")
st.caption("Multi-Agent Trading Intelligence powered by CrewAI")

st.divider()

# ---------------- INPUT SECTION ----------------
st.subheader("Stock Analysis")

stock = st.text_input(
    "Enter Stock Symbol",
    placeholder="TESLA | AAPL | TCS.NS | INFY.NS"
)

analyze = st.button("Analyze Stock 📊")

# ---------------- RESULT SECTION ----------------
if analyze and stock:
    with st.spinner("AI agents analyzing market data..."):
        try:
            result = stock_crew.kickoff(
                inputs={"stock": stock.upper()}
            )
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    st.success("Analysis Complete!")
    st.subheader("Final AI Verdict")
    st.markdown(result)

elif analyze:
    st.warning("Please enter a stock symbol first.")
