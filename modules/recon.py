# modules/recon.py

import subprocess

def recon(target):
    print("[1] Running Reconnaissance...\n")

    print(f"[+] WHOIS for {target}")
    subprocess.run(["whois", target])

    print(f"\n[+] nslookup for {target}")
    subprocess.run(["nslookup", target])
