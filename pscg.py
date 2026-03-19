# PSCG(Password Security Checker & Generator)
import secrets, string, time

# check password strength
def check_pass_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak Password!"
    elif score == 3:
        return "Medium Password!"
    elif score == 4:
        return "Good Password!"
    else:
        return "Strong Password! :)"

#  Generate strong password   
def generate_strong_pass(length=15):
    while True:
      strong_password = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    
      # guaranteed logic
      if (any(c.islower() for c in strong_password) and
          any(c.isupper() for c in strong_password) and
          any(c.isdigit() for c in strong_password) and
          any(c in string.punctuation for c in strong_password)):
          return strong_password

# user input & O/P
def main(): 
    print("[~] Initializing PSCG Tool...")
    time.sleep(1)
    while True:
            print("\n╔══════════════════════════════════════╗")
            print("║         PSCG v1.0 TERMINAL           ║")
            print("║     Password Security Utility        ║")
            print("║        Author: PRiTi.EX              ║")
            print("╚══════════════════════════════════════╝")

            print("\n[+] Select an option:\n")
            print("    (1) Check Password Strength")
            print("    (2) Generate Strong Password")
            print("    (3) Exit")

            print("\n────────────────────────────────────────")

            choice =input("Enter Your Choice: ").strip()

            if choice == "1":
                password = input("\n[?] Enter Your Password: ")
                print("\n[~] Analyzing password strength...")
                time.sleep(1)
                print("\n[+] Your Password Strength: ", check_pass_strength(password))
            elif choice == "2":
                print("\n[~] Generating secure password...")
                time.sleep(1)
                print("\n[✔] Generated Strong Password: ", generate_strong_pass())
            elif choice == "3":
                print("Exiting PSCG Tool.....")
                time.sleep(0.5)
                print("[✔] Stay Secure :)")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    main()

     





