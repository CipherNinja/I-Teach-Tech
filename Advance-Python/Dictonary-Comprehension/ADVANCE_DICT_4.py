# Problem 2: Create a Dictionary of Usernames and Password Strength
# Problem: Given a list of users with their usernames and password strings, create a dictionary where the key is the username and the value is a boolean indicating whether the password is "strong" (at least 8 characters, contains a number, and a special character).
import re

users = [('john_doe', 'password123!'), ('alice_smith', '12345'), ('bob_jones', 'strongPassword!2')]

# Function to check if password is strong
def is_strong_password(password):
    return bool(re.match(r'^(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', password))


select_query = {user:is_strong_password(password) for (user,password) in users}
print(select_query)