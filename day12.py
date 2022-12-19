
map = []
path = []

with open('inputtest.txt', 'r') as handler:
    for line in handler:
        map.append(line[:-1])

S = []
P = []
E = []
ymax = len(map)
xmax = len(map[0])

linenr = 0
for i in range(len(map)):
    print(map[i])
    if 'S' in map[i]:
        x, y = map[i].find('S'), i
        S.append(x)
        S.append(y)
        print(S)

    if 'E' in map[i]:
        x, y = map[i].find('E'), i
        E.append(x)
        E.append(y)
        print(E)

while True:
    # Try up
    
