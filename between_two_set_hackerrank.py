#!/bin/python3

import math
import os
from itertools import islice,accumulate,repeat
from functools import reduce
from operator import add
def take(n, it):
    return[x for x in islice(it,n)]
def iterate(f,x):
    return accumulate(repeat(x),lambda fx,_:f(fx))
def add1(x):return add(1,x)
def lazy_integer():return iterate(add1,1)
def lcm(a, b):return abs(a*b) // math.gcd(a, b)
def getTotalX(a, b):
    d,c=reduce(math.gcd,b),reduce(lcm,a)
    return (len(list(filter(lambda x: d%x==0,[i*c for i in take(d//c,lazy_integer())]))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

