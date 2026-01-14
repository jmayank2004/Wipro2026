#2. Create a generator function that yields the first N Fibonacci numbers

def Count(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
limit=int(input("Enter the limit: "))
for num in Count(limit):
    print(num)