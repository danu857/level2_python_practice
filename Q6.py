correct_username = "admin"
correct_password = "admin123"

for attempt in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful.")
        break

    else:
        remaining_attempts = 2 - attempt

        if remaining_attempts > 0:
            print("Invalid username or password.")
            print("Remaining attempts :", remaining_attempts)

        else:
            print("Invalid username or password.")
else:
    print("Account locked.")