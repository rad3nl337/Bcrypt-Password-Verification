# ==========================================
# bcrypt password checker (streaming)
# Author : RADEN
# ==========================================

import bcrypt
import time

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ==============================
# LOAD TARGET HASH
# ==============================
def load_target_hash(filename):
    with open(filename, "rb") as f:
        return f.read().strip()

# ==============================
# WORDLIST STREAM (NO RAM LOAD)
# ==============================
def wordlist_stream(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pw = line.strip()
            if pw:
                yield pw

# ==============================
# MAIN
# ==============================
print(f"""{CYAN}
██████╗  █████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║
██████╔╝███████║██║  ██║█████╗  ██╔██╗ ██║
██╔══██╗██╔══██║██║  ██║██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║██████╔╝███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝
        bcrypt checker | STREAM MODE
{RESET}""")

try:
    target_hash = load_target_hash("target.txt")
except FileNotFoundError:
    print(f"{RED}[ERROR] target.txt not found{RESET}")
    exit(1)

start = time.time()
checked = 0
REPORT_EVERY = 10_000   

for password in wordlist_stream("wordlist.txt"):
    checked += 1

    if bcrypt.checkpw(password.encode("utf-8"), target_hash):
        elapsed = time.time() - start
        print(f"\n{GREEN}[SUCCESS] Password found: {password}{RESET}")
        print(f"Checked   : {checked}")
        print(f"Time spent: {elapsed:.2f} seconds")
        break

    if checked % REPORT_EVERY == 0:
        elapsed = time.time() - start
        speed = checked / elapsed if elapsed > 0 else 0
        print(f"[INFO] Checked: {checked:,} | {speed:.2f} pwd/sec")

else:
    elapsed = time.time() - start
    print(f"\n{RED}[FAILED] Password not found{RESET}")
    print(f"Checked   : {checked}")
    print(f"Time spent: {elapsed:.2f} seconds")
