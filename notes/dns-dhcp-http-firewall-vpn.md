# DNS, DHCP, HTTP/S, Firewalls and VPN

---

## DNS: Domain Name System

Converts domain names into IP addresses.

```
1. You type google.com
2. Query goes to DNS Resolver (your router or ISP)
3. Resolver checks cache, if empty asks Root Server
4. Root points to .com server, .com points to Google nameserver
5. Google nameserver returns the IP
6. Resolver caches it and sends it back to you
```

Port 53, uses UDP for queries and TCP for large responses.

Security risk: DNS logs reveal which services a machine contacts even without
breaking encryption. Used in SOCs to detect malware. WPAD is a known attack
where a rogue DNS response redirects all browser traffic silently.

---

## DHCP: Dynamic Host Configuration Protocol

Automatically gives devices their network config when they join a network.
Without it you configure IP, subnet mask, gateway and DNS manually on every device.

DORA process:
```
Discover -> device asks "is there a DHCP server?"
Offer    <- server says "here is an IP for you"
Request  -> device says "I want that IP"
ACK      <- server confirms
```

Server also sends gateway and DNS addresses. Security risk: rogue DHCP server
can send fake gateway to redirect all traffic.

---

## HTTP and HTTPS

Both transfer web content at Layer 7.

**HTTP** is unencrypted. Everything is readable in plaintext by anyone on the
network. Confirmed in Wireshark, full HTML response visible on neverssl.com.

**HTTPS** adds TLS on top of HTTP. Process after TCP handshake:
```
Client Hello  -> browser offers cipher suites
Server Hello  <- server picks one
Certificate   <- server proves identity
Change Cipher Spec -> encryption starts, nothing readable after this
```

SNI leakage: destination domain is still visible in Client Hello even on HTTPS.
Content is encrypted but not the destination.

---

## Firewalls and ACLs

ACL is the rulebook, firewall is the enforcer.

**Stateless** looks at each packet alone, no memory, no history. Fast but easy to bypass.

**Stateful** tracks active connections. Knows if a packet belongs to an existing
session or arrived unsolicited. Much harder to bypass.

**IDS** detects and alerts but does not block. Passive, out of band.
**IPS** detects and blocks. Active, traffic passes through it inline.

---

## VPN: Virtual Private Network

Encrypted tunnel between two endpoints. Nobody in the middle can read the traffic.

**IPsec** operates at Layer 3. Site-to-site, connects two office networks
permanently. Requires configuration on both ends.

**SSL-VPN** operates at Layer 7 using TLS. Remote access for one person
connecting temporarily. Works through a browser or lightweight client.

Key difference: IPsec connects two networks. SSL-VPN connects one person.

VPN vs Proxy: proxy handles one app only. VPN encrypts all traffic from the
entire device at network level.

---

*HTB Academy Introduction to Networking, Wireshark live capture*
