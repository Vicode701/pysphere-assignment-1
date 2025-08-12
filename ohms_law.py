# Profile: github.com/Vicode701
# ohms_law.py
# This program calculates voltage using Ohm's Law: V = I * R

# Ask the user for current (I) in amperes
current = float(input("Enter the current (in A): "))

# Ask the user for resistance (R) in ohms
resistance = float(input("Enter the resistance (in ohms): "))

# Calculate voltage using the formula V = I * R
voltage = current * resistance

# Display the result
print(f"The voltage is: {voltage} volts")
