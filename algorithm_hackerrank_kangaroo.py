#!/bin/python3

import math 
import os
from itertools import islice,accumulate,repeat
from functools import partial
from operator import add
def take(n, it):
    return[x for x in islice(it,n)]
def drop(n,it):
    return islice(it,n,None)
head=next
tail=partial(drop,1)
# Complete the kangaroo function below


def iterate(f,x):
    return accumulate(repeat(x),lambda fx,_:f(fx))
def kangaroo(x1, v1, x2, v2):
    def addm(x):return add(v1,x)
    def addM(x):return add(v2,x)
    def lazy_min_distance():
        return iterate(addm,x1)
    def lazy_max_distance():
        return iterate(addM,x2)
    x=(take(5000,lazy_max_distance()))
    y=(take(5000,lazy_min_distance()))
    z=[x1 - x2 for (x1, x2) in zip(x,y)]
    if 0 in z:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

