import sys


    script_name = sys.argv[0]
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    weight = 60.0   
    height = 1.65   
    print("No input given — using default values:")


bmi = weight / (height * height)


print("Script Name:", script_name)
print("Weight (kg):", weight)
print("Height (m):", height)
print("BMI Value:", bmi)
