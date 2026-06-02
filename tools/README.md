# Tools

Security tools built from scratch using Python.
Each tool is documented with an explanation of how it works and real results.

---

## Contents

| Tool | Description | Language |
|---|---|---|
| [port-scanner.py](port-scanner.py) | TCP port scanner using raw sockets | Python |
| [crypto-demo.py](crypto-demo.py) | Hashing, symmetric and asymmetric encryption demo | Python |

---

## How to run

Make sure you have Python 3 installed.

Port scanner (no dependencies):
```
python port-scanner.py
```

Crypto demo (requires cryptography library):
```
pip install cryptography
python crypto-demo.py
```

Before running the port scanner, open the file and change the target IP to your
own machine or network. Only scan machines you own or have explicit permission to scan.

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
