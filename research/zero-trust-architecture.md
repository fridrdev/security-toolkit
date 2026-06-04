# Zero Trust Architecture: Research Writeup

> **Author:** Mohamed Amin
> **Date:** June 2026
> **Topic:** Zero Trust security model, implementation and comparison with traditional perimeter security

---

## What is Zero Trust?

Zero Trust is a security model based on one principle: never automatically trust
anyone or anything, even if they are already inside your network. Every request
is verified every time regardless of where it comes from.

The term was coined by John Kindervag at Forrester Research in 2010 and has
since become the dominant security architecture model in enterprise environments.
NIST published the official framework in SP 800-207 in 2020.

---

## Why Zero Trust Replaced the Castle Model

Traditional security worked like a castle with a moat.

```
TRADITIONAL PERIMETER MODEL

Internet
   |
[ Firewall ] <-- hard outer shell
   |
+---------------------------+
|     Trusted Network       |
|  Everything inside is     |
|  automatically trusted    |
|                           |
|  PC -- Server -- Database |
|                           |
+---------------------------+

Problem: once an attacker is inside the moat
they can move freely to any resource
```

This model fails for three reasons:

**Insider threats** are not stopped because internal traffic is trusted by default.

**Stolen credentials** give an attacker the same free movement as a legitimate user.

**Lateral movement** during attacks like ransomware is possible because there
are no internal barriers. An attacker who compromises one machine can reach all others.

---

## The Zero Trust Model

```
ZERO TRUST MODEL

Internet
   |
[ Identity Verification ]
[ Device Compliance Check ]
[ Conditional Access Policy ]
   |
+--------+    +--------+    +--------+
| Zone A |    | Zone B |    | Zone C |
|  Apps  |    |  Data  |    |  VMs   |
+--------+    +--------+    +--------+
     |              |              |
     +---- No direct paths --------+
           between zones without
           explicit authorization

Every request verified. Every zone isolated.
No free movement even after initial access.
```

The key difference: there is no trusted zone. Every request from every user,
device, and application is verified against policy before access is granted.

---

## The 5 Pillars of Zero Trust

### 1. Identity

Verify who the user is on every request. Do not trust a user just because
they logged in once.

Controls: MFA, SSO, conditional access policies, privileged access management.

Example: a user logs in from an unusual country at 3am. The conditional access
policy detects the anomaly and blocks the login or requires additional
verification even though the password is correct.

### 2. Devices

Verify that the device making the request is trusted, managed, and compliant
with security policies.

Controls: device enrollment, endpoint protection, patch compliance checks,
mobile device management.

Example: a user tries to access company data from a personal unmanaged laptop.
The policy blocks access because the device is not enrolled and does not have
endpoint protection installed.

### 3. Network

Micro-segmentation. Split the network into small isolated zones so that
compromising one zone does not give access to others.

Controls: network segmentation, NSG rules, firewall policies, no implicit
east-west trust between internal systems.

Example: a VM in the application zone cannot directly communicate with the
database zone unless there is an explicit allow rule. An attacker who
compromises the application server hits a wall when trying to reach the database.

### 4. Applications

Only give users access to the specific applications they need. Not the whole
network, just the application. Applications verify identity on every request.

Controls: application proxies, per-app access policies, application-level
authentication, RBAC within applications.

Example: a contractor gets access to one specific internal tool. They cannot
see any other internal application even though they are on the corporate network.

### 5. Data

Classify data by sensitivity, encrypt it, control who can access it, and log
every access event.

Controls: data classification, encryption at rest and in transit, data loss
prevention, audit logging.

Example: confidential documents are encrypted and only accessible to users
with a specific role. Every access is logged. If someone tries to download
a large amount of sensitive files an alert fires.

---

## Implementing Zero Trust in Azure

Azure provides native tools for each pillar:

| Pillar | Azure Tool |
|---|---|
| Identity | Azure Active Directory, MFA, Conditional Access, PIM |
| Devices | Microsoft Intune, Defender for Endpoint |
| Network | NSGs, Azure Firewall, Virtual Network peering with policies |
| Applications | Azure AD App Proxy, per-app Conditional Access |
| Data | Microsoft Purview, encryption, Azure Monitor logs |

### Practical steps

**Step 1:** Enable MFA for all users, especially admins. This alone stops the
majority of credential-based attacks.

**Step 2:** Configure Conditional Access policies. Block logins from untrusted
locations, require compliant devices, enforce MFA on sensitive applications.

**Step 3:** Apply Least Privilege with RBAC. No user or service should have
more permissions than their specific job requires.

**Step 4:** Segment your network with NSGs. No VM should be able to reach
another VM unless there is an explicit business reason.

**Step 5:** Enable logging and monitoring. Microsoft Defender for Cloud and
Microsoft Sentinel collect signals from all pillars and correlate them.

---

## Zero Trust vs Traditional Perimeter Security

| | Traditional Perimeter | Zero Trust |
|---|---|---|
| Trust model | Trust everything inside | Trust nothing by default |
| User verification | Once at login | Every request |
| Internal movement | Unrestricted | Blocked by default |
| Stolen credential impact | Full network access | Limited by policies |
| Insider threat protection | Weak | Strong |
| Remote work support | VPN dependent | Native |
| Complexity | Lower | Higher |

---

## Why Zero Trust Matters Now

Three trends made Zero Trust necessary:

**Cloud adoption** means resources are no longer inside a network perimeter.
They are in Azure, AWS, SaaS applications. There is no castle wall anymore.

**Remote work** means users are not inside the office network. They connect
from homes, coffee shops, client sites. The perimeter is everywhere.

**Sophisticated attacks** like ransomware use lateral movement to spread after
gaining initial access. Zero Trust limits the blast radius even after a breach.

---

## Key Takeaway

Zero Trust is not a product you buy. It is a security philosophy and
architecture. You implement it gradually by applying its principles across
identity, devices, network, applications, and data. The goal is not to prevent
every breach but to limit what an attacker can do after one.

---

*References: NIST SP 800-207, Microsoft Zero Trust documentation, Forrester Research*
