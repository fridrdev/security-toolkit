from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.network import NetworkManagementClient

SUBSCRIPTION_ID = "your-subscription-id-here"

credential = DefaultAzureCredential()

findings = []

print("=" * 60)
print("AZURE SECURITY BASELINE CHECKER")
print("=" * 60)

print("\n[*] Checking storage accounts for public access...")

storage_client = StorageManagementClient(credential, SUBSCRIPTION_ID)

try:
    for account in storage_client.storage_accounts.list():
        if account.allow_blob_public_access:
            findings.append({
                "severity": "HIGH",
                "resource": account.name,
                "type": "Storage Account",
                "issue": "Public blob access is enabled"
            })
            print(f"  [HIGH]   {account.name}: public blob access enabled")
        else:
            print(f"  [OK]     {account.name}: public access disabled")
except Exception as e:
    print(f"  [ERROR]  Could not check storage accounts: {e}")

print("\n[*] Checking NSG rules for dangerous open ports...")
network_client = NetworkManagementClient(credential, SUBSCRIPTION_ID)

dangerous_ports = ["22", "3389", "23", "21"]

try:
    for nsg in network_client.network_security_groups.list_all():
        for rule in nsg.security_rules or []:
            if (
                rule.direction == "Inbound"
                and rule.access == "Allow"
                and rule.source_address_prefix in ["*", "Internet", "0.0.0.0/0"]
                and rule.destination_port_range in dangerous_ports
            ):
                findings.append({
                    "severity": "CRITICAL",
                    "resource": nsg.name,
                    "type": "NSG Rule",
                    "issue": f"Port {rule.destination_port_range} open to internet"
                })
                print(f"  [CRITICAL] {nsg.name}: port {rule.destination_port_range} open to internet")
            else:
                print(f"  [OK]     {nsg.name}: rule {rule.name} looks fine")
except Exception as e:
    print(f"  [ERROR]  Could not check NSGs: {e}")

print()
print("=" * 60)
print("SECURITY REPORT")
print("=" * 60)

if not findings:
    print("No issues found.")
else:
    print(f"{len(findings)} issue(s) found:\n")
    for f in findings:
        print(f"  [{f['severity']}] {f['type']}: {f['resource']}")
        print(f"         Issue: {f['issue']}")
        print()

print("=" * 60)
print(f"Checks completed. {len(findings)} finding(s) total.")
print("=" * 60)