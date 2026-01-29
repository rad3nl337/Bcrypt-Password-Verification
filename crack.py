# ==========================================
# bcrypt password checker
# by : RADEN
# ==========================================

import bcrypt

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def load_wordlist(filename):
    """Load password candidates from wordlist file"""
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]

def load_target_hash(filename):
    """Load bcrypt hash from target file"""
    with open(filename, "rb") as f:
        return f.read().strip()

# ==============================
# MAIN PROGRAM
# ==============================

# ASCII Art Watermark - RADEN
print(f"""{CYAN}
██████╗  █████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║
██████╔╝███████║██║  ██║█████╗  ██╔██╗ ██║
██╔══██╗██╔══██║██║  ██║██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║██████╔╝███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝
        bcrypt checker | RADEN
{RESET}""")

try:
    target_hash = load_target_hash("target.txt")
    wordlist = load_wordlist("wordlist.txt")
except FileNotFoundError as e:
    print(f"{RED}[ERROR] File not found: {e}{RESET}")
    exit(1)

print(f"Total passwords in wordlist: {len(wordlist)}\n")

for word in wordlist:
    print(f"{RED}Trying password: {word}{RESET}")
    if bcrypt.checkpw(word.encode("utf-8"), target_hash):
        print(f"\n{GREEN}[SUCCESS] Password found: {word}{RESET}")
        break
else:
    print(f"\n{RED}[FAILED] Password not found in wordlist{RESET}")

# EOF
# Author: RADEN
