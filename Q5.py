number_of_products = int(
    input("Enter number of products: ")
)

if number_of_products <= 0:
    print("Number of products must be positive.")

else:
    subtotal = 0

    for product_number in range(1, number_of_products + 1):
        price = float(input(f"Enter price of product {product_number}: "))

        if price < 0:
            print("Price cannot be negative.")
            exit()

        subtotal += price

    if subtotal >= 10000:
        discount_percentage = 15

    elif subtotal >= 5000:
        discount_percentage = 10

    elif subtotal >= 1000:
        discount_percentage = 5

    else:
        discount_percentage = 0

    discount = subtotal * discount_percentage / 100
    amount_after_discount = subtotal - discount

    tax = amount_after_discount * 0.18

    final_amount = amount_after_discount + tax

    print("Subtotal:", subtotal)
    print("Discount Percentage  :", discount_percentage, "%")
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final Amount:", final_amount)