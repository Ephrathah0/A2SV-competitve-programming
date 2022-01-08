n = int(input())
s = set(map(int, input().split()))
nCommands = int(input())
for i in range(nCommands):
    command = input();
    theList = command.split()
    if theList[0] == 'pop':
        s.pop()
    elif theList[0] == 'remove':
        val = int(theList[1])
        if val in s:
            s.remove(int(theList[1]))
    elif theList[0] == 'discard':
        s.discard(int(theList[1]))
print(sum(s))
