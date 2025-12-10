import random
import time
from datetime import datetime

EVENT_TYPES = [
    "FAILED_LOGIN",
    "FIREWALL_BLOCK",
    "VPN_DISCONNECT",
    "SUSPICIOUS_IP",
    "PORT_SCAN",
    "MALWARE_ALERT"
]

SOURCES = [
    "10.1.1.25",
    "172.16.8.14",
    "192.168.1.77",
    "201.33.55.88",
    "66.249.66.1"
]

def generate_event():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event_type": random.choice(EVENT_TYPES),
        "source_ip": random.choice(SOURCES),
        "description": "Security event detected by monitoring system"
    }

def get_event_feed():
    # Return a list of 5 fresh events
    return [generate_event() for _ in range(5)]
