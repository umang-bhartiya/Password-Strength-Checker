import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from password_utils import check_strength, generate_password
import pyperclip
import hashlib
import requests

PWNED_URL = "https://api.pwnedpasswords.com/range/{}"
MASTER_PASSWORD = "admin123"  # Change this to your preferred master password


class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Tool")
        self.root.geometry("550x660")
        self.root.resizable(False, False)

        self.is_dark_mode = False
        self.show_password = False

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Green.Horizontal.TProgressbar", background='green')
        style.configure("Orange.Horizontal.TProgressbar", background='orange')
        style.configure("Red.Horizontal.TProgressbar", background='red')

        # Live password variable
        self.pw_var = tk.StringVar()
        self.pw_var.trace_add('write', self.on_password_change)

        self.setup_ui()
        self.apply_light_theme()

    def setup_ui(self):
        tk.Label(self.root, text="Password Utility Tool", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.input_entry = tk.Entry(self.root, width=40, font=("Courier", 12), show="*", textvariable=self.pw_var)
        self.input_entry.pack(pady=5)

        self.show_btn = tk.Checkbutton(self.root, text="👁 Show Password", command=self.toggle_show_password)
        self.show_btn.pack()

        tk.Button(self.root, text="Check Strength Now", command=self.check_strength_ui).pack(pady=5)

        # Strength Bar
        self.strength_var = tk.IntVar()
        self.strength_bar = ttk.Progressbar(self.root, length=400, variable=self.strength_var, maximum=100)
        self.strength_bar.pack(pady=5)
        self.strength_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.strength_label.pack()

        # Heatmap Indicators
        self.heatmap_frame = tk.Frame(self.root)
        self.heatmap_frame.pack(pady=5)
        self.heat_labels = {
            "length": tk.Label(self.heatmap_frame, text="❌ Length"),
            "upper": tk.Label(self.heatmap_frame, text="❌ Uppercase"),
            "lower": tk.Label(self.heatmap_frame, text="❌ Lowercase"),
            "digit": tk.Label(self.heatmap_frame, text="❌ Digit"),
            "symbol": tk.Label(self.heatmap_frame, text="❌ Symbol")
        }
        for i, label in enumerate(self.heat_labels.values()):
            label.grid(row=0, column=i, padx=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength=480, justify="left")
        self.result_label.pack(pady=10)

        # Generator options
        options_frame = tk.LabelFrame(self.root, text="Generate Password Options", padx=10, pady=10)
        options_frame.pack(pady=10)

        self.length_var = tk.IntVar(value=12)
        tk.Label(options_frame, text="Length:").grid(row=0, column=0, sticky="w")
        tk.Scale(options_frame, from_=8, to=32, orient="horizontal", variable=self.length_var).grid(row=0, column=1, columnspan=3)

        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        tk.Checkbutton(options_frame, text="Uppercase", variable=self.upper_var).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Lowercase", variable=self.lower_var).grid(row=1, column=1, sticky="w")
        tk.Checkbutton(options_frame, text="Digits", variable=self.digit_var).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Special", variable=self.special_var).grid(row=2, column=1, sticky="w")

        action_frame = tk.Frame(self.root)
        action_frame.pack(pady=5)
        tk.Button(action_frame, text="Generate", command=self.generate_password_ui).grid(row=0, column=0, padx=5)
        tk.Button(action_frame, text="Copy", command=self.copy_to_clipboard).grid(row=0, column=1, padx=5)
        tk.Button(action_frame, text="Save", command=self.save_to_file).grid(row=0, column=2, padx=5)

        tk.Button(self.root, text="🌙 Toggle Dark Mode", command=self.toggle_theme).pack(pady=10)

    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.input_entry.config(show="" if self.show_password else "*")

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        if self.is_dark_mode:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()

    def apply_dark_theme(self):
        bg = "#2e2e2e"
        fg = "white"
        self.root.configure(bg=bg)
        for w in self.root.winfo_children():
            try:
                w.configure(bg=bg, fg=fg)
            except:
                pass
        for label in self.heat_labels.values():
            label.configure(bg=bg, fg=fg)

    def apply_light_theme(self):
        bg = "#f0f0f0"
        fg = "black"
        self.root.configure(bg=bg)
        for w in self.root.winfo_children():
            try:
                w.configure(bg=bg, fg=fg)
            except:
                pass
        for label in self.heat_labels.values():
            label.configure(bg=bg, fg=fg)

    def on_password_change(self, *args):
        self.check_strength_ui(check_breach=False)

    def check_strength_ui(self, check_breach=True):
        password = self.pw_var.get()
        strength, feedback = check_strength(password)
        self.update_heatmap(password)

        text = f"🟢 Strength: {strength}\n"
        if feedback:
            text += "\n💡 Suggestions:\n" + "\n".join(f"- {f}" for f in feedback)
        self.result_label.config(text=text)

        if strength == "Strong":
            self.strength_var.set(100)
            color = "Green"
        elif strength == "Moderate":
            self.strength_var.set(60)
            color = "Orange"
        else:
            self.strength_var.set(30)
            color = "Red"

        self.strength_bar.configure(style=f"{color}.Horizontal.TProgressbar")
        self.strength_label.config(text=strength, fg=color.lower())

        if check_breach and password:
            count = self.check_pwned(password)
            if count:
                messagebox.showwarning("⚠️ Breach Found", f"This password has appeared {count} time(s) in data breaches!")
            else:
                messagebox.showinfo("✅ Not Found", "This password was NOT found in any known breaches.")

    def update_heatmap(self, password):
        def update(label, passed):
            label.config(text=("✅" if passed else "❌") + " " + label.cget("text")[2:])

        update(self.heat_labels["length"], len(password) >= 8)
        update(self.heat_labels["upper"], any(c.isupper() for c in password))
        update(self.heat_labels["lower"], any(c.islower() for c in password))
        update(self.heat_labels["digit"], any(c.isdigit() for c in password))
        update(self.heat_labels["symbol"], any(not c.isalnum() for c in password))

    def generate_password_ui(self):
        password = generate_password(
            length=self.length_var.get(),
            use_upper=self.upper_var.get(),
            use_lower=self.lower_var.get(),
            use_digits=self.digit_var.get(),
            use_special=self.special_var.get()
        )
        self.pw_var.set(password)
        self.result_label.config(text="✅ Password generated!")

    def copy_to_clipboard(self):
        password = self.pw_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("⚠️ Warning", "Nothing to copy.")

    def save_to_file(self):
        password = self.pw_var.get()
        if not password:
            messagebox.showwarning("⚠️ Warning", "Nothing to save.")
            return
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            with open(file, "w") as f:
                f.write("Password:\n" + password + "\n")
            messagebox.showinfo("✅ Saved", f"Password saved to:\n{file}")

    def check_pwned(self, password):
        sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1[:5], sha1[5:]
        res = requests.get(PWNED_URL.format(prefix))
        if res.status_code != 200:
            return None
        for line in res.text.splitlines():
            h, count = line.split(':')
            if h == suffix:
                return int(count)
        return 0


def prompt_login():
    attempt = simpledialog.askstring("🔐 Login", "Enter master password:", show="*")
    if attempt != MASTER_PASSWORD:
        messagebox.showerror("Access Denied", "Incorrect password.")
        exit()


if __name__ == "__main__":
    root = tk.Tk()
    prompt_login()
    app = PasswordApp(root)
    root.mainloop()
