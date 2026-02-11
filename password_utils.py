import re
import nltk
import string
import random
import pyperclip
from nltk.corpus import words

# Load English word list
try:
    word_list = set(words.words())
except LookupError:
    nltk.download('words')
    word_list = set(words.words())


def check_strength(password):
    if not password:
        return "Invalid", ["Password cannot be empty."]

    feedback = []
    score = 0

    # Length scoring
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 characters).")

    # Character checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        score += 1
    else:
        feedback.append("Include special characters (e.g., !@#$%).")

    # Dictionary word check
    password_lower = password.lower()
    for word in word_list:
        if len(word) > 4 and word in password_lower:
            feedback.append("Password contains dictionary words. Avoid predictable patterns.")
            break

    # Strength classification
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if length < 4:
        return ""  # GUI will handle this with a warning

    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        return ""  # GUI will warn user if no types are selected

    # Guarantee at least one of each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill remaining with random from pool
    remaining = length - len(password)
    password += random.choices(char_pool, k=remaining)
    random.shuffle(password)

    result = ''.join(password)
    pyperclip.copy(result)  # Auto-copy to clipboard
    return result
