# Prompt user for temperature and unit
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Convert temperature based on unit
if unit.upper() == 'C':
    converted_temp = (temperature * 9/5) + 32
    new_unit = 'Fahrenheit'
    print(f"The temperature in Fahrenheit is: {converted_temp} {new_unit}")
elif unit.upper() == 'F':
    converted_temp = (temperature - 32) * 5/9
    new_unit = 'Celsius'
    print(f"The temperature in Celsius is: {converted_temp} {new_unit}")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
