CORRECT_PIN = "1130"

pin = input("Enter your 4-digit PIN: ")

if pin != CORRECT_PIN:
    print("\nIncorrect PIN. Access denied.")
else:
    print("\nPIN accepted.")
    print("\nChoose an account:")
    print("1. Checking")
    print("2. Savings")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        print("\nWelcome to your Checking account!")
    elif choice == "2":
        print("\nWelcome to your Savings account!")
    else:
        print("\nInvalid selection.")
