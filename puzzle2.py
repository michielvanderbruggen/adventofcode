value1 = 151
increments = 0
list = []
totallist = []

with open('input.txt', 'r') as handler:
    for line in handler:
        value2 = int(line)
        list.append(value2)
print(list)

for i in range(len(list)-2):
    totallist.append(list[i]+list[i+1]+list[i+2])
print(totallist)

value1 = totallist[0]
for i in range(len(totallist)):
    print(i)
    value2 = totallist[i]
    print('Value1:', value1, ' . Value2:', value2)
    if value2 > value1:
        increments += 1
    value1 = value2

print('Number of increments:', increments)

