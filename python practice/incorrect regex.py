import re

T = int(input())
for i in range(T):
    S = input()
    val = True
    try:
        re.compile(S)
    except re.error:
        val = False
    print(val)
