# Problem 9: Generate a Dictionary of Dates for Upcoming Events
# Problem: You are managing a list of upcoming events. 
# Create a dictionary where the key is the event name and the value is the event date.

events = [('Birthday Party', '2024-12-25'), ('Conference', '2025-01-10'), ('Meeting', '2024-12-05')]

dictonary_of_upcoming_events = { date:event for (event,date) in events }
print(dictonary_of_upcoming_events)