import os
from itertools import islice,accumulate,repeat
from functools import reduce
from operator import add
def take(n, it):
    return[x for x in islice(it,n)]
def iterate(f,x):
    return accumulate(repeat(x),lambda fx,_:f(fx))
def add1(x):return add(1,x)
def lazy_min_distance():return iterate(add1,1)
# Complete the factorial function below.
def factorial(n):
    return(reduce(lambda a,b : a*b,take(n,lazy_min_distance())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

