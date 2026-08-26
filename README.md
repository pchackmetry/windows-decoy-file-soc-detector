Yes. You want **only the README text**, with no extra instructions around it.

Copy everything inside this block and paste it directly into `README.md`:

````markdown
# Windows Decoy File SOC Detector

## Windows Endpoint Detection and SOC Investigation Lab

This project demonstrates a practical Windows endpoint detection scenario using a decoy file.

The purpose of the project is to detect access to a file that appears to contain sensitive information and investigate the resulting Windows security telemetry from a SOC analyst perspective.

The project combines Windows Security Auditing, Sysmon, PowerShell, Python, and Windows Event Logs to demonstrate a basic security monitoring and detection workflow.

The complete process is:

```text
Create Confidential Directory
        ↓
Create Decoy File
        ↓
Configure Windows Auditing
        ↓
Configure Sysmon
        ↓
Generate Controlled File Access
        ↓
Capture Security Telemetry
        ↓
Investigate Event ID 4663
        ↓
Run Python Detector
        ↓
Detect Decoy File Access
        ↓
SOC Analyst Investigation
````

---

## 1. Project Objective

The objective of this project is to build a small Windows-based security monitoring lab that can identify access to a monitored decoy file.

A decoy file is designed to look interesting to an unauthorized user or attacker but does not contain real sensitive information.

If the file is accessed unexpectedly, the activity can become a security signal for investigation.

The project demonstrates how a SOC analyst can move from an endpoint event to an investigation.

The main objectives are:

* Configure Windows Security Auditing
* Monitor file access
* Configure Sysmon
* Generate controlled security activity
* Investigate Windows Security Event ID 4663
* Run a Python detection component
* Detect access to the decoy file
* Understand SOC alert triage
* Document the complete investigation

---

## 2. Security Scenario

The scenario used in this project represents a Windows workstation containing a simulated confidential financial directory.

The directory used for the laboratory is:

```text
C:\Finance\Confidential
```

A decoy file is placed inside this directory.

The file is designed to look like a sensitive file:

```text
C:\Finance\Confidential\passwords.txt
```

The file does not contain real credentials.

It is only used as a detection mechanism.

The security concept is simple:

```text
Unexpected Access
       ↓
Security Event
       ↓
Detection
       ↓
SOC Investigation
```

Instead of waiting for an attacker to access a real sensitive file, the decoy provides an early-warning signal.

---

## 3. Lab Environment

The project was performed in a controlled Windows environment.

| Component           | Details                       |
| ------------------- | ----------------------------- |
| Operating System    | Windows                       |
| Environment         | Windows Lab / Virtual Machine |
| Security Logging    | Windows Security Event Log    |
| Endpoint Monitoring | Sysmon                        |
| Scripting           | PowerShell                    |
| Detection           | Python                        |
| Version Control     | Git                           |
| Repository          | GitHub                        |

The project was performed for educational and cybersecurity portfolio purposes.

No real confidential information or credentials were used.

---

## 4. Tools Used

### Windows Security Auditing

Windows Security Auditing was used to generate security events related to file access.

### Event Viewer

Windows Event Viewer was used to review and investigate generated security events.

### Sysmon

Sysmon was used to provide additional endpoint telemetry.

### PowerShell

PowerShell was used for Windows configuration and controlled testing.

### Python

Python was used as part of the detection component.

### Git

Git was used for version control.

### GitHub

GitHub was used to store and document the project.

---

# 5. Step 1 — Configure Windows Security Auditing

The first stage of the project was configuring Windows Security Auditing.

The purpose of this step was to make file-access activity visible through Windows security logs.

A SOC analyst needs reliable endpoint telemetry to investigate suspicious activity.

Without appropriate auditing, an analyst may not be able to determine whether a sensitive-looking file was accessed.

The auditing configuration allows the Windows system to record information associated with object access.

Important information can include:

* User account
* Object name
* Object type
* Access type
* Process
* Timestamp

### Evidence

![Windows Security Audit](screenshots/01_windows_security_audit.png)

**Figure 1 — Windows Security Auditing configuration.**

### Why This Matters

Logging is one of the foundations of security monitoring.

A detection rule cannot work reliably if the activity being monitored is not generating useful telemetry.

Therefore, the first step was making file-access activity observable.

### Result

Windows Security Auditing was configured and the endpoint was prepared for the next stage.

---

# 6. Step 2 — Create the Confidential Directory

The next stage was creating a simulated confidential directory.

The directory used in this project was:

```text
C:\Finance\Confidential
```

The directory name was intentionally selected to represent a location that could contain sensitive business information.

This is only a simulated environment.

No real financial records were used.

### Evidence

![Confidential Folder Permissions](screenshots/02_confidential_folder_permissions.png)

**Figure 2 — Confidential directory and permissions.**

### Why This Matters

During an attack, an attacker may perform directory discovery and look for interesting locations.

Directories with names such as:

```text
Finance
Confidential
Passwords
Credentials
Backup
```

could attract attention.

In this project, the confidential directory provides the environment for the decoy-file detection scenario.

### Result

The simulated confidential directory was created and prepared for the decoy file.

---

# 7. Step 3 — Create the Decoy File

The next step was creating the decoy file.

The monitored file was:

```text
C:\Finance\Confidential\passwords.txt
```

The filename was intentionally chosen to appear interesting.

The file was used only as a decoy.

It did not contain real passwords or credentials.

### Why Use a Decoy?

A decoy file can provide an early-warning mechanism.

Normal users should have little reason to access a specially monitored decoy.

If the file is accessed unexpectedly, the activity can be investigated.

The basic concept is:

```text
Normal Activity
      ↓
Decoy Not Accessed
```

versus:

```text
Suspicious Activity
      ↓
Decoy Accessed
      ↓
Security Event
      ↓
SOC Investigation
```

### Result

The decoy file was created and ready for controlled testing.

---

# 8. Step 4 — Configure Sysmon

The next stage was configuring Sysmon.

Sysmon is a Windows system monitoring tool that provides additional endpoint telemetry.

The configuration used in this project is stored in:

```text
config/sysmon-config.xml
```

### Evidence

![Sysmon Configuration](screenshots/03_sysmon_configuration.png)

**Figure 3 — Sysmon configuration.**

### Why Sysmon?

Windows Security logs provide valuable information, but endpoint investigations often require additional context.

Sysmon can provide telemetry that helps analysts investigate:

* Process activity
* Process relationships
* Network connections
* System activity
* Other endpoint events

This additional information can help with event correlation.

### Result

The Sysmon configuration was prepared for the Windows endpoint.

---

# 9. Step 5 — Install Sysmon

After preparing the configuration, Sysmon was installed on the Windows endpoint.

### Evidence

![Sysmon Installation](screenshots/04_sysmon_installation.png)

**Figure 4 — Sysmon installation.**

The installation enabled additional endpoint monitoring.

### Why This Matters

When a SOC analyst receives a suspicious file-access alert, a single event may not be enough to determine what happened.

The analyst may need to investigate:

* Which process performed the activity
* Which user started the process
* What happened before the event
* What happened after the event
* Whether there was related network activity

Additional endpoint telemetry can help answer these questions.

### Result

Sysmon was installed and ready for monitoring.

---

# 10. Step 6 — Apply and Verify Sysmon Configuration

After installing Sysmon, the configuration was applied and verified.

### Evidence

![Sysmon Configuration Applied](screenshots/06_sysmon_configuration_applied.png)

**Figure 5 — Sysmon configuration applied.**

### Why Verification Is Important

Before testing a detection, the monitoring configuration should be verified.

Otherwise, a failed detection test could be caused by missing telemetry rather than a problem with the detection logic.

The verification step confirms that the endpoint is ready for testing.

### Result

The Sysmon configuration was applied and the endpoint was prepared for the detection test.

---

# 11. Step 7 — Generate Controlled Access to the Decoy File

The next stage was generating controlled access to the decoy file.

The monitored file was:

```text
C:\Finance\Confidential\passwords.txt
```

The access was intentionally generated as part of the laboratory test.

The objective was to create a known event that could later be investigated.

### Why Controlled Testing?

When developing a detection, it is important to know what activity should generate the expected event.

The testing process is:

```text
Known Action
     ↓
Expected Event
     ↓
Verify Telemetry
     ↓
Create Detection
```

This makes it easier to determine whether the detection is working as intended.

### Result

The controlled file access generated Windows security telemetry.

---

# 12. Step 8 — Investigate Windows Security Event ID 4663

After the decoy file was accessed, Windows Security logs were reviewed.

The investigation focused on:

```text
Event ID: 4663
```

Event ID 4663 can provide information about access to an object such as a file.

### Evidence

![Windows Security Event Logs](screenshots/05_sysmon_event_logs.png)

**Figure 6 — Windows Security event investigation.**

The event contained information useful for investigating the file-access activity.

Important fields include:

* Account
* Object name
* Object type
* Process
* Access type
* Timestamp

### Observed Event Information

The captured event contained information including:

```text
Event ID       : 4663
Account Name   : oxuke
Account Domain : DESKTOP-NT7M0K9
Object Type    : File
Object Name    : C:\Finance\Confidential\passwords.txt
Process Name   : C:\Windows\System32\cmd.exe
Access         : ReadData (or ListDirectory)
Access Mask    : 0x1
```

### Initial Analysis

The event provides several useful indicators.

The user associated with the activity was:

```text
oxuke
```

The accessed object was:

```text
C:\Finance\Confidential\passwords.txt
```

The process associated with the activity was:

```text
C:\Windows\System32\cmd.exe
```

The access type included:

```text
ReadData / ListDirectory
```

### Important SOC Observation

This event alone does not prove that an attack occurred.

It only tells the analyst that an access event happened.

The analyst must investigate the context.

---

# 13. Step 9 — Run the Python Detector

The next stage was running the Python detection component.

The project contains:

```text
detector.py
```

The Python component demonstrates how the monitored activity can be processed as part of a detection workflow.

### Evidence

![Decoy Detector Running](screenshots/07_decoy_detector_running.png)

**Figure 7 — Decoy detector running.**

### Why Automation?

A SOC can receive a large number of security events.

Manually reviewing every event is not practical.

Automation can help identify events that require analyst attention.

A simplified automation workflow is:

```text
Security Event
      ↓
Read Event
      ↓
Check Relevant Conditions
      ↓
Identify Decoy Access
      ↓
Generate Detection
```

### Result

The Python detector was executed as part of the laboratory workflow.

---

# 14. Step 10 — Detect the Decoy File Access

The final stage was detecting access to the monitored decoy file.

### Evidence

![Decoy File Access Detected](screenshots/08_decoy_file_access_detected.png)

**Figure 8 — Decoy file access detected.**

The detection confirms that the controlled file-access activity was identified.

The detection provides the SOC analyst with a starting point for investigation.

### Detection Workflow

```text
Decoy File Access
        ↓
Windows Security Event
        ↓
Event ID 4663
        ↓
Detection Logic
        ↓
Alert
        ↓
SOC Analyst
```

### Result

The decoy-file access was detected and became a security investigation point.

---

# 15. Example SOC Alert

A simplified SOC alert could contain information such as:

```text
==================================================
          DECOY FILE ACCESS DETECTED
==================================================

Event ID : 4663

User     : oxuke

Host     : DESKTOP-NT7M0K9

File     : C:\Finance\Confidential\passwords.txt

Process  : C:\Windows\System32\cmd.exe

Access   : ReadData / ListDirectory

==================================================
```

This information gives the analyst a starting point for triage.

---

# 16. SOC Analyst Triage

After receiving the alert, the analyst should investigate the activity instead of immediately declaring it malicious.

The first question is:

> Was this activity expected?

The investigation can be divided into several areas.

---

## 16.1 User Investigation

The observed account was:

```text
oxuke
```

The analyst should determine:

* Is this a legitimate account?
* Is the user authorized to access the directory?
* Was the user logged in at the time?
* Did the account perform other suspicious actions?

---

## 16.2 File Investigation

The accessed file was:

```text
C:\Finance\Confidential\passwords.txt
```

The analyst should determine:

* Is this the expected decoy?
* Was the file intentionally accessed?
* Were other files accessed?
* Was there unusual activity around the same time?

---

## 16.3 Process Investigation

The observed process was:

```text
C:\Windows\System32\cmd.exe
```

The analyst should investigate:

* Why was Command Prompt running?
* Which user started it?
* What commands were executed?
* Was the process launched by another suspicious process?
* Was the process expected on the endpoint?

---

## 16.4 Timeline Investigation

The analyst should review the event timestamp and correlate nearby events.

Useful events may include:

* User logon
* Failed authentication
* Process creation
* File access
* Network connections
* Other security alerts

Timeline analysis helps determine whether the decoy access was an isolated action or part of a larger sequence.

---

# 17. Detection Does Not Equal Compromise

One of the most important SOC concepts demonstrated by this project is:

> An alert is a signal for investigation, not automatic proof of compromise.

For example:

```text
Decoy File Access
        ↓
Alert
        ↓
Investigate User
        ↓
Investigate Process
        ↓
Review Timeline
        ↓
Correlate Other Events
        ↓
Determine Risk
```

A legitimate administrator could potentially access the file during testing or maintenance.

Therefore, the analyst must evaluate the context before assigning a final classification.

---

# 18. Complete SOC Workflow

The complete project workflow is:

```text
                WINDOWS ENDPOINT
                       │
                       ▼
              Confidential Folder
                       │
                       ▼
                  Decoy File
                       │
                       ▼
               File Access Activity
                       │
                       ▼
             Windows Security Audit
                       │
                       ▼
                  Event ID 4663
                       │
                       ▼
                Event Investigation
                       │
                       ▼
                Python Detection
                       │
                       ▼
                    SOC Alert
                       │
                       ▼
                  Analyst Triage
                       │
                       ▼
              Context Investigation
                       │
                       ▼
                 Final Assessment
```

---

# 19. Investigation Indicators

The following indicators were observed during the laboratory investigation:

| Indicator   | Observed Value                          |
| ----------- | --------------------------------------- |
| Event ID    | 4663                                    |
| Account     | `oxuke`                                 |
| Host        | `DESKTOP-NT7M0K9`                       |
| Object Type | File                                    |
| File        | `C:\Finance\Confidential\passwords.txt` |
| Process     | `C:\Windows\System32\cmd.exe`           |
| Access      | ReadData / ListDirectory                |
| Access Mask | `0x1`                                   |

These values can be used as starting points for additional investigation and event correlation.

---

# 20. Detection Logic

The simplified detection logic used in this project is:

```text
IF
    monitored decoy file is accessed

THEN
    identify the corresponding security event

AND

    extract relevant event information

AND

    generate a detection

AND

    provide the event information
    for SOC investigation
```

The purpose is to demonstrate the detection concept in a controlled environment.

This project should not be considered a production-ready detection platform.

---

# 21. How This Could Be Used in a Real SOC

A production SOC could expand this concept significantly.

For example:

```text
Windows Endpoint
       ↓
Windows Events
       ↓
Sysmon
       ↓
SIEM
       ↓
Detection Rule
       ↓
Alert
       ↓
SOC Analyst
       ↓
Investigation
       ↓
Incident Response
```

The detection could be integrated into platforms such as:

* Splunk
* Wazuh
* Microsoft Sentinel
* Elastic Security

The SIEM could centralize the events and allow analysts to correlate the decoy-file access with other endpoint and network activity.

---

# 22. Possible Investigation Questions

If this alert appeared in a real SOC environment, an analyst could ask:

### Identity

* Who accessed the file?
* Is the account legitimate?
* Was the account recently created?
* Was there unusual authentication activity?

### Endpoint

* Which process accessed the file?
* What was the parent process?
* What command line was used?
* Were other suspicious processes running?

### Files

* Were other files accessed?
* Were files created or modified?
* Was there evidence of data collection?

### Network

* Did the endpoint communicate with unusual destinations?
* Was there an outbound connection?
* Was there evidence of remote access?

### Timeline

* What happened before the decoy access?
* What happened after the access?
* Were there multiple related events?

---

# 23. What I Learned

This project helped me understand how endpoint telemetry can be turned into a practical SOC detection workflow.

### Windows Security Events

I learned how Windows Security events can provide useful information about object access.

### Event ID 4663

I learned how Event ID 4663 can be investigated as part of a file-access monitoring scenario.

### Sysmon

I learned how Sysmon can provide additional endpoint visibility.

### Detection Engineering

I learned that collecting logs is only the first step.

The important part is identifying relevant activity and turning it into a detection.

### SOC Investigation

I learned that an alert needs context.

A SOC analyst should investigate the user, process, file, host, timestamp, and related activity before making a final determination.

### Automation

I used Python as part of the detection workflow to demonstrate how security monitoring can be automated.

### Documentation

I documented the implementation with screenshots so that each stage of the project can be reproduced and reviewed.

---

# 24. Limitations

This project is a controlled laboratory demonstration.

There are several limitations.

### Limited Environment

The project was performed on a test Windows environment.

### Limited Detection Scope

The detector focuses on the decoy-file scenario.

### No Central SIEM

The current project does not rely on a centralized SIEM.

### Limited Correlation

The current implementation does not perform enterprise-wide correlation across multiple endpoints.

### No Automated Response

The project detects the activity but does not automatically isolate the endpoint or disable an account.

These limitations provide opportunities for future improvements.

---

# 25. Future Improvements

The project could be extended with additional capabilities.

### SIEM Integration

Integrate the detection with:

* Splunk
* Wazuh
* Microsoft Sentinel
* Elastic Security

### Multiple Decoy Files

Monitor multiple decoy files across different directories.

### Risk Scoring

Assign a risk score based on:

* User
* File
* Process
* Host
* Time
* Repeated activity

### MITRE ATT&CK Mapping

Map relevant behaviors to MITRE ATT&CK techniques.

### Automated Enrichment

Automatically collect:

* Username
* Hostname
* Process
* Parent process
* IP address
* File information

### Automated Notifications

Send alerts to a SOC communication channel or incident management system.

### SOC Dashboard

Create a dashboard showing:

* Number of decoy accesses
* Source hosts
* Users
* Processes
* Event timestamps
* Risk levels

### Incident Response

A future version could automatically initiate response actions after analyst confirmation.

---

# 26. Project Structure

```text
windows-decoy-file-soc-detector/
│
├── config/
│   └── sysmon-config.xml
│
├── screenshots/
│   ├── 01_windows_security_audit.png
│   ├── 02_confidential_folder_permissions.png
│   ├── 03_sysmon_configuration.png
│   ├── 04_sysmon_installation.png
│   ├── 05_sysmon_event_logs.png
│   ├── 06_sysmon_configuration_applied.png
│   ├── 07_decoy_detector_running.png
│   └── 08_decoy_file_access_detected.png
│
├── detector.py
├── requirements.txt
└── README.md
```

---

# 27. Evidence Summary

The repository contains screenshots documenting the main stages of the project.

| Screenshot                               | Description                             |
| ---------------------------------------- | --------------------------------------- |
| `01_windows_security_audit.png`          | Windows Security Auditing configuration |
| `02_confidential_folder_permissions.png` | Confidential directory and permissions  |
| `03_sysmon_configuration.png`            | Sysmon configuration                    |
| `04_sysmon_installation.png`             | Sysmon installation                     |
| `05_sysmon_event_logs.png`               | Security event investigation            |
| `06_sysmon_configuration_applied.png`    | Sysmon configuration verification       |
| `07_decoy_detector_running.png`          | Python detector running                 |
| `08_decoy_file_access_detected.png`      | Decoy access detection                  |

The screenshots are embedded directly into the relevant sections of this README so that the project reads as a step-by-step technical write-up.

---

# 28. Conclusion

This project demonstrates how a simple decoy file can be used as a security detection mechanism on a Windows endpoint.

The project followed a complete basic SOC workflow:

```text
Create Decoy
     ↓
Configure Auditing
     ↓
Configure Sysmon
     ↓
Generate File Access
     ↓
Capture Security Telemetry
     ↓
Investigate Event ID 4663
     ↓
Run Detection
     ↓
Generate Alert
     ↓
Perform SOC Triage
```

The most important lesson is that cybersecurity detection is not only about generating alerts.

The analyst must understand what happened, identify the user and process involved, examine the timeline, correlate related events, and determine whether the activity is legitimate or suspicious.

This project provides a practical demonstration of that process using Windows endpoint telemetry, Sysmon, Python, and a decoy file.

---

# 29. Disclaimer

This project was created strictly for educational and cybersecurity laboratory purposes.

The confidential directory and decoy file were simulated.

No real credentials or confidential organizational information were intentionally used.

The testing was performed in a controlled Windows environment.

No production systems were intentionally targeted.

---

# Author

## Katakam Likith Kumar

Cybersecurity / Information Security Graduate

Areas of Interest:

* Security Operations Center (SOC)
* Detection and Monitoring
* Incident Response
* Governance, Risk and Compliance
* Vulnerability Assessment
* Information Security

---

If you found this project useful, feel free to explore the repository and review the implementation and evidence.

```
```
