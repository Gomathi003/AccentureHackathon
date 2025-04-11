import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd

def render_health_metrics(health_data):
    st.subheader("Health Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Heart Rate Gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=health_data['heart_rate'],
            title={'text': "Heart Rate"},
            gauge={'axis': {'range': [0, 150]},
                   'threshold': {'line': {'color': "red", 'width': 4},
                               'thickness': 0.75,
                               'value': 100}}))
        st.plotly_chart(fig)
        
    with col2:
        # Blood Pressure Display
        st.metric("Blood Pressure", health_data['blood_pressure'])
        
    with col3:
        # Glucose Level
        st.metric("Glucose Level", f"{health_data['glucose_level']} mg/dL")

def render_activity_timeline(activities):
    st.subheader("Recent Activities")
    
    for activity in activities:
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(activity['timestamp'].strftime("%H:%M"))
            with col2:
                st.write(f"{activity['activity_type']} - {activity['location']}")
        st.divider()

def render_alerts_panel():
    st.sidebar.subheader("Active Alerts")
    
    alert_types = {
        'emergency': 'red',
        'warning': 'orange',
        'info': 'blue'
    }
    
    for alert_type, color in alert_types.items():
        if alert_type == 'emergency':
            st.sidebar.error("⚠️ Fall detected in bedroom!")
        elif alert_type == 'warning':
            st.sidebar.warning("⚠️ Medication reminder: Blood pressure pills")
        else:
            st.sidebar.info("ℹ️ Next doctor appointment: Tomorrow 10 AM")