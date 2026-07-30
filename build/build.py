#!/usr/bin/env python3
"""Rebuild both Hibbing proposals. Run from the build/ directory: python3 build.py"""
import subprocess, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("../output", exist_ok=True)
for script in ("realweb.py", "reallogo.py"):
    print(f"→ {script}")
    subprocess.run([sys.executable, script], check=True)
print("Done. See ../output/")
