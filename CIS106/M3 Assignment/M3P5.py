# Program to find the area and perimeter of a circle

# Input section
radius = float(input("Enter the radius of the circle: "))

# Processing section
PI = 3.14
area = PI * (radius * radius)
perimeter = 2 * PI * radius

# Output section
print(f"\n--- Circle Measurements ---")
print(f"Radius: {radius}")
print(f"Area: {area:.2f} square units")
print(f"Perimeter: {perimeter:.2f} units")
