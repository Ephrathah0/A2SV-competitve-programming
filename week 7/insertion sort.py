#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    number = arr[len(arr)-1]

    for i in range(len(arr)-1, -1, -1):
        if arr[i-1] > number:
            arr[i] = arr[i-1]
            if i == 0:
                arr[i] =  number
            for j in arr:
                print(j, end = " ")
        else:
            arr[i] = number
            for j in arr:
                print(j, end = " ")
            return False
        print()
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
