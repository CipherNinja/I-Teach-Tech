# Problem 3: Filter Active Users Based on Last Login Date
# Problem: Given a dictionary of users with their last login dates,
#  filter out the users who haven't logged in in the last 30 days.
#  Assume the dates are in the format YYYY-MM-DD.

from datetime import datetime, timedelta

users_last_login = {
    'john_doe': '2024-11-15',
    'alice_smith': '2024-09-01',
    'bob_jones': '2024-11-10'
}