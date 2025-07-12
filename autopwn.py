# autopwn.py

import argparse
from modules import recon, scan, enum, exploit

def main():
    parser = argparse.ArgumentParser(description="🎯 AutoPwn Framework — Beginner Pentest Automation Tool")
    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
    args = parser.parse_args()

    target = args.target

    print(f"\n[+] Starting AutoPwn against: {target}\n")

    recon.recon(target)
    scan.scan(target)
    enum.enum(target)
    exploit.exploit(target)

    print("\n[✓] AutoPwn complete!")

if __name__ == "__main__":
    main()
