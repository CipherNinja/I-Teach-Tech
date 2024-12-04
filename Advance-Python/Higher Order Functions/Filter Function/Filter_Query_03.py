# Problem 3: Filtering Valid Emails
# You are developing an authentication system for a user management platform. You have an API response containing a list of email addresses, and your task is to filter out invalid email addresses.
# Task: Use filter() to filter out valid email addresses. A valid email must contain '@' and '.'

emails = ["john.doe@gmail.com", "alice123@", "bob_smith@yahoo.com", "mary@domain"]

valid_email = [email for email in filter(lambda mail: "@" in mail and '.' in mail,emails)]
print(valid_email)