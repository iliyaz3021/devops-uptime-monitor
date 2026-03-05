import requests
import datetime
import os

# List of websites to monitor (Your client's sites)
SITES = ["https://google.com", "https://github.com"]

def check_uptime():
    print(f"--- Monitoring Scan: {datetime.datetime.now()} ---")
    results = []
    
    for url in SITES:
        try:
            response = requests.get(url, timeout=10)
            status = "UP" if response.status_code == 200 else f"DOWN ({response.status_code})"
        except Exception as e:
            status = f"ERROR ({str(e)})"
        
        log_entry = f"{datetime.datetime.now()} | {url} | {status}"
        print(log_entry)
        results.append(log_entry)

    # Save to a log file
    with open("uptime_log.txt", "a") as f:
        for line in results:
            f.write(line + "\n")

if __name__ == "__main__":
    check_uptime()