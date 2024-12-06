# Problem 4: Deeply Nested Data Filtering
# You are working on a weather prediction system that processes weather data for different cities.
# The data is stored as a list of dictionaries, where each dictionary represents a city with nested information
# about temperature, humidity, and wind speed for various days.

# Your task is to filter out cities where:

# The average temperature for the last 7 days is below a certain threshold (e.g., 20°C).
# The wind speed on any of those days exceeded 15 km/h.


weather_data = [
    {"city": "CityA", "weather": [{"day": 1, "temperature": 22, "wind_speed": 12}, {"day": 2, "temperature": 18, "wind_speed": 10}, {"day": 3, "temperature": 24, "wind_speed": 5}]},
    {"city": "CityB", "weather": [{"day": 1, "temperature": 15, "wind_speed": 16}, {"day": 2, "temperature": 20, "wind_speed": 14}, {"day": 3, "temperature": 17, "wind_speed": 16}]},
    {"city": "CityC", "weather": [{"day": 1, "temperature": 18, "wind_speed": 7}, {"day": 2, "temperature": 19, "wind_speed": 8}, {"day": 3, "temperature": 21, "wind_speed": 10}]},
]

threshold_temp = 20
threshold_wind_speed = 15

# Task: Filter cities where the average temperature is below the threshold and wind speed exceeds the limit


# average temprature for CityA = (22+18+24)/3 = 21.33 
# average temprature for CityB = (15+20+17)/3 = 17.33 📉
# average temprature for CityC = (18+19+21)/3 = 19.33 📉

filter_cities = [
    print(f'\n{data}\n') for data in 
    filter(lambda weather:
        # Logic for Temprature
        round(sum([metadata['temperature']
        for metadata in weather['weather']])/len(weather["weather"]),3)<threshold_temp
        and
        #Logic for WindSpeed
        any(day['wind_speed'] > threshold_wind_speed for day in weather['weather'])
        ,weather_data)
]
