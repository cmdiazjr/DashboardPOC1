from modules.latency import check_latency
import json

print(json.dumps(check_latency(), indent=4))
