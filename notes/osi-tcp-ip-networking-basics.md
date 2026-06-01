# OSI Model, TCP/UDP and IP Addressing

---

## OSI Model

7 layers that standardize how network communication works. Each layer has one job.

| Layer | Name | Job | Example |
|---|---|---|---|
| 7 | Application | Interface between apps and network | HTTP, DNS, FTP |
| 6 | Presentation | Formats and encrypts data | TLS |
| 5 | Session | Opens and closes sessions | Login sessions |
| 4 | Transport | Splits data, ensures delivery | TCP, UDP |
| 3 | Network | Routes packets between networks | IP, Routers |
| 2 | Data Link | Transfers data on same network | MAC, Switches |
| 1 | Physical | Transmits raw bits | Cables, Wi-Fi |

Memory trick: All People Seem To Need Data Processing

Security relevance: firewalls work at Layer 3/4, TLS at Layer 6, ARP spoofing attacks Layer 2.

---

## TCP vs UDP

Both at Layer 4. TCP is reliable but slower, UDP is fast but no guarantees.

**TCP** establishes a connection first with a 3-way handshake, then sends data.
If a packet is lost it automatically resends it. Used for HTTP, HTTPS, SSH, FTP.

```
Client -> SYN    -> Server
Client <- SYN-ACK <- Server
Client -> ACK    -> Server
```

**UDP** fires packets with no handshake and no retransmission. Used for video
streaming, gaming, DNS. Speed matters more than perfection.

---

## IP Addressing

Every device needs a unique IP to communicate.

| Subnet | Mask | Usable Hosts |
|---|---|---|
| /24 | 255.255.255.0 | 254 |
| /16 | 255.255.0.0 | 65534 |
| /32 | 255.255.255.255 | 1 |

For 192.168.1.0/24: first address is network, last is broadcast, rest are usable.

Private ranges (not routable on internet): 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
Your router uses NAT to translate between your private IP and your public IP.

---

## Wireshark Observations

Confirmed in practice on a live home network:

- DNS queries run constantly in background without user action
- WPAD queries repeated by Windows automatically, known attack vector
- ARP traffic revealed 4 devices on network passively, no scanning needed
- TCP retransmission observed live, SYN resent automatically when first was lost
- HTTP fully readable in plaintext, HTTPS unreadable after Change Cipher Spec
- SNI field in TLS Client Hello reveals destination domain even on HTTPS
- Most traffic was QUIC not TLS over TCP, modern Google protocol over UDP

Key insight: you do not need to break encryption to learn a lot about a network.

---

*HTB Academy Introduction to Networking, Wireshark live capture*
