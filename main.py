#!/usr/bin/env python3
"""
Automated generation script for the houseplant out-of-office notification entry.
Configures output directories and exports the botanical status message.
"""
import os

LINE = "I am currently out of water, out of patience, and recycling your tears into fresh soil nutrients."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
