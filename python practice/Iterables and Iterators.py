import itertools 
N = int(input())
letter = list(map(str,input().split()))
k = int(input())
count = 0
letter_list = list(itertools.combinations(letter,k))
for i in letter_list:
    if 'a' in i:
        count += 1
probability = count / len(letter_list)
print(round(probability,3))
