class Temperature_Converter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature: {celsius}°C is equal to {fahrenheit}°F") # Output: 25°C is equal to 77.0°F
