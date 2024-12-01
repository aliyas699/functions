temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (Celsius or Fahrenheit): ").lower()

converted_temperature = convert_temperature(temperature, unit)
if isinstance(converted_temperature, str):
    print(converted_temperature)
else:
    print(f"The converted temperature is: {converted_temperature:.2f}")