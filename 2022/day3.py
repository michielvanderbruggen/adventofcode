
prioSum = 0
prioSum2 = 0
itemsList = []

with open('input3.txt', 'r') as handler:
    for line in handler:
        itemsList.append(line[:-1])

for items in itemsList:
    length = int(len(items)/2)
    comp1 = items[:length]
    comp2 = items[length:]
    for nr in range(length):
        item = comp1[nr:nr+1]
        if item in comp2:
            if item.isupper():
                prio = ord(item)-38
            else:
                prio = ord(item)-96
            prioSum += prio
            break

for nr in range(0, int(len(itemsList)), 3):
    for pr in range(int(len(itemsList[nr]))):
        item = itemsList[nr][pr:pr+1]
        if item in itemsList[nr+1] and item in itemsList[nr+2]:
            if item.isupper():
                prio2 = ord(item)-38
            else:
                prio2 = ord(item)-96
            prioSum2 += prio2
            break

print('Total score puzzle 1:', prioSum)
print('Total score puzzle 2:', prioSum2)