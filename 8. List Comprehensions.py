def permutations(lst):

    if len(lst) == 1:
        return [lst]

    perms = permutations(lst[1:])
    num = [lst[0]]
    result = []

    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + num + perm[i:])

    #return result

    return result[:1]


x = int(input())
y = int(input())
z = int(input())
n = int(input())


# List comprehension is down below
# res_lst = []
#
#
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             rs = permutations([i, j, k])
#             if sum(rs[0]) != n:
#                 res_lst.append(rs[0])
#
# print(res_lst)

print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if sum(permutations([i, j, k])[0]) != n])
