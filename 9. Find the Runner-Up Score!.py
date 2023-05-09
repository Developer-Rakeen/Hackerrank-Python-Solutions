n = int(input("Enter size:"))

lst = []

templist = input("Enter numbers:").split()

for i in range(n):
    x = int(templist[i])
    lst.append(x)

maximum = max(lst)
result = min(lst)
temp = min(lst)

for i in range(n):
    if lst[i] > result and lst[i] < maximum:
        result = lst[i]

print(result)