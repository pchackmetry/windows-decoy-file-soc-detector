# Windows Decoy File SOC Detector

A Windows-based SOC detection lab that monitors access to a confidential decoy file and generates security alerts using Windows Security Auditing, Sysmon, and Python.

## Project Overview

This project simulates a SOC analyst investigation of suspicious access to a sensitive-looking file.

A decoy file is placed inside:

`C:\Finance\Confidential\passwords.txt`

Windows Security Auditing generates Event ID 4663 when the file is accessed. Sysmon provides additional endpoint telemetry, while a Python-based detector analyzes the event and generates a SOC-style alert.

## Detection Workflow

```text
User / Process
      |
      v
C:\Finance\Confidential\passwords.txt
      |
      v
Windows Security Auditing
      |
      v
Event ID 4663
      |
      v
Sysmon / Windows Event Logs
      |
      v
Python Detection Logic
      |
      v
SOC Alert
      |
      v
HIGH Severity
Risk Score: 85/100