# Log Monitoring Script

This Python script is designed to monitor authentication logs on a Linux system for failed login attempts.

## Description
The script reads the `/var/log/auth.log` file to detect failed login attempts. It searches for lines that contain the phrase `Failed password`, which indicates an unsuccessful login attempt. The script then prints each line that corresponds to a failed login attempt.

## Features
- Opens and reads the `/var/log/auth.log` file (common on Linux systems).
- Searches for failed login attempts (identified by the string `Failed password`).
- Prints out each failed login attempt to the console.

## Requirements
- Python 3.x or higher
- Linux system with `/var/log/auth.log` file containing authentication logs

## How to Use
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/YourUsername/log-monitoring-script.git
