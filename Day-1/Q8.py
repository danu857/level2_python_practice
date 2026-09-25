# Number Analyzer

while True:

    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Check Palindrome")
    print("4. Check Armstrong")
    print("5. Reverse Number")
    print("6. Sum of Digits")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            number = int(input("Enter a number: "))

            if number % 2 == 0:
                print(number, "is Even")
            else:
                print(number, "is Odd")

        case 2:
            number = int(input("Enter a number: "))

            if number <= 1:
                print(number, "is Not Prime")
            else:
                i = 2
                is_prime = True

                while i < number:
                    if number % i == 0:
                        is_prime = False
                        break
                    i += 1

                if is_prime:
                    print(number, "is Prime")
                else:
                    print(number, "is Not Prime")

        case 3:
            number = int(input("Enter a number: "))

            original = number
            reverse = 0

            while number > 0:
                digit = number % 10
                reverse = reverse * 10 + digit
                number //= 10

            if original == reverse:
                print(original, "is a Palindrome")
            else:
                print(original, "is Not a Palindrome")

        case 4:
            number = int(input("Enter a number: "))

            original = number
            count = len(str(number))

            total = 0

            while number > 0:
                digit = number % 10
                total = total + digit ** count
                number //= 10

            if original == total:
                print(original, "is an Armstrong Number")
            else:
                print(original, "is Not an Armstrong Number")

        case 5:
            number = int(input("Enter a number: "))

            reverse = 0

            while number > 0:
                digit = number % 10
                reverse = reverse * 10 + digit
                number //= 10

            print("Reversed Number =", reverse)

        case 6:
            number = int(input("Enter a number: "))

            total = 0

            while number > 0:
                digit = number % 10
                total += digit
                number //= 10

            print("Sum of Digits =", total)

        case 7:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")