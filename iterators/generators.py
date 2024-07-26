def my_iterator(nums):
    for num in nums:
        print("yielding numbers")
        yield num
    

my_iterator([1,2,3,4,5])

