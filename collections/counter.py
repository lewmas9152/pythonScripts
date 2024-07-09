from collections import Counter

# Counter is a dictionary subclass that counts hashable objects
# It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values
# Counts are allowed to be any integer value including zero or negative counts
# The Counter class is similar to bags or multisets in other languages

# Example 1: Creating a Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter) # Counter({'a': 5, 'b': 5, 'c': 5})
print(my_counter.items()) # dict_items([('a', 5), ('b', 5), ('c', 5)])
print(my_counter.most_common()[0][1])  #5
print(my_counter.keys()) #dict_keys(['a', 'b', 'c'])
print(my_counter.values()) #dict_values([5, 4, 3])


# Example 2: Creating a Counter with a list
my_list = [1,2,3,4,1,2,6,7,3,8,1]
my_counter = Counter(my_list)
print(my_counter) # Counter({1: 3, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1})
print(my_counter[1]) #3

# Example 3: Creating a Counter with a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2}
my_counter = Counter(my_dict)
print(my_counter) # Counter({'c': 3, 'b': 2, 'e': 2, 'a': 1, 'd': 1})
print(my_counter['a']) # 1
print(my_counter['f']) # 0
print(my_counter.most_common(1)) # [('c', 3)]   # Returns the most common element in the Counter
print(my_counter.items()) # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 1), ('e', 2)])  

# Example 4: Creating a Counter with keyword arguments
my_counter = Counter(a=2, b=3, c=1)
print(my_counter) # Counter({'b': 3, 'a': 2, 'c': 1})

# Example 5: Accessing Counts
my_counter = Counter(a=2, b=3, c=1)
print(my_counter['a']) # 2

# Example 6: Accessing Counts of an element that does not exist
my_counter = Counter(a=2, b=3, c=1)
print(my_counter['d']) # 0


# Example 7: Setting Counts
my_counter = Counter(a=2, b=3, c=1)
my_counter['a'] = 1
print(my_counter) # Counter({'b': 3, 'a': 1, 'c': 1})

# Example 8: Setting Counts of an element that does not exist
my_counter = Counter(a=2, b=3, c=1)
my_counter['d'] = 0
print(my_counter) # Counter({'b': 3, 'a': 2, 'c': 1, 'd': 0})

# Example 9: Removing elements from the Counter
my_counter = Counter(a=2, b=3, c=1)
del my_counter['a']
print(my_counter) # Counter({'b': 3, 'c': 1})

# Example 10: Removing elements from the Counter that does not exist
my_counter = Counter(a=2, b=3, c=1)
del my_counter['d']
# Raises KeyError

# Example 11: Arithmetic Operations on Counters
c1 = Counter(a=2, b=3, c=1)
c2 = Counter(a=1, b=2, c=3)
print(c1 + c2) # Counter({'b': 5, 'c': 4, 'a': 3})
print(c1 - c2) # Counter({'a': 1, 'b': 1})
print(c1 & c2) # Counter({'b': 2, 'a': 1, 'c': 1})
print(c1 | c2) # Counter({'b': 3, 'c': 3, 'a': 2})

