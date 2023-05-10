# this code works in Pypy 3 not in Python 3
n = int(input("Enter size:"))
tup = tuple(map(int, input().split()))
print(hash(tup))