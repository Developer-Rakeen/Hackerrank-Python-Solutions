n = int(input("Enter number: "))
lst = []
i = 0
while i < n:
    lst.append(i)
    i += 1
for i in range(n):
    print(lst[i] * lst[i])
