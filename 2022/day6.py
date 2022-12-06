
with open('input6.txt', 'r') as handler:
    line = handler.readline()

for i in range(len(line)):
    mark = set(line[i:i+4])
    if len(mark) == 4:
        total1 = i+4
        break

for i in range(len(line)):
    mark = set(line[i:i+14])
    if len(mark) == 14:
        total2 = i+14
        break

print('Total score puzzle 1:', total1)
print('Total score puzzle 2:', total2)