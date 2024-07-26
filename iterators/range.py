class Myrange():
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.current =start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current< self.end:
            current = self.current
            self.current +=1
            return current
        else:
            raise StopIteration
    

my_range = Myrange(1,9);

for num in my_range :
    print(num)