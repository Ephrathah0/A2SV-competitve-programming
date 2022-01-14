# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
S  = input()    
for key, value in groupby(S):
    group_obj = len(list(value)), int(key)
    print(tuple(group_obj), end = " ")
