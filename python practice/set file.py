# Enter your code here. Read input from STDIN. Print output to STDOUT
nEng = int(input())
engSet = set(map(int, input().split()) )
nFre = int(input())
freSet = set(map(int, input().split()) )


eng_U_fre = engSet.union(freSet)
print(len(eng_U_fre))
