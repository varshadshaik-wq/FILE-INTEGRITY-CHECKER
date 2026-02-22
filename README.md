# FILE-INTEGRITY-CHECKER
"COMPANY": CODTECH IT SOLUTIONS
*NAME*: SHAIK VARSHAD
"INTERN ID*:CTIS2404
"DOMAIN*: CYBER SECURITY & ETHICAL HACKING
"DURATION*: 8 WEEEKS
"MENTOR*: NEELA SANTOSH
# 🔐 File Integrity Checker Using Python

## 📌 Introduction
File integrity is a critical aspect of computer security and system reliability. It ensures that files remain unchanged unless modified by authorized users or processes. Unauthorized file changes may indicate security breaches, malware infections, or system misconfigurations. To address this issue, this project implements a File Integrity Checker using Python.

The File Integrity Checker monitors a specified directory and detects any changes in files by calculating and comparing cryptographic hash values. By verifying file integrity, this tool helps in identifying unauthorized modifications, newly added files, or deleted files within a directory.

This project is developed as part of an internship task and demonstrates fundamental concepts of cybersecurity, file handling, and hashing techniques using Python.

---

## 🎯 Project Objective
The main objective of this project is to design and implement a Python-based tool that ensures file integrity by:
- Calculating hash values for files
- Storing baseline hash values
- Detecting file modifications, additions, and deletions
- Providing clear output to the user regarding file integrity status

---

## 🛠 Technologies and Tools Used
- **Python 3** – Core programming language
- **hashlib** – Used to generate cryptographic hash values (SHA-256)
- **os** – Used for directory traversal and file handling
- **json** – Used to store and retrieve hash values persistently

---

## 🧠 Project Concept and Working Principle
The File Integrity Checker works on the principle of cryptographic hashing. A hash function generates a fixed-length unique value for a file based on its contents. Even a small change in the file will produce a completely different hash value.

### Working Flow:
1. The user runs the Python script and provides a directory path to monitor.
2. The program scans all files in the specified directory.
3. For each file, a SHA-256 hash value is calculated.
4. During the first execution, these hash values are stored in a JSON file as baseline data.
5. On subsequent executions, the program recalculates hash values.
6. The new hash values are compared with the previously stored hash values.
7. Based on comparison results, the program identifies:
   - Modified files (hash values changed)
   - New files (file not present in baseline)
   - Deleted files (file missing from current scan)
8. The results are displayed to the user in the terminal.

---

## ⚙️ How to Run the Project
1. Ensure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open Command Prompt or PowerShell in the project directory.
4. Run the following command:
   ```bash
   python file_integrity_checker.py
## Output
![Image](https://github.com/user-attachments/assets/f6210c0e-342f-4a7b-a367-7904e93c6bc9)
