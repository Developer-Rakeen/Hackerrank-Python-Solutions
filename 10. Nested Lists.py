N = int(input())

lst = []

nest_lst = []

find_min_lst = []

for i in range(N):
    temp1 = input()
    temp2 = input()
    find_min_lst.append(float(temp2))
    nest_lst.append(temp1)
    nest_lst.append(float(temp2))
    lst.append(nest_lst)
    nest_lst = []


minimum = min(find_min_lst)
result = max(find_min_lst)
temp = max(find_min_lst)


for i in range(len(lst)):
    if lst[i][1] < result and lst[i][1] > minimum:
        result = lst[i][1]


prnt_lst = []

for i in range(len(lst)):
    if lst[i][1] == result:
        prnt_lst.append(lst[i][0])


prnt_lst.sort()

for prnt in prnt_lst:
    print(prnt)