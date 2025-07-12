# modules/enum.py

import subprocess

def enum(target):
    print("\n[3] Starting Web Enumeration...\n")

    print("[+] Nikto scan (basic web vulns):")
    subprocess.run(["nikto", "-h", target])

    print("\n[+] Gobuster (directory bruteforce):")
    subprocess.run([
        "gobuster", "dir",
        "-u", f"http://{target}",
        "-w", "/usr/share/wordlists/dirb/common.txt",
        "-q", "-t", "20"
    ])
