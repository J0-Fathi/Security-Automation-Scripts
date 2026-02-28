import json

print("===============================================")
print("        SIMPLE SOC LOG ANALYZER TOOL")
print("===============================================\n")

# Read JSON file

file_name = input("Enter JSON log file name (example: logs.json): ")

try:
    with open(file_name, "r") as file:
        logs = json.load(file)
except:
    print("\n[!] Error: Could not open file.")
    exit()

print("\n[+] Log file loaded successfully!\n")

# Count failed attempts

failed_count = {}
total_success = 0

for log in logs:
    if log["status"] == "failed":
        user = log["user"]

        if user in failed_count:
            failed_count[user] += 1
        else:
            failed_count[user] = 1
    elif log["status"] == "success":
        total_success += 1

# Risk Level

suspicious_users = []

for user in failed_count:
    attempts = failed_count[user]

    if attempts >= 5:
        risk = "HIGH"
    elif attempts >= 3:
        risk = "MEDIUM"
        suspicious_users.append(user)
    else:
        risk = "LOW"

    failed_count[user] = {
        "failed_attempts": attempts,
        "risk_level": risk
    }

#  Output

print("=================================================")
print("            SIMPLE SOC ANALYSIS REPORT")
print("=================================================\n")

print(f"[*] Total Successful Logins : {total_success}\n")

print("[+] Users Analysis:\n")
print("User     Failed_Attempts     Risk_Level")
print("-----------------------------------------")

for user in failed_count:
    attempts = failed_count[user]["failed_attempts"]
    risk = failed_count[user]["risk_level"]
    print(f"{user:<8} {attempts:<18} {risk}")

print("\n[!] Suspicious Users Detected:")

if suspicious_users:
    for user in suspicious_users:
        print(f"    - {user}")
else:
    print("    None")

print("\n=================================================")