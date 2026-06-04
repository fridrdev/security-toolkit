# security-toolkit

Cybersecurity learning portfolio by Mohamed Amin. Hands-on tools, writeups and
study notes covering network analysis, cryptography, web vulnerabilities,
penetration testing basics, and cloud security. Built while preparing for a
cybersecurity internship at Deloitte Belgium.

---

## Contents

### Tools
Custom security tools built from scratch in Python.

| Tool | Description |
|---|---|
| [port-scanner.py](tools/port-scanner.py) | TCP port scanner using raw Python sockets |
| [crypto-demo.py](tools/crypto-demo.py) | Hashing, symmetric and asymmetric encryption demo |
| [azure-security-checker.py](tools/azure-security-checker.py) | Automated Azure security baseline audit |

### Writeups
Practical security analysis based on real hands-on work.

| Writeup | Topic |
|---|---|
| [Wireshark Network Analysis](writeups/wireshark-network-analysis.md) | DNS, ARP, TCP, TLS, HTTP vs HTTPS |
| [Port Scanner Analysis](writeups/port-scanner-analysis.md) | TCP scanning, open port analysis, security findings |
| [Crypto Demo Analysis](writeups/crypto-demo-analysis.md) | Hashing, AES, RSA, TLS flow |
| [Juice Shop Analysis](writeups/juice-shop-analysis.md) | SQLi, XSS, security through obscurity |
| [Azure Security Checker Analysis](writeups/azure-security-checker-analysis.md) | Cloud security audit, NSG rules, storage access |

### Research
In-depth technical research documents on security concepts and architectures.

| Document | Topic |
|---|---|
| [Zero Trust Architecture](research/zero-trust-architecture.md) | Zero Trust model, 5 pillars, Azure implementation |

### Notes
Study notes per topic covered. Short and to the point.

| File | Topics |
|---|---|
| [OSI, TCP/UDP, IP Addressing](notes/osi-tcp-ip-networking-basics.md) | OSI model, TCP vs UDP, subnetting, Wireshark observations |
| [DNS, DHCP, HTTP/S, Firewalls, VPN](notes/dns-dhcp-http-firewall-vpn.md) | DNS resolution, DHCP, HTTP vs HTTPS, stateless vs stateful, IPsec vs SSL-VPN |
| [CIA Triad, Encryption, Authentication](notes/cia-triad-encryption-auth.md) | CIA triad, hashing, AES, RSA, TLS, AAA model |
| [OWASP, Attacks, CVE/CVSS](notes/owasp-attacks-cve.md) | SQLi, XSS, Broken Auth, IDOR, phishing, MITM, ransomware, CVE, CVSS |
| [Azure Security, RBAC, Zero Trust](notes/azure-cloud-security-rbac.md) | Shared Responsibility, Defender for Cloud, RBAC, Least Privilege, NSGs |

---

## HackTheBox

Actively practicing on HackTheBox Academy and Starting Point machines.

Completed Starting Point machines:
- Meow (SSH)
- Fawn (FTP)
- Dancing (SMB)
- Redeemer (Redis)
- Appointment (SQLi)
- Sequel (MySQL)

Completed machines:
- Cap (Easy) — IDOR, pcap analysis, credential reuse, Linux capabilities privilege escalation

Academy badges:
- Academician: Introduction to Academy
- Cyber Starter: Introduction to Information Security
- Solid Basis: Network Foundations

Profile: [fridr](https://app.hackthebox.com/users/3569346)

---

## Stack

Python, Wireshark, Nmap, Docker, OWASP Juice Shop, Azure, HTB Academy

---

## Disclaimer

All tools and writeups in this repo are for educational purposes only.
Only scan and test systems you own or have explicit permission to test.
