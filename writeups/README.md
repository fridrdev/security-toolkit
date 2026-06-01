# Writeups

Practical security analysis writeups based on hands-on lab work.
Each writeup documents a real exercise including tools used, observations,
and security findings.

---

## Contents

| Writeup | Topic | Tools |
|---|---|---|
| [Wireshark Network Analysis](wireshark-network-analysis.md) | DNS, ARP, TCP, TLS, HTTP vs HTTPS | Wireshark |
| [Port Scanner Analysis](port-scanner-analysis.md) | TCP scanning, open port analysis, security findings | Python |

---

## What you will find in each writeup

Every writeup follows the same structure:

- Lab setup: interface, IP configuration, tools used
- What I observed: real packet captures with screenshots
- Security findings: what each observation means from a security perspective
- Key takeaways: practical lessons learned

---

## Topics covered so far

- DNS analysis and WPAD spoofing risk
- ARP traffic and device discovery
- TCP 3-way handshake and retransmission
- HTTP vs HTTPS in practice
- TLS handshake and SNI leakage
- QUIC and HTTP3
- OSI model mapped to real traffic
- TCP port scanning with raw Python sockets
- Open port analysis and security implications
