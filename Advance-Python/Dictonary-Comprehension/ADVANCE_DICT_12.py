# Problem 10: Identify Users Who Have Reset Their Password Recently
# Problem: You have a list of users with their last password reset dates.
# Create a dictionary where the key is the username, and the value is True if the password was reset within the last 30 days, and False otherwise.


from datetime import datetime, timedelta

users_password_reset = {
    'john_doe': '2024-11-20',
    'alice_smith': '2024-09-15',
    'bob_jones': '2024-11-01'
}

# Get today's date
today = datetime.today()