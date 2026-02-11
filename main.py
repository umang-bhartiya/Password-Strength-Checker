from password_utils import check_strength, generate_password
import pyperclip

def main():
    print("🔐 Password Utility Tool")
    print("-------------------------")

    while True:
        print("\nSelect an option:")
        print("1. Check password strength")
        print("2. Generate strong password")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1':
            password = input("\nEnter your password: ")
            strength, feedback = check_strength(password)
            print(f"\n🟩 Password Strength: {strength}")
            if feedback:
                print("\n💡 Suggestions:")
                for suggestion in feedback:
                    print(f" - {suggestion}")

        elif choice == '2':
            try:
                length = int(input("Desired length (min 8): "))
                use_upper = input("Include UPPERCASE? (y/n): ").strip().lower() == 'y'
                use_lower = input("Include lowercase? (y/n): ").strip().lower() == 'y'
                use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
                use_special = input("Include special chars (!@#$)? (y/n): ").strip().lower() == 'y'

                password = generate_password(length, use_upper, use_lower, use_digits, use_special)

                print(f"\n🔑 Generated Password: {password}")

                # ✅ Optional clipboard
                to_clip = input("📋 Copy to clipboard? (y/n): ").strip().lower()
                if to_clip == 'y':
                    pyperclip.copy(password)
                    print("✅ Copied to clipboard.")

                # ✅ Optional file save
                to_file = input("💾 Save to file? (y/n): ").strip().lower()
                if to_file == 'y':
                    filename = input("Enter filename (e.g., my_password.txt): ").strip()
                    with open(filename, 'w') as f:
                        f.write(f"Generated Password:\n{password}\n")
                    print(f"✅ Saved to file: {filename}")

            except ValueError:
                print("⚠️ Please enter a valid number for length.")

        elif choice == '3':
            print("👋 Exiting. Stay safe with strong passwords!")
            break

        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
