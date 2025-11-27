import sys

# Expecting: script_name weight height
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    weight = 60.0   # default weight in kg
    height = 1.65   # default height in meters
    print("No input given — using default values:")

# Calculate BMI
bmi = weight / (height * height)

# Output
print("Script Name:", script_name)
print("Weight (kg):", weight)
print("Height (m):", height)
print("BMI Value:", bmi)
