# SOC Log Parser
# Reads log files and identifies suspicious activity

print("=" * 50)
print("SOC Log Parser")
print("=" * 50)
print()

# Get log file path from user
log_file = input("Enter log file path: ")

# Attempt to open and read the file
# try/except handles errors gracefully without crashing
try:
    # Open file in read mode ("r")
    # with automatically closes file when done
    # "as f" gives the file a short nickname
    with open(log_file, "r") as f:
        # Read ALL lines at once into a list
        logs = f.readlines()
    print(f"\n Successfully loaded {len(logs)} log entries")

except FileNotFoundError:
    # Triggers if user typed wrong file path
    print(f"\n Error: File '{log_file}' not found!")
    exit()  # Stop program - no point continuing

suspicious_patterns = [
    "failed password",
    "invalid user",
    "authentication failure",
    "maximum authentication attempts",
    "refused connect",
    "denied",
    "blocked",
    "dropped",
    "reject",
    "error",
    "critical",
    "warning",
    "segfault",
    "sql",
    "../",
    "union select",
    "unauthorized",
    "illegal",
    "attack",
    "scan"

]

print(f"\n🔍 Scanning for {len(suspicious_patterns)} suspicious patterns...")

# Empty list to store flagged log lines
suspicious_findings = []

# Loop through every line in the log file
for line in logs:
    # Check each suspicious pattern against current line
    for pattern in suspicious_patterns:
        if pattern in line.lower():
            # Pattern found! Add line to findings
            suspicious_findings.append(line)
            # break stops checking remaining patterns
            # Prevents adding same line multiple times
            break

# Display scan summary
print(f"\n{'=' * 50}")
print("SCAN RESULTS")
print(f"{'=' * 50}")
print(f"Total log entries scanned: {len(logs)}")
print(f"Suspicious entries found: {len(suspicious_findings)}")
print(f"{'=' * 50}")

# Check if any suspicious entries were found
# Empty list = False, List with items = True
if suspicious_findings:
    print("\n SUSPICIOUS ENTRIES:")
    print("-" * 50)
    
    # enumerate() loops through list with a counter
    # (suspicious_findings, 1) starts counter at 1 not 0
    for i, finding in enumerate(suspicious_findings, 1):
        # .strip() removes extra spaces and newlines
        # Makes output clean and readable
        print(f"{i}. {finding.strip()}")
else:
    # No suspicious entries found - clean log!
    print("\n No suspicious entries found!")

print(f"\n{'=' * 50}")
print("Scan Complete!")
print(f"{'=' * 50}")