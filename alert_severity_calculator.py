# Alert Severity Calculator
# Helps SOC analysts determine alert priority

print("=" * 60)
print("SOC Alert Severity Calculator")
print("=" * 60)
print()
# Get alert details from user
print("Enter alert details:\n")

alert_type = input("Alert type (malware/phishing/brute_force/unauthorized_access): ").lower()
source_ip = input("Source IP address: ")
failed_attempts = int(input("Number of failed attempts (0 if not applicable): "))
affected_systems = int(input("Number of affected systems: "))
severity_score = 0

if (alert_type == "malware"):
    severity_score += 30
elif alert_type == "phising":
    severity_score += 20
elif alert_type == "brute force":
    severity_score += 25
elif alert_type == "unauthorized access":
    severity_score += 25

    if (failed_attempts >= 500 ):
        severity_score += 20
    elif failed_attempts >= 100:
        severity_score +=15
    elif failed_attempts >= 10:
        severity_score += 10
    elif failed_attempts >= 5:
        severity_score += 5
        if affected_systems >= 5:
            severity_score += 20
        elif affected_systems >= 2:
            severity_score += 10
        else:
            severity_score += 5
# Determine severity level
if severity_score >= 61:
    severity_level = "HIGH"
elif severity_score >= 31:
    severity_level = "MEDIUM"
else:
    severity_level = "LOW"

print("\n" + "=" * 50)
print("ANALYSIS RESULT")
print("=" * 50)
print(f"Alert Type: {alert_type}")
print(f"Source IP: {source_ip}")
print(f"Failed Attempts: {failed_attempts}")
print(f"Affected Systems: {affected_systems}")
print(f"\nSeverity Score: {severity_score}")
print(f"Priority Level: {severity_level}")
print("=" * 50)
  