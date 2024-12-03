# Problem 4: Group Users by Subscription Tier
# Problem: You have a list of users with their subscription tiers.
# Create a dictionary where the key is the subscription tier and the value is a list of usernames.

users = [('john_doe', 'premium'), ('alice_smith', 'basic'), ('bob_jones', 'premium'), ('charlie_brown', 'basic')]


group_user_by_subscription = {subscription:list(filter(lambda user:user[1]==subscription,users)) for (username,subscription) in users}
print(group_user_by_subscription)