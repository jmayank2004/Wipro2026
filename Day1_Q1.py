#Question – Widely Used Built-in Functions & Lambda

#1. Uses range() to generate numbers from 1 to 20
for a in range(1,21):
    print(a,end= " ")

#2. Uses filter() with a lambda to select only even numbers
num = [1,2,3,4,5,6,7,8,9]
even_num = list(filter(lambda n : n%2==0,num))
print(even_num)

#3. Uses map() with a lambda to square the filtered numbers
square_num = list(map(lambda x: x**2,even_num))
print(square_num)

#4. Uses reduce() to calculate the sum of squared even numbers
from functools import reduce
sum_of_square_num = reduce(lambda x,y : x+y,square_num)
print(sum_of_square_num)

#5. Uses enumerate() to print the index and value of the final result list
resul=list(enumerate(square_num,start=1))
print(resul)
