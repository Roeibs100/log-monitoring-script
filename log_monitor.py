import re

# Open the log file
with open('/var/log/auth.log', 'r') as file:
    logs = file.readlines()

# Search for failed login attempts
for line in logs:
    if 'Failed password' in line:
        print(f"Failed login attempt detected: {line}")
