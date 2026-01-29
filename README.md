
# 🔐 Bcrypt Password Verification (Dictionary-Based)

This project demonstrates how **bcrypt password hashes** can be verified using a dictionary-based approach in **Python**. The program does **not decrypt** hashes, but verifies candidate passwords against a given bcrypt hash.
> ⚠️ This project is intended for **educational purposes only**.

--- 

## 📌 Features 
- Bcrypt password verification 
- Dictionary-based password checking 
- Colorized terminal output 
- ❌ Red → unsuccessful attempts 
- ✅ Green → successful match - Simple and beginner-friendly Python code

---

## 📄 File Description 
- crack.py Main Python script for verifying bcrypt hashes 
- target.txt Contains the bcrypt hash 
- wordlist.txt List of password candidates 
- requirements.txt Python dependencies

--- 

## 🧠 How It Works 
- The program reads a bcrypt hash from target.txt 
- Password candidates are loaded from wordlist.txt 
- Each password is verified using bcrypt.checkpw() 
- If a match is found, the password is displayed 
- No decryption is performed (bcrypt is one-way)

## 📥 Clone the Repository
```bash
git clone https://github.com/USERNAME/bcrypt-password-verification.git
cd bcrypt-password-verification
```

## ⚙️ Requirements
- Python **3.8 or higher** 
- pip

## 📦 Installation 
✅ Recommended Method (Virtual Environment) This method avoids conflicts with system Python (PEP 668 compliant).
```bash
- Create virtual environment 
python3 -m venv venv  

- Activate virtual environment 
source venv/bin/activate 
 
- Install dependencies 
pip install -r requirements.txt
```
## 🐧 Kali Linux (Alternative)
If you are using Kali Linux and prefer system packages: 
```bash
sudo apt update
sudo apt install python3-bcrypt
```
## ▶️ Usage
python crack.py

## 📚 Academic Notes
- Bcrypt uses salt and cost factor 
- Hashes cannot be decrypted 
- Verification is the only valid approach 
- Bcrypt is significantly more secure than MD5 or SHA-1

## ⚠️ Disclaimer
This project is for educational and research purposes only. Do not use this tool for unauthorized access or illegal activities.
