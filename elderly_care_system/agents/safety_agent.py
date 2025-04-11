from datetime import datetime, timedelta
from utils.notifications import send_alert

class SafetyAgent:
    def __init__(self):
        self.inactivity_threshold = timedelta(hours=2)
        self.last_activity = {}
        
    def monitor_activity(self, elder_id, activity_data):
        current_time = datetime.now()
        self.last_activity[elder_id] = current_time
        
        # Check for falls
        if activity_data.get('acceleration', 0) > 20:  # Threshold for fall detection
            self._handle_fall_alert(elder_id, activity_data['location'])
            
        # Check for inactivity
        self._check_inactivity(elder_id)
    
    def _handle_fall_alert(self, elder_id, location):
        alert_msg = f"FALL DETECTED - Elder ID: {elder_id}, Location: {location}"
        send_alert('emergency', alert_msg)
        
    def _check_inactivity(self, elder_id):
        if elder_id in self.last_activity:
            time_diff = datetime.now() - self.last_activity[elder_id]
            if time_diff > self.inactivity_threshold:
                alert_msg = f"INACTIVITY ALERT - No movement detected for Elder ID: {elder_id}"
                send_alert('caregiver', alert_msg)