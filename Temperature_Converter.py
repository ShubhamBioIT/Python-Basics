# 📦 Temperature Converter Tool
# Converts between Celsius, Fahrenheit, and Kelvin

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k * 9/5) - 459.67

# Sample Test
if __name__ == "__main__":
    print("🌡 Celsius to Fahrenheit:", celsius_to_fahrenheit(25))
    print("🌡 Fahrenheit to Kelvin:", fahrenheit_to_kelvin(98.6))
    print("🌡 Kelvin to Celsius:", kelvin_to_celsius(300))
