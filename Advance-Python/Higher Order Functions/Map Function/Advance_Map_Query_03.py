# Problem 3: Converting Temperatures
# You are building a weather app that needs to convert temperatures from Celsius to Fahrenheit.

# Task: Use map() to convert a list of temperatures in Celsius to Fahrenheit.

celsius_temperatures = [0, 20, 30, 100, -5]
# F = C * 9/5 + 32

transform_in_fahrenheit = [print(fahrenheit) for fahrenheit in map(lambda C: (C * (9/5)) + 32,celsius_temperatures)]