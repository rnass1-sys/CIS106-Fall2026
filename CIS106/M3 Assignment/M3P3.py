# Program to split a job payment evenly among three friends

# Input section
total_amount = float(input("Enter the total amount received for the job: $"))

# Processing section
individual_share = total_amount / 3

# Output section
print(f"\nEach person will receive: ${individual_share:.2f}")
