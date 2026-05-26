#Write a function celsius_to_fahrenheit(c) that converts Celsius to Fahrenheit: F = C * 9/5 + 32
#Test it with 0°C, 100°C, and 37°C

def ctof(c):
    f = (c * 9/5) + 32
    return f

c = float(input("Enter the Temperature in C:"))

f = ctof(c)

print(f"{c}C = {f}F")