from collections import Counter
X = int(input())
shoesize = Counter(map(int,input().split()))
N = int(input())

sumearnings = 0
for j in range(N):
    sizes, x  = map(int,input().split())
    if sizes in shoesize and shoesize[sizes] >0:
        shoesize[sizes] -=1
        sumearnings += x
print(sumearnings)
