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
| [Crypto Demo Analysis](crypto-demo-analysis.md) | Hashing, symmetric and asymmetric encryption, TLS flow | Python |

---

## What you will find in each writeup

Every writeup follows the same structure:

- Lab setup: tools and environment used
- What I built or observed: code, captures, or output with screenshots
- Security findings: what each result means from a security perspective
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
- SHA-256 hashing and the avalanche effect
- AES symmetric encryption
- RSA asymmetric encryption
- How TLS combines RSA and AES
- CIA Triad mapped to cryptographic concepts
