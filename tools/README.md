# Tools

Security tools built from scratch using Python.
Each tool is documented with an explanation of how it works and real results.

---

## Contents

| Tool | Description | Language |
|---|---|---|
| [port-scanner.py](port-scanner.py) | TCP port scanner using raw sockets | Python |
| [crypto-demo.py](crypto-demo.py) | Hashing, symmetric and asymmetric encryption demo | Python |
| [azure-security-checker.py](azure-security-checker.py) | Automated Azure security baseline audit | Python |
| [log-analyzer.py](log-analyzer.py) | Suspicious login detector from auth logs | Python |

---

## How to run

**Port scanner** (no dependencies):
```
python port-scanner.py
```

**Crypto demo** (requires cryptography library):
```
pip install cryptography
python crypto-demo.py
```

**Azure Security Checker** (requires Azure SDK and Azure CLI login):
```
pip install azure-identity azure-mgmt-storage azure-mgmt-network
az login
python azure-security-checker.py
```

**Log Analyzer** (no dependencies):
```
python log-analyzer.py
```

The log analyzer automatically creates a sample auth.log file if none exists.
To analyze a real log file replace samples/auth.log with your own log.

---

## Port reference

| Port | Service | Security note |
|---|---|---|
| 21 | FTP | Often misconfigured, avoid exposing publicly |
| 22 | SSH | Should use key-based auth, not passwords |
| 23 | Telnet | Completely unencrypted, should never be open |
| 25 | SMTP | Email server, check for open relay |
| 53 | DNS | Normal on routers, risky on public servers |
| 80 | HTTP | Unencrypted web, should redirect to 443 |
| 443 | HTTPS | Encrypted web, preferred over port 80 |
| 3389 | RDP | Common attack target, never expose publicly |
| 8080 | HTTP alt | Often used for admin panels, check access control |
