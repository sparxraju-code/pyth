import psutil
import time

def monitor_cpu(threshold=80):
    print("Monitoring CPU usage...")       
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
           
            if cpu_usage > threshold:
                print(f"CPU usage exceeded Threshold of {threshold}%, current usage: {cpu_usage}%")
            else:
                print(f"Current CPU Usage: {cpu_usage}%")            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring interrupted by user.")

monitor_cpu()