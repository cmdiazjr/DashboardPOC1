from pythonping import ping

# Targets to monitor
TARGETS = {
    "Cloudflare DNS": "1.1.1.1",
    "Google DNS": "8.8.8.8",
    "GitHub": "github.com"
}

def check_latency():
    results = {}

    for name, host in TARGETS.items():
        try:
            response = ping(host, count=3, timeout=1)
            latency = response.rtt_avg_ms

            # Determine status
            if latency < 50:
                status = "UP"
            elif latency < 150:
                status = "DEGRADED"
            else:
                status = "DOWN"

            results[name] = {
                "host": host,
                "latency": round(latency, 2),
                "status": status
            }

        except Exception:
            results[name] = {
                "host": host,
                "latency": None,
                "status": "DOWN"
            }

    return results
