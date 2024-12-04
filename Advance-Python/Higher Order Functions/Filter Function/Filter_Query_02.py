# Problem 2: Filtering Out Odd Numbers
# You are working on a data cleaning project where you need to clean up raw data of ages
#  (in a list) from an external API. The task is to filter out all odd-numbered ages.

ages = [21, 32, 45, 60, 77, 88, 91, 101]

odd_filter = [data for data in ages if data%2!=0]
print(odd_filter)