# Problem 1: Updating User Information
# Scenario:
# You are working as a software developer at XYZ Corp, and you need to update the user profile information in your system.
# The system receives a list of users with their profile details.
# Your task is to ensure that the user’s age is updated by adding one year to their current age.

# Task:
# Use map() to increment the age of each user in the list.


users = [
    {"username": "john_doe", "age": 29},
    {"username": "alice_smith", "age": 35},
    {"username": "bob_jones", "age": 22},
]

# Task: Update the age of each user by adding 1 year

update_ages = [print(ages) for ages in map(lambda all_ages: all_ages["age"]+1 ,users)]
