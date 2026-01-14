#3. Demonstrate the difference between using the iterator and generator by printing values using a for loop

class CountIterator:
    def __init__ (self,limit):
        self.limit=limit
        self.current=1
    def __iter__(self):
        return self
    def __next__ (self):
        if self.current<=self.limit:
            val=self.current
            self.current+=1
            return val
        else:
            raise StopIteration
obj=CountIterator(int(input("using iterator:")))
for num in obj:
    print(num)

def count_generator(n):
    for i in range(1,n+1):
        yield i
x=count_generator(int(input("using generator:")))
for num in x:
    print(num)