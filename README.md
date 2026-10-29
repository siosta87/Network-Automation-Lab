# Network Automation Lab

Two beginner Python scripts for connectivity checks and TCP port checks.

## Included files

| File | Purpose |
| --- | --- |
| [scanner.py](scanner.py) | Reads devices.txt and sends one ping per nonblank target |
| [devices.txt](devices.txt) | Input target list for the ping scanner |
| [network_auditor.py](network_auditor.py) | Resolves configured targets and attempts TCP connections |

## Requirements

- Python 3
- Windows for the ping scanner as currently written
- No third-party Python packages; both scripts use the standard library

## Run

1. Open a terminal in the repository folder.
2. Edit devices.txt with one authorized lab target per line.
3. Run the ping scanner:

```console
python scanner.py
```

4. Review targets and ports_to_check in network_auditor.py, then run:

```console
python network_auditor.py
```

## What the results mean

The scanner prints UP or DOWN according to the ping command exit status. A failed ping can also mean ICMP is blocked.

The TCP checker currently tests ports **80, 443, and 53**, with a one-second socket timeout. OPEN means a TCP connection succeeded. CLOSED/FILTERED groups several unsuccessful connection outcomes; it does not distinguish the exact cause or prove a vulnerability.

## Current limitations

- scanner.py uses Windows ping syntax (-n 1). A Linux/macOS port needs -c 1 as well as the appropriate output handling.
- scanner.py passes target text to a shell command. Keep devices.txt limited to trusted addresses or hostnames. Input validation and subprocess argument handling are future improvements.
- The TCP checker uses IPv4 and hard-coded targets and ports.
- Results are printed to the console; no saved reports or automated tests are included.
- This cleanup reviewed source code and documentation, not live network results.

## Skills practiced

File input, loops, conditionals, socket connections, DNS resolution, timeouts, and readable console output.
