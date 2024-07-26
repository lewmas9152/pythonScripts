# iterators are used to iterate/parse through iterable objects. They know ther state at any point i.e. they know which element they are currently at and they can move to the next element

nums = [1,2,3,4,5]

# a list is an iterable but it is not an iterator, you can parse through a list using the for loop
for num in nums:
    print(num)


# for an iterator the object has  functions attributed to it e.g __next__() and __iter__() which a list doesn't have

# the dir function returns the functions attributed to the list(notice it has no __next__() and __iter__() functions )
print(dir(nums))

# the for loop turns the nums to an iterator so that it can be able to print out each of the nums till the end of the list

# to turn the nums to an iterator manually we can use the iter function which is an encaplsulation of the __iter__() dunder method

nums_2 = iter(nums)

# notice that there are the __next__() and __iter__() in the list of the metods printed
print(dir(nums_2))
# you can use the next() function to move through each of the nums in the list . You can only move foward and never backwards
print(next(nums_2))
print(next(nums_2))
print(next(nums_2))
print(next(nums_2))
print(next(nums_2))

# when you reach the end of the iterator and try to run the next method again you receive an exception i.e.StopIteration
# print(next(nums_2))

# to prevent running into a StopIteration exception you can use try except method'

while True:
        try:
            print(next(nums_2))
        except StopIteration:
            break





