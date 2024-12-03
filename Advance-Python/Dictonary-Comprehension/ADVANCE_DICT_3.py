# Problem 1: Create a Dictionary of Usernames and Email Addresses
# Problem: You have a list of users, each represented by a tuple of (username, email). You need to create a dictionary where the username is the key, and the email address is the value.

users = [('john_doe', 'john@example.com'), ('alice_smith', 'alice@example.com'), ('bob_jones', 'bob@example.com')]

query = {user:email for (user,email) in users}
print(query)