fahrenheit = float(input("Enter the temperature in farenheit(°F): "))

celcius = (fahrenheit - 32) * 5/9
kelvin = celcius + 273.15

print (f"{fahrenheit:.1f} °F is equal to {celcius:.2f} °C and {kelvin:.2f} K")