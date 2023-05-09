n = int(input())
lst = []
for _ in range(n):
    inp = input().split()  # it's a list
    if inp[0] == 'insert':
        lst.insert(int(inp[1]), int(inp[2]))
    elif inp[0] == 'print':
        print(lst)
    elif inp[0] == 'remove':
        lst.remove(int(inp[1]))
    elif inp[0] == 'append':
        lst.append(int(inp[1]))
    elif inp[0] == 'sort':
        lst.sort()
    elif inp[0] == 'pop':
        lst.pop()
    elif inp[0] == 'reverse':
        lst.reverse()