# CIA Triad, Encryption and Authentication

> Quick reference notes on core cybersecurity concepts.
> Covered through hands-on Python crypto demo and personal study.

---

## CIA Triad

Three pillars that every security control maps back to. They work together and
sometimes conflict with each other. Security is about finding the right balance.

**Confidentiality** — only authorized people can read the data.
Tools: encryption, access control, MFA.
Example: your password travels encrypted over HTTPS. Even if intercepted it is unreadable.

**Integrity** — data has not been modified or tampered with.
Tools: hashing (SHA-256), digital signatures, checksums.
Example: you download a file and verify its SHA-256 hash matches the one published by the website.

**Availability** — systems and data are accessible when needed.
Tools: backups, redundancy, load balancers, DDoS protection.
Example: a hospital needs its patient database available 24/7. Ransomware attacking availability can cost lives.

Why it is called a triad: the three pillars are always a set. You cannot maximize one without
affecting the others. Too much confidentiality hurts availability. Too much availability hurts
confidentiality. Security is always a balance between all three.

---

## AAA Model

**Authentication** — who are you? Proving your identity.
Examples: username and password, fingerprint, face ID, MFA, smart card.
Real life: security guard checks your ID at the door.

**Authorization** — what are you allowed to do? Happens after authentication.
Examples: RBAC, file permissions, ACLs.
Real life: your badge opens floors 1-3 but not floor 4.

**Accounting** — what did you do? Logging everything for audit trails.
Examples: log files, SIEM events, audit trails.
Real life: building records every door your badge opened and at what time.

Order matters: always authenticate first, then authorize, then log.

---

## Hashing

One way function that produces a fixed length fingerprint of any input.
Cannot be reversed. Same input always produces same output.
Change one character and the entire hash changes completely (avalanche effect).

Main algorithms: SHA-256 (secure), MD5 (broken, do not use for security).

Use cases:
- Password storage: system stores hash not plaintext password
- File integrity: verify downloaded file was not tampered with
- Digital signatures: prove a message came from a specific sender

Maps to: Integrity in CIA Triad.

---

## Symmetric Encryption (AES)

One key used for both encrypting and decrypting. Fast, used for bulk data.

Problem: how do you securely share the key with the other side?
Solution: use asymmetric encryption to share the key first.

Main algorithm: AES (Advanced Encryption Standard). Industry standard worldwide.

Maps to: Confidentiality in CIA Triad.

---

## Asymmetric Encryption (RSA)

Two mathematically linked keys. Public key and private key.
What public key encrypts, only private key can decrypt.

Share your public key with everyone. Keep your private key secret.
Anyone can send you an encrypted message. Only you can read it.

Main algorithm: RSA. Slower than AES but solves the key sharing problem.
Modern alternative: ECDH (Elliptic Curve). Faster, smaller keys, used in TLS 1.3.

Maps to: Confidentiality in CIA Triad.

---

## How TLS Combines Everything

TLS uses all three concepts together. This is what happens every time you visit an HTTPS site.

```
1. Server shares its public key via certificate
2. Client generates a random AES session key
3. Client encrypts that AES key with server's public key (RSA)
4. Server decrypts it with its private key
5. Both sides now have the same AES session key
6. All further communication uses AES (fast)
7. Hashes verify integrity of each message
```

RSA solves the key sharing problem.
AES solves the speed problem.
Hashing solves the integrity problem.
Together they make HTTPS both secure and fast.

---

*Based on: hands-on Python crypto demo, Wireshark TLS analysis, personal study*
