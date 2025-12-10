from modules.latency import check_latency
from modules.security_feed import get_event_feed

def get_device_health():
    latency = check_latency()
    events = get_event_feed()

    # Count VPN disconnects
    vpn_issues = sum(1 for e in events if e["event_type"] == "VPN_DISCONNECT")

    # Count firewall blocks
    firewall_blocks = sum(1 for e in events if e["event_type"] == "FIREWALL_BLOCK")

    # Device health dictionary
    health = {}

    # Router health based on 1.1.1.1 latency
    cloudflare_status = latency["Cloudflare DNS"]["status"]
    health["Router"] = cloudflare_status

    # Firewall health based on number of blocks
    if firewall_blocks > 3:
        health["Firewall"] = "DEGRADED"
    elif firewall_blocks > 7:
        health["Firewall"] = "DOWN"
    else:
        health["Firewall"] = "UP"

    # Switch (static for now)
    health["Switch"] = "UP"

    # VPN Gateway
    if vpn_issues >= 3:
        health["VPN Gateway"] = "DEGRADED"
    elif vpn_issues >= 5:
        health["VPN Gateway"] = "DOWN"
    else:
        health["VPN Gateway"] = "UP"

    # Cloud Provider based on Google DNS
    google_status = latency["Google DNS"]["status"]
    health["Cloud Provider"] = google_status

    # Internet based on combined status
    if cloudflare_status == "DOWN" and google_status == "DOWN":
        health["Internet"] = "DOWN"
    elif cloudflare_status == "DEGRADED" or google_status == "DEGRADED":
        health["Internet"] = "DEGRADED"
    else:
        health["Internet"] = "UP"

    return health
