# Scenario: Astronomical Data Transformation
# Story: As a data scientist at the Space Exploration Institute,
# you're tasked with processing a list of dictionaries, each representing a celestial object with attributes like
# name, type, and distance_from_earth (in light-years). Your goal is to convert the distances from light-years to kilometers (1 light-year ≈ 9.461 trillion kilometers)
# and return a list of updated dictionaries.

# Challenge: Use the map() function to transform the list so that each dictionary includes the distance in both light-years and kilometers.

# Hint: Define a function that takes a dictionary, calculates the distance in kilometers,
# adds this information to the dictionary, and then use map() to apply this function to the list.

# Explanation of Fields:
# name: The name of the celestial object (e.g., star, galaxy, etc.).
# type: The type of celestial object (e.g., star, galaxy).
# distance_from_earth: Distance of the celestial object from Earth in light-years.

# Task Using This Dataset:
# Input: A list of dictionaries (celestial_objects).
# Output: Transform the dataset to include an additional key distance_in_km for each object, where:
# distance_in_km = distance_from_earth x 9.461 x 10^12

# Example Transformation:
# For Proxima Centauri:

# Distance from Earth: 4.24 light-years
# Converted Distance: 4.24×9.461×10^12

'''
Result:
{
    "name": "Proxima Centauri",
    "type": "Star",
    "distance_from_earth": 4.24,
    "distance_in_km": 40133640000000.0
}
'''


celestial_objects = [
    {"name": "Proxima Centauri", "type": "Star", "distance_from_earth": 4.24},
    {"name": "Alpha Centauri A", "type": "Star", "distance_from_earth": 4.37},
    {"name": "Alpha Centauri B", "type": "Star", "distance_from_earth": 4.37},
    {"name": "Barnard's Star", "type": "Star", "distance_from_earth": 5.96},
    {"name": "Wolf 359", "type": "Star", "distance_from_earth": 7.78},
    {"name": "Sirius A", "type": "Star", "distance_from_earth": 8.6},
    {"name": "Vega", "type": "Star", "distance_from_earth": 25.04},
    {"name": "Betelgeuse", "type": "Star", "distance_from_earth": 548.7},
    {"name": "Andromeda Galaxy", "type": "Galaxy", "distance_from_earth": 2537000.0},
    {"name": "Triangulum Galaxy", "type": "Galaxy", "distance_from_earth": 2992000.0},
]

convert_to_trillion_km = [print(data) for data in map(lambda bodies: {**bodies, "distance_from_earth":str(bodies["distance_from_earth"]*9.461*(10**12))+" Trillion Kilometers"},celestial_objects)]
