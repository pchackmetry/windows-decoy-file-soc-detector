import os
import time
from datetime import datetime

DECOY_FILE = r"C:\Finance\Confidential\Decoy_File.txt"
LOG_FILE = r".\detector_alerts.log"


def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    alert = f"[{timestamp}] ALERT: {message}"

    print(alert)

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(alert + "\n")


def create_decoy():
    folder = os.path.dirname(DECOY_FILE)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(DECOY_FILE):
        with open(DECOY_FILE, "w", encoding="utf-8") as file:
            file.write(
                "CONFIDENTIAL FINANCIAL DATA - DECOY FILE\n"
                "This file is monitored by the SOC detector.\n"
            )

        print(f"[+] Decoy file created: {DECOY_FILE}")
    else:
        print(f"[+] Decoy file already exists: {DECOY_FILE}")


def monitor_decoy():
    print("\n========================================")
    print(" Windows Decoy File SOC Detector")
    print("========================================")
    print(f"Monitoring: {DECOY_FILE}")
    print("Press CTRL+C to stop.\n")

    last_modified = os.path.getmtime(DECOY_FILE)

    while True:
        time.sleep(2)

        if not os.path.exists(DECOY_FILE):
            log_alert("CRITICAL - Decoy file was deleted!")
            break

        current_modified = os.path.getmtime(DECOY_FILE)

        if current_modified != last_modified:
            log_alert(
                "Decoy file was modified. "
                f"Path: {DECOY_FILE}"
            )

            last_modified = current_modified


if __name__ == "__main__":
    create_decoy()
    monitor_decoy()