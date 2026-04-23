import socket
from datetime import datetime

# 1. Define targets and PORTS (must be a list of integers)
targets = ["8.8.8.8", "1.1.1.1", "google.com"]
ports_to_check = [80, 443, 53]  # Added common ports to check

# Use strftime for a cleaner looking timestamp
print(f"--- Network Audit Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

for target in targets:
    print(f"Checking {target}...")
    
    # Try to resolve hostname to IP (needed for reliability)
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"  [!] Error: Could not resolve {target}")
        continue

    for port in ports_to_check:
        # Create a socket connection attempt
        # AF_INET = IPv4, SOCK_STREAM = TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Don't wait more than 1 second
        
        # connect_ex returns 0 if successful, or an error code if not
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"   [+] Port {port}: OPEN")
        else:
            # Result codes other than 0 usually mean closed or timed out
            print(f"   [-] Port {port}: CLOSED/FILTERED")
        
        sock.close()
    print("-" * 30)

print(f"\n--- Audit Complete: {datetime.now().strftime('%H:%M:%S')} ---")
