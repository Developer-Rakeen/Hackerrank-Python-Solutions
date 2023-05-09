dict = {}
n = int(input("Enter size:"))
for i in range(n):
    key, *temp = input("Enter values(1st is key and"
                       " rest of it are"
                       " its values):").split()
    value = list(map(float, temp))
    dict.update({key: value})
parst = input()

result = float(sum(dict.get(parst)) / len(dict.get(parst)))
print("%.2f" % result)