number = int(input("Enter a number: "))

original_number = number

number = abs(number)

# Number of digits
if number == 0:
    digit_count = 1
else:
    digit_count = 0
    temp = number

    while temp > 0:
        digit_count += 1
        temp //= 10

digit_sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

digit_product = 1

if number == 0:
    digit_product = 0

else:
    temp = number

    while temp > 0:
        digit = temp % 10
        digit_product *= digit
        temp //= 10

reverse = 0
temp = number

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

# Even / Odd
if number % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"

# Prime check
if number < 2:
    prime_status = "Not Prime"

else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_status = "Prime"
    else:
        prime_status = "Not Prime"

# Palindrome check
if number == reverse:
    palindrome_status = "Palindrome"
else:
    palindrome_status = "Not Palindrome"

# Armstrong check
if number == 0:
    armstrong_sum = 0

else:
    armstrong_sum = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** digit_count
        temp //= 10

if armstrong_sum == number:
    armstrong_status = "Armstrong"
else:
    armstrong_status = "Not Armstrong"


print("\n===== NUMBER ANALYZER =====")
print("Number          :", original_number)
print("Number of digits:", digit_count)
print("Sum of digits   :", digit_sum)
print("Product of digits:", digit_product)
print("Reverse         :", reverse)
print("Even/Odd         :", even_odd)
print("Prime            :", prime_status)
print("Palindrome       :", palindrome_status)
print("Armstrong        :", armstrong_status)