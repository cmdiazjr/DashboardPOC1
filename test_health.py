from modules.device_health import get_device_health
import json

print(json.dumps(get_device_health(), indent=4))
