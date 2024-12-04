# Problem 1: Complex Nested Data Filtering
# You are developing a social media analytics tool.
# You receive an API response containing user profiles, including their activities and status.
# You need to filter out users who are active and have posted at least 3 activities.

users = [
    {"username": "john_doe", "status": "active", "activities": ["post", "like", "share"]},
    {"username": "alice_smith", "status": "inactive", "activities": ["comment"]},
    {"username": "bob_jones", "status": "active", "activities": ["like"]},
    {"username": "mary_wilson", "status": "active", "activities": ["share", "comment"]},
    {"username": "carla_lee", "status": "active", "activities": []},
]

# Task: Filter users who are active and have at least 3 activities
ls=[1,2,3,4,6]
filter_users = [usr for usr in filter(lambda x:x['status']=="active" and len(x["activities"])>=3,users)]
print(filter_users)