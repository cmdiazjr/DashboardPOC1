from modules.system_metrics import get_system_metrics
import json

print(json.dumps(get_system_metrics(), indent=4))
