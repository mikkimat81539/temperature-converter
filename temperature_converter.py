"""Build a program that converts temperatures between Celsius and Fahrenheit.
Create separate functions for each conversion."""

# fahrenheit formula: (#°C × 9/5) + 32 = #°F
# celsius formula: (#°F − 32) × 5/9 = #°C

def fahrenheit():
    formula = (num_f * 9/5) + 32
    return formula

def celsius():
    formula = (num_c - 32) * 5/9
    return formula

conversion = input("What are you converting to Celsius or Fahrenheit? ").lower()

if conversion == "celsius":
    num_c = int(input("Input a number: "))
    print(f"{round(celsius(), 2)}°C")

elif conversion == "fahrenheit":
    num_f = int(input("Input a number: "))
    print(f"{round(fahrenheit(), 2)}°F")

else:
    print("Not a valid input.")
