import streamlit as st
from ui.dashboard import Dashboard
from agents.health_agent import HealthAgent
from agents.safety_agent import SafetyAgent
import threading
import time

def main():
    # Initialize agents
    health_agent = HealthAgent()
    safety_agent = SafetyAgent()
    
    # Initialize and render dashboard
    dashboard = Dashboard()
    dashboard.render()

if __name__ == "__main__":
    main()

"""
pip install streamlit plotly pandas sqlalchemy numpy
streamlit run app.py
"""