from modules.security_feed import get_event_feed
import json

print(json.dumps(get_event_feed(), indent=4))
