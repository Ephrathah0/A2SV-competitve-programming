#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    
    def cookies(k, A):
    heapq.heapify(A)
    count = 0
    while A[0] < k: 
        s1 = heapq.heappop(A)
        if len(A) > 0:
            s2 = heapq.heappop(A)
            new = s1 + (s2 * 2)
            heapq.heappush(A, new)
            count += 1
        if not A:
            return -1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
