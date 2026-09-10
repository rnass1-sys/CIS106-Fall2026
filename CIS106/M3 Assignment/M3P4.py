# Program to calculate car discounts and final prices

# Input section
make = input("Enter the vehicle make: ")
model = input("Enter the vehicle model: ")
msrp = float(input("Enter the MSRP amount: $"))
discount_percent = float(input("Enter the discount percent (as a decimal, e.g., 0.15 for 15%): "))

# Processing section
amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

# Output section
print(f"\n--- Vehicle Price Details ---")
print(f"Vehicle: {make} {model}")
print(f"Original MSRP: ${msrp:.2f}")
print(f"Discount Percent: {discount_percent * 100:.1f}%")
print(f"Amount Off MSRP: ${amount_off:.2f}")
print(f"Discounted Price: ${discounted_price:.2f}")
