# Problem 2: Create a Dictionary Mapping Words to Their Lengths (Using map() and lambda)
# Problem: Given a list of words, create a dictionary where each word is a key, and its length is the value. Use map() and lambda to process the list.

# map(function,iterable)
# lambda arg1,arg2: arg1+arg2 
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana', 'apple']

generate = { word:length for word,length in zip(words,map(lambda x:len(x),words)) }
print(generate)