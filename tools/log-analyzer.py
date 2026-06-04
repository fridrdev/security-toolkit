import re
from datetime import datetime
from collections import defaultdict
import os

LOG_FILE = "samples/auth.log"
BRUTE_FORCE_THRESHOLD = 5
BRUTE_FORCE_WINDOW = 60
OFFICE_HOURS_START = 6
OFFICE_HOURS_END = 22

sample_logs = """Jan 15 02:30:01 server sshd[1234]: Failed password for admin from 192.168.1.100 port 22 ssh2
Jan 15 02:30:05 server sshd[1234]: Failed password for admin from 192.168.1.100 port 22 ssh2
Jan 15 02:30:09 server sshd[1234]: Failed password for admin from 192.168.1.100 port 22 ssh2
Jan 15 02:30:13 server sshd[1234]: Failed password for admin from 192.168.1.100 port 22 ssh2
Jan 15 02:30:17 server sshd[1234]: Failed password for admin from 192.168.1.100 port 22 ssh2
Jan 15 02:30:21 server sshd[1234]: Accepted password for admin from 192.168.1.100 port 22 ssh2
Jan 15 03:15:00 server sshd[1234]: Accepted password for john from 203.0.113.50 port 22 ssh2
Jan 15 09:00:00 server sshd[1234]: Accepted password for alice from 192.168.1.10 port 22 ssh2
Jan 15 09:05:00 server sshd[1234]: Accepted password for alice from 192.168.1.10 port 22 ssh2
Jan 15 23:45:00 server sshd[1234]: Accepted password for bob from 10.0.0.5 port 22 ssh2
"""

os.makedirs("samples", exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write(sample_logs)
    print("[OK] Sample log file created at samples/auth.log\n")

failed_logins = defaultdict(list)
findings = []

print("=" * 60)
print("LOG ANALYZER: SUSPICIOUS LOGIN DETECTOR")
print("=" * 60)

def parse_line(line):
    pattern = r'(\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}).*?(Failed password|Accepted password) for (\w+) from ([\d.]+)'
    match = re.search(pattern, line)
    if match:
        timestamp_str = match.group(1)
        event_type = match.group(2)
        user = match.group(3)
        ip = match.group(4)
        try:
            timestamp = datetime.strptime(f"2024 {timestamp_str}", "%Y %b %d %H:%M:%S")
        except:
            return None
        return {"timestamp": timestamp, "event": event_type, "ip": ip, "user": user}
    return None

with open(LOG_FILE, "r") as f:
    lines = f.readlines()

events = []
for line in lines:
    parsed = parse_line(line)
    if parsed:
        events.append(parsed)

print(f"[*] Parsed {len(events)} events from log file\n")

# CHECK 1: Brute force detection
print("[*] Checking for brute force attempts...")
for event in events:
    if event["event"] == "Failed password":
        failed_logins[event["ip"]].append(event["timestamp"])

brute_force_ips = set()
for ip, timestamps in failed_logins.items():
    timestamps.sort()
    for i in range(len(timestamps)):
        window = [t for t in timestamps[i:] if (t - timestamps[i]).seconds <= BRUTE_FORCE_WINDOW]
        if len(window) >= BRUTE_FORCE_THRESHOLD:
            brute_force_ips.add(ip)
            finding = f"Brute force from {ip}: {len(window)} failed logins in {BRUTE_FORCE_WINDOW} seconds"
            if finding not in findings:
                findings.append(finding)
                print(f"  [HIGH]     {finding}")
            break
    else:
        print(f"  [OK]       {ip}: {len(timestamps)} failed login(s), below threshold")

# CHECK 2: Login outside office hours
print("\n[*] Checking for logins outside office hours...")
for event in events:
    if event["event"] == "Accepted password":
        hour = event["timestamp"].hour
        if hour < OFFICE_HOURS_START or hour >= OFFICE_HOURS_END:
            finding = f"Login outside office hours: {event['user']} from {event['ip']} at {event['timestamp'].strftime('%H:%M:%S')}"
            findings.append(finding)
            print(f"  [MEDIUM]   {finding}")
        else:
            print(f"  [OK]       {event['user']} logged in at {event['timestamp'].strftime('%H:%M:%S')}, within office hours")

# CHECK 3: Successful login after brute force
print("\n[*] Checking for successful login after brute force...")
found_post_brute = False
for event in events:
    if event["event"] == "Accepted password" and event["ip"] in brute_force_ips:
        finding = f"Successful login after brute force: {event['user']} from {event['ip']}"
        findings.append(finding)
        print(f"  [CRITICAL] {finding}")
        found_post_brute = True
if not found_post_brute:
    print("  [OK]       No successful logins from brute force IPs detected")

# REPORT
print()
print("=" * 60)
print("SECURITY REPORT")
print("=" * 60)
if not findings:
    print("No suspicious activity detected.")
else:
    print(f"{len(findings)} finding(s):\n")
    for f in findings:
        print(f"  {f}")
print("=" * 60)
print(f"Analysis complete. {len(findings)} finding(s) total.")
print("=" * 60)