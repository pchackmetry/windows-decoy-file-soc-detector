# Windows Decoy File SOC Detector

A Windows-based SOC detection lab for identifying and investigating suspicious access to a sensitive-looking decoy file using Windows Security Auditing, Sysmon, PowerShell, and Python.

---

## 1. Project Overview

This project demonstrates a basic Security Operations Center (SOC) detection and investigation workflow on a Windows 10 system.

A decoy file was placed inside a directory representing confidential financial information:

`C:\Finance\Confidential\passwords.txt`

The Windows Security auditing mechanism was configured to generate security telemetry when the file was accessed.

The activity was investigated using Windows Security Event ID **4663**, which provides information about attempts to access an object such as a file.

The project also uses Sysmon to provide additional endpoint visibility and a Python-based detector to demonstrate how security telemetry can be converted into a SOC-style alert.

---

## 2. Project Objective

The main objectives of this project were:

- Create a controlled decoy-file detection scenario.
- Configure Windows auditing for file access monitoring.
- Monitor access to a sensitive-looking file.
- Generate Windows Security Event ID 4663.
- Investigate the resulting event information.
- Use Sysmon for additional endpoint visibility.
- Develop a Python-based detection component.
- Generate a simple SOC-style security alert.
- Document the investigation using screenshots and evidence.

---

## 3. Lab Environment

| Component | Details |
|---|---|
| Operating System | Windows 10 |
| Security Logging | Windows Security Event Log |
| Primary Event | Event ID 4663 |
| Endpoint Telemetry | Sysmon |
| Scripting | PowerShell |
| Detection Logic | Python |
| Test File | `C:\Finance\Confidential\passwords.txt` |
| Environment | Isolated cybersecurity lab |

---

## 4. Tools Used

### Windows Security Auditing

Windows Security auditing provides security events related to activities performed on the system.

In this project, Event ID **4663** was used to investigate access to the monitored file.

### Sysmon

Sysmon provides detailed endpoint telemetry that can help a SOC analyst investigate processes, files, and other system activity.

### PowerShell

PowerShell was used to configure, test, and investigate the Windows environment and event logs.

### Python

Python was used to demonstrate automation of the detection and alerting process.

---

## 5. Detection Scenario

The scenario simulates a user or process accessing a file that appears to contain confidential information.

The monitored path was:

```text
C:\Finance\Confidential\passwords.txt