# NIS2 and ISO 27001 Compliance Checklist: Belgian Context

> **Author:** Mohamed Amin
> **Date:** June 2026
> **Purpose:** Practical compliance reference for Belgian organizations
> **Frameworks:** NIS2 Directive (2022/2555), ISO/IEC 27001:2022, NIST CSF

---

## Overview

This checklist maps NIS2 requirements for Belgian organizations against the
most relevant ISO 27001 Annex A controls. It is designed as a practical
starting point for understanding what compliance looks like in practice.

NIS2 is a legal obligation enforced by CCB (Centre for Cybersecurity Belgium).
ISO 27001 is a voluntary certification that demonstrates NIS2 compliance in
a structured and auditable way.

---

## Part 1: NIS2 Requirements for Belgian Organizations

### Who must comply

**Essential entities** (strictest requirements):
- Energy: electricity, gas, oil operators
- Transport: aviation, rail, road, maritime
- Banking and financial market infrastructure
- Health: hospitals, pharmaceutical companies
- Drinking water and wastewater
- Digital infrastructure: DNS providers, cloud providers, internet exchange points
- Public administration (federal and regional)

**Important entities** (significant but less strict):
- Postal and courier services
- Waste management
- Chemical and food manufacturing
- Medical device manufacturers
- Digital providers: online marketplaces, search engines, social networks

---

### Mandatory security measures (Article 21)

| Requirement | Description | Status |
|---|---|---|
| Risk analysis | Conduct and document information security risk assessments | |
| Incident handling | Documented procedures for detecting, reporting and responding to incidents | |
| Business continuity | Plans for backup management, disaster recovery, crisis management | |
| Supply chain security | Assess and manage security risks from suppliers and service providers | |
| Network security | Secure acquisition, development and maintenance of network systems | |
| Security effectiveness | Policies and procedures to assess effectiveness of security measures | |
| Cyber hygiene | Basic security practices and cybersecurity training for all staff | |
| Cryptography | Policies on use of encryption and key management | |
| Access control | Human resources security, asset management, MFA where appropriate | |
| Vulnerability management | Process for handling and disclosing vulnerabilities | |

---

### Incident reporting obligations to CCB

| Timeframe | What to report |
|---|---|
| 24 hours | Early warning: significant incident occurred, initial assessment |
| 72 hours | Full notification: impact assessment, severity, indicators of compromise |
| 1 month | Final report: root cause, remediation measures, cross-border impact |

A significant incident is one that causes severe disruption to services or
financial loss, or affects other organizations or persons.

Contact: cert@ccb.belgium.be | ccb.belgium.be

---

### Penalties

| Entity type | Maximum fine |
|---|---|
| Essential entities | 10 million EUR or 2% of global annual turnover, whichever is higher |
| Important entities | 7 million EUR or 1.4% of global annual turnover, whichever is higher |

Management bodies of essential entities can be held personally liable.

---

## Part 2: ISO 27001 Annex A Top 10 Most Critical Controls

ISO 27001 Annex A contains 93 controls (2022 version) organized into 4 themes.
The following 10 are the most commonly implemented and most relevant for NIS2
compliance.

| Control | Reference | Description | NIS2 Mapping |
|---|---|---|---|
| Information security policies | A.5.1 | Documented security policies approved by management | Risk analysis, cyber hygiene |
| Access control policy | A.5.15 | Rules for granting and revoking access to assets | Access control |
| Multi-factor authentication | A.8.5 | MFA for all privileged and remote access | Access control |
| Malware protection | A.8.7 | Controls against malware on all systems | Network security |
| Logging and monitoring | A.8.15 | Collect and review logs from systems and networks | Incident handling |
| Vulnerability management | A.8.8 | Identify, evaluate and remediate vulnerabilities | Vulnerability management |
| Cryptography policy | A.8.24 | Rules for use of encryption and key management | Cryptography |
| Backup | A.8.13 | Regular backups tested for restoration | Business continuity |
| Incident management | A.5.24 | Documented process for managing security incidents | Incident handling |
| Supply chain security | A.5.19 | Agreements and monitoring of supplier security | Supply chain security |

---

## Part 3: Framework Mapping

How NIS2 requirements map to ISO 27001 controls and NIST CSF functions.

| NIS2 Requirement | ISO 27001 Controls | NIST CSF Function |
|---|---|---|
| Risk analysis | A.5.1, A.8.8 | Identify |
| Incident handling | A.5.24, A.8.15 | Detect, Respond |
| Business continuity | A.8.13, A.5.29 | Recover |
| Supply chain security | A.5.19, A.5.20 | Identify, Protect |
| Network security | A.8.7, A.8.20 | Protect |
| Cyber hygiene and training | A.6.3, A.5.1 | Protect |
| Cryptography | A.8.24 | Protect |
| Access control and MFA | A.5.15, A.8.5 | Protect |
| Vulnerability management | A.8.8 | Identify, Protect |

---

## Part 4: Implementation Priority

For a Belgian organization starting from scratch, this is the recommended
implementation order based on impact and NIS2 enforcement risk.

**Priority 1: Immediate (0 to 3 months)**
- Determine if your organization falls under NIS2 and which category
- Register with CCB if required
- Implement MFA for all admin and remote access accounts
- Set up basic logging and monitoring
- Document an incident response procedure and reporting contacts at CCB

**Priority 2: Short term (3 to 6 months)**
- Conduct a full risk assessment
- Implement backup procedures and test restoration
- Deploy vulnerability scanning on all internet-facing systems
- Train all staff on basic cyber hygiene
- Review and document supplier security agreements

**Priority 3: Medium term (6 to 12 months)**
- Pursue ISO 27001 certification to demonstrate structured compliance
- Implement full ISMS with documented policies and procedures
- Set up continuous monitoring and a SIEM solution
- Develop and test a business continuity plan
- Conduct annual penetration tests

---

## References

- NIS2 Directive: eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555
- CCB Belgium: ccb.belgium.be
- ISO 27001:2022: iso.org/standard/27001
- NIST Cybersecurity Framework: nist.gov/cyberframework
- ENISA NIS2 guidance: enisa.europa.eu

---

*Research document for educational purposes | Based on publicly available regulatory and standards documentation*
