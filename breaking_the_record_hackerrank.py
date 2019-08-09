#!/bin/python3
import os
# Complete the breakingRecords function below.
def breakingRecords(scores):
    return len(list(filter(lambda x:scores[x]>max(scores[0:x]),range(1,len(scores))))),len(list(filter(lambda x:scores[x]<min(scores[0:x]),range(1,len(scores)))))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

