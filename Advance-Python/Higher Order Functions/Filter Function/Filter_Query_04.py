# Problem 5: Filtering Positive Numbers
# You are working on a machine learning project and need to filter out all negative values
# from a dataset containing various numbers (list of integers).
numbers = [-23, 45, -67, 89, 12, -5, 34] #dataset

filter_negative = [num for num in filter(lambda n:n>0,numbers)]
print(filter_negative)