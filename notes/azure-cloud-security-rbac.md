# Azure Security, Shared Responsibility and RBAC

> Quick reference notes on cloud security concepts.
> Covered through Azure hands-on practice, Python Azure SDK and personal study.

---

## Shared Responsibility Model

In cloud computing security responsibilities are split between the cloud provider
and the customer. The model depends on which service type you use.

| Responsibility | IaaS | PaaS | SaaS |
|---|---|---|---|
| Data | You | You | You |
| User access | You | You | You |
| Application | You | You | Provider |
| Runtime/middleware | You | Provider | Provider |
| Operating system | You | Provider | Provider |
| Infrastructure | Provider | Provider | Provider |
| Physical security | Provider | Provider | Provider |

**IaaS (Infrastructure as a Service):** provider gives you VMs, storage and
networking. You manage everything on top including OS, apps and security.
Example: Azure Virtual Machines. This is what your school project used.

**PaaS (Platform as a Service):** provider gives you a platform to deploy code
on. You manage your application and data only.
Example: Azure App Service, Google App Engine, AWS Elastic Beanstalk.

**SaaS (Software as a Service):** provider gives you a fully working app.
You manage only your data and who has access.
Example: Microsoft 365, Dropbox.

The higher you go from IaaS to SaaS the less you manage but also the less
control you have over security.

---

## Microsoft Defender for Cloud

A security management tool built into Azure that does two things: tells you
how secure your environment is right now, and detects threats and suspicious
activity.

**Secure Score:** a percentage showing how many security best practices you
have implemented out of all the ones Microsoft recommends. Example: 60 out of
100 controls implemented = 60% Secure Score. Each recommendation has an impact
score telling you how much your score improves if you fix it.

**Continuous monitoring:** Defender for Cloud monitors all your Azure resources
and alerts when something is wrong. Common findings:
- VMs without endpoint protection
- Storage accounts with public access enabled
- Missing MFA on admin accounts
- NSG rules with dangerous ports open to the internet
- Outdated operating systems

This is exactly the kind of tool Deloitte uses when auditing client Azure environments.

---

## RBAC: Role Based Access Control

A way of managing who can do what in a system by assigning roles instead of
individual permissions. You create roles with predefined permissions and assign
users to those roles.

**Azure built-in roles:**

**Owner:** full control over the resource. Can read, write, delete, and manage
who else has access.

**Contributor:** can create and manage resources but cannot grant access to
others.

**Reader:** can only view resources. Cannot make any changes.

---

## Least Privilege

Give every user, system, or application only the minimum permissions they need
to do their job. Nothing more.

Why it matters: if an account gets compromised the attacker only gets what that
account could do. If everyone has Owner access one compromised account gives
full control of everything. If accounts only have the minimum needed the blast
radius is much smaller.

In practice:
- A monitoring service that only reads metrics needs Reader only
- A CI/CD pipeline deploying to AKS needs Contributor scoped to that cluster only
- A developer building a project needs Owner on their resource group, not the whole subscription

---

## Storage Accounts and Blob Access

A storage account in Azure is a service that stores files in the cloud. Blob
storage holds any type of file: images, videos, backups, logs, documents.

By default a storage account is private. Only authorized users can access files.

Public blob access means anyone on the internet can read files without any
authentication. This is a common misconfiguration — a developer enables it
temporarily and forgets to turn it off.

Confirmed in practice: the Azure Security Baseline Checker scanned the school
subscription and found 3 storage accounts all with public access correctly disabled.

---

## NSG Rules and Dangerous Ports

An NSG (Network Security Group) is a firewall ruleset attached to a subnet or
network interface in Azure. It contains rules that allow or deny inbound and
outbound traffic.

Dangerous ports that should never be open to the internet:
- Port 22: SSH, remote shell access
- Port 3389: RDP, Windows remote desktop
- Port 23: Telnet, completely unencrypted
- Port 21: FTP, unencrypted file transfer

Confirmed in practice: the Azure Security Baseline Checker found 6 CRITICAL
findings on the school subscription — multiple VMs with port 22 and port 3389
open to the entire internet via their NSG rules.

This is one of the most common misconfigurations in Azure environments. Deloitte
flags this as critical in client audits.

---

## Connection to CIA Triad

| Finding | CIA Impact |
|---|---|
| Public blob access | Confidentiality: anyone can read sensitive files |
| Port 3389 open to internet | All three: attacker can access, modify, or destroy data |
| Port 22 open to internet | All three: full shell access to the VM |
| Missing MFA | Confidentiality: easier account takeover |

---

*Based on: Azure hands-on practice, Python Azure SDK audit tool, Microsoft Learn, personal study*
