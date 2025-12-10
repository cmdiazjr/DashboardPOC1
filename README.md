# DashboardPOC1  
### Real-Time IT Operations Monitoring Dashboard  
**Technologies:** Python, Dash, Plotly, psutil, pythonping  
**Author:** Carlos Diaz  

---

## 📌 Overview  
DashboardPOC1 is a **real-time IT Operations Dashboard** designed to simulate and visualize the health of a modern network environment.  
It demonstrates the core skills expected of a **Network Engineer, Cloud Engineer, NOC Analyst, or SRE**, including:

- Network latency monitoring  
- System performance metrics  
- Security event feed  
- Device health status modeling  
- Real-time updates every 5 seconds  
- Modular architecture following real production patterns  

This project was built as a **portfolio-ready Proof of Concept (POC)** to showcase engineering ability, dashboard development, and operational awareness.

---

## 🚀 Features

### ✔ **1. Network Latency Monitoring**
Pings multiple external endpoints (Google DNS, Cloudflare, GitHub)  
Displays color-coded latency bars for:

- UP (Green)  
- DEGRADED (Yellow)  
- DOWN (Red)

---

### ✔ **2. System Metrics (Local Machine)**
Uses `psutil` to capture:

- CPU usage  
- Memory consumption  
- Disk utilization  

Refreshes every 5 seconds.

---

### ✔ **3. Security Event Feed (Simulated)**
Generges realistic rotating events such as:

- FAILED_LOGIN  
- FIREWALL_BLOCK  
- PORT_SCAN  
- VPN_DISCONNECT  

Used to demonstrate log ingestion and alerting concepts.

---

### ✔ **4. Device Health Panel**
Aggregates multiple signals to determine:

- Router health  
- Firewall health  
- Switch status  
- VPN Gateway status  
- Cloud Provider availability  
- Internet status  

Color-coded for quick NOC visibility.

---

## 🏗 Project Structure

```
DashboardPOC1/
│
├── app.py
├── README.md
│
├── modules/
│   ├── latency.py
│   ├── system_metrics.py
│   ├── security_feed.py
│   └── device_health.py
│
└── venv/  (ignored)
```

---

## ▶️ How to Run Locally

### 1. Install dependencies:
```
pip install -r requirements.txt
```

### 2. Start the dashboard:
```
python app.py
```

### 3. Open your browser to:
```
http://127.0.0.1:8050/
```

---

## 🖼 Example Screenshot

Include a screenshot like the one you posted for maximum portfolio impact.

Example placeholder:

```
/Screenshots/dashboard_running.png
```

---

## 🎯 Purpose of this Project

This dashboard was designed to:
- Demonstrate real-time data handling  
- Build a visually appealing, functional IT monitoring tool  
- Showcase operational knowledge  
- Serve as a **portfolio project for job applications**  
- Prepare for roles in:
  - Network Engineering  
  - Cloud Operations  
  - NOC/SOC  
  - Site Reliability Engineering  
  - DevOps  
  - MSP technical roles  

---

## 📬 Contact  
**Carlos Diaz**  
📧 cmdiazjr@gmail.com  
🔗 linkedin.com/in/carlos-diaz-networkcloud

---

## ⭐ Future Enhancements  
Potential improvements for v2:

- Add time-series history charts  
- Add SNMP polling for real routers/switches  
- Add cloud provider API checks (AWS, Azure)  
- Export dashboard as Docker container  
- Store event logs in SQLite or Redis  
- Add authentication to the dashboard  

---

### ⭐ If you found this project helpful or interesting, please star the repository!
