import psutil

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu_percent": cpu,
        "memory_used": round(mem.used / (1024**3), 2),
        "memory_total": round(mem.total / (1024**3), 2),
        "disk_used": round(disk.used / (1024**3), 2),
        "disk_total": round(disk.total / (1024**3), 2)
    }
