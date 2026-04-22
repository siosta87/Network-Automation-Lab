import os

# Open the list of devices
with open("devices.txt", "r") as file:
    devices = file.readlines()

for ip in devices:
    ip = ip.strip()  # Remove extra spaces and newlines
    
    # If the line is empty, skip it
    if not ip:
        continue
        
    print(f"Checking: {ip}...")
    
    # Sends 1 ping packet; "> nul" hides the command output on Windows
    # Note: Use "> /dev/null" instead of "> nul" if you are on Linux/macOS
    response = os.system(f"ping -n 1 {ip} > nul")

    if response == 0:
        print(f"Device {ip} is UP")
    else:
        print(f"Device {ip} is DOWN")