# modules/scan.py

import subprocess

def scan(target):
    print("\n[2] Scanning for open ports with Nmap...\n")

    # Quick scan first
    subprocess.run(["nmap", "-T4", "-Pn", "-F", target])

    # Full port scan (comment out if you want faster testing)
    # subprocess.run(["nmap", "-sS", "-p-", "-T4", "-Pn", target])
