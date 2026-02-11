# Password Strength Checker

A Python-based desktop application that evaluates password strength, generates secure passwords,
and provides real-time visual feedback through a modern GUI.

This project demonstrates secure design principles, modular architecture, and user-focused UX.

---

## Features

- Password strength evaluation with actionable feedback
- Visual strength meter (Weak / Moderate / Strong)
- Password evaluation heatmap (length, case, digits, symbols)
- Secure password generator with customization
- Clipboard integration
- Dark / Light mode toggle
- Have I Been Pwned (HIBP) breach detection (k-anonymity)
- Modular architecture (GUI + logic separation)

---

## Project Structure

PasswordStrengthChecker/
├── gui_app.py # GUI entry point

├── password_utils.py # Core password logic

├── requirements.txt # Dependencies

├── README.md

└── .gitignore


---

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/PasswordStrengthChecker.git
cd PasswordStrengthChecker
