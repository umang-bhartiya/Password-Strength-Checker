# Password Strength Checker 🔐

A Python-based desktop application that evaluates password strength, generates secure passwords,
and provides real-time visual feedback through a modern GUI.

This project demonstrates secure design principles, modular architecture, and user-focused UX.

---

## 🚀 Features

- Password strength evaluation with actionable feedback
- Visual strength meter (Weak / Moderate / Strong)
- Password evaluation heatmap (length, case, digits, symbols)
- Secure password generator with customization
- Clipboard integration
- Dark / Light mode toggle
- Have I Been Pwned (HIBP) breach detection using k-anonymity
- Modular architecture (GUI + logic separation)

---

## 🧩 Problem Statement & Solution

### 🔍 Real-Life Problem Statement

In today’s digital ecosystem, users are required to create and manage passwords across multiple platforms such as email, banking, social media, academic portals, and enterprise systems.  

Despite increasing awareness of cybersecurity risks, a significant number of users continue to rely on weak, predictable, or reused passwords due to:  

- Lack of real-time feedback during password creation  
- Limited understanding of what constitutes a “strong” password  
- Absence of user-friendly tools that explain password weaknesses clearly  
- Unawareness of whether their passwords have appeared in known data breaches  
- This behavior significantly increases the risk of account compromise, identity theft, and unauthorized access, impacting both individuals and organizations.  

---

### 💡 How This Project Provides a Solution

The Password Strength Checker addresses this problem by offering an interactive, educational, and security-focused desktop application that assists users in creating and evaluating strong passwords.

Solution Capabilities:  

* Real-time password strength evaluation  
  Users receive immediate feedback while typing, allowing them to iteratively improve password quality.  
* Visual strength indicators  
  A progress bar and heatmap clearly highlight which security criteria are satisfied or missing (length, uppercase, lowercase, digits, symbols).  
* Actionable recommendations  
  Instead of generic warnings, the application provides specific suggestions to strengthen weak passwords.  
* Secure password generation  
  Users can generate strong, randomized passwords based on customizable criteria, reducing reliance on guessable patterns.  
* Breach exposure awareness  
  Integration with the Have I Been Pwned API enables users to check whether a password has appeared in known data breaches, improving risk awareness.  
* Privacy-conscious design  
  Breach checks use k-anonymity, ensuring passwords are never transmitted or stored externally in plaintext.  

---

### 👥 How Users and the Public Should Address This Problem

Users should treat password security as a preventive practice, not a reactive one. This project encourages that mindset by:  

- Educating users on password hygiene at the moment of password creation  
- Helping users understand why a password is weak, not just that it is weak  
- Promoting unique, high-entropy passwords for different platforms  
- Raising awareness of real-world data breaches and their implications  

For students and developers, the project also serves as a practical demonstration of secure software design, reinforcing best practices in both cybersecurity and application development.  

---

## 🧱 Project Structure

PasswordStrengthChecker/  
│  
├── gui_app.py             # GUI entry point  
├── password_utils.py      # Core password logic  
├── requirements.txt       # Project dependencies  
├── README.md              # Project documentation  
└── .gitignore             # Git ignore rules  

---

## 🛠️ Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/PasswordStrengthChecker.git
cd PasswordStrengthChecker
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run The Application

```bash
python gui_app.py
```

---

## 🔮 Future Enhancements
```bash  
├── SQLite encrypted password vault  
├── First-run master password setup  
├── Executable packaging (.exe)  
└── Cross-platform UI polish
```

---
