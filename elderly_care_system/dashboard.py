import streamlit as st
from .components import render_health_metrics, render_activity_timeline, render_alerts_panel
import pandas as pd

class Dashboard:
    def __init__(self):
        st.set_page_config(
            page_title="Elderly Care System",
            page_icon="👴",
            layout="wide"
        )
        
    def render(self):
        st.title("Elderly Care Monitoring System")
        
        # Sidebar
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ["Dashboard", "Health Monitoring", "Activity Log", "Reminders"])
        
        if page == "Dashboard":
            self._render_dashboard()
        elif page == "Health Monitoring":
            self._render_health_page()
        elif page == "Activity Log":
            self._render_activity_page()
        elif page == "Reminders":
            self._render_reminders_page()
            
        # Always show alerts panel
        render_alerts_panel()
    
    def _render_dashboard(self):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Sample health data
            health_data = {
                'heart_rate': 75,
                'blood_pressure': '120/80',
                'glucose_level': 95
            }
            render_health_metrics(health_data)
            
            # Sample activities
            activities = [
                {'timestamp': pd.Timestamp.now(), 'activity_type': 'Walking', 'location': 'Living Room'},
                {'timestamp': pd.Timestamp.now() - pd.Timedelta(minutes=30), 'activity_type': 'Sitting', 'location': 'Kitchen'}
            ]
            render_activity_timeline(activities)
            
        with col2:
            st.subheader("Quick Actions")
            if st.button("Call Emergency"):
                st.error("Emergency services contacted!")
            if st.button("Contact Caregiver"):
                st.success("Message sent to caregiver")
    
    def _render_health_page(self):
        st.header("Health Monitoring")
        # Add detailed health monitoring interface
        
    def _render_activity_page(self):
        st.header("Activity Log")
        # Add detailed activity monitoring interface
        
    def _render_reminders_page(self):
        st.header("Reminders & Schedules")
        with st.form("add_reminder"):
            st.subheader("Add New Reminder")
            reminder_type = st.selectbox("Type", ["Medication", "Appointment", "Activity"])
            reminder_time = st.time_input("Time")
            reminder_note = st.text_area("Notes")
            if st.form_submit_button("Add Reminder"):
                st.success("Reminder added successfully!")