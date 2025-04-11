import numpy as np
from datetime import datetime
from utils.notifications import send_alert

class HealthAgent:
    def __init__(self):
        self.thresholds = {
            'heart_rate': {'low': 60, 'high': 100},
            'blood_pressure_systolic': {'low': 90, 'high': 140},
            'blood_pressure_diastolic': {'low': 60, 'high': 90},
            'glucose': {'low': 70, 'high': 180}
        }
    
    def analyze_vitals(self, data):
        alerts = []
        
        # Check heart rate
        if data['heart_rate'] < self.thresholds['heart_rate']['low']:
            alerts.append(f"Low heart rate detected: {data['heart_rate']}")
        elif data['heart_rate'] > self.thresholds['heart_rate']['high']:
            alerts.append(f"High heart rate detected: {data['heart_rate']}")
            
        # Process blood pressure
        sys, dia = map(int, data['blood_pressure'].split('/'))
        if sys < self.thresholds['blood_pressure_systolic']['low']:
            alerts.append(f"Low blood pressure detected: {data['blood_pressure']}")
        elif sys > self.thresholds['blood_pressure_systolic']['high']:
            alerts.append(f"High blood pressure detected: {data['blood_pressure']}")
            
        return alerts