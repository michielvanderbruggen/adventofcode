
# 99x99
forrest = []
counted = []

with open('input8.txt', 'r') as handler:
    for line in handler:
        forrest.append(line[:-1])

# Add the outher rim
for x in range(0, 99):
    counted.append(str(x) + ',0')
for x in range(0, 99):
    counted.append(str(x) + ',98')
for y in range(1, 98):
    counted.append('0,' + str(y))
for y in range(1, 98):
    counted.append('98,' + str(y))

# Left 2 right
for y in range(99):
    hightree = int(forrest[y][0])
    for x in range(99):
        treeloc = str(x) + ',' + str(y)
        tree = int(forrest[y][x])
        prevtree = int(forrest[y][x-1])
        if tree > prevtree and tree > hightree and treeloc not in counted:
            print('Tree', treeloc, 'has size',tree, 'and is bigger that', prevtree,'and highest', hightree)
            counted.append(treeloc)
            hightree = tree
            print('Count:', len(counted))

# Right 2 left
for y in range(99):
    hightree = int(forrest[y][0])
    for x in range(98, -1, -1):
        treeloc = str(x) + ',' + str(y)
        tree = int(forrest[y][x])
        prevtree = int(forrest[y][x-1])
        if tree > prevtree and tree > hightree and treeloc not in counted:
            print('Tree', treeloc, 'has size',tree, 'and is bigger that', prevtree,'and highest', hightree)
            counted.append(treeloc)
            hightree = tree
            print('Count:', len(counted))

# Top 2 bottom
for x in range(99):
    hightree = int(forrest[0][x])
    for y in range(99):
        treeloc = str(x) + ',' + str(y)
        tree = int(forrest[y][x])
        prevtree = int(forrest[y][x-1])
        if tree > prevtree and tree > hightree and treeloc not in counted:
            print('Tree', treeloc, 'has size',tree, 'and is bigger that', prevtree,'and highest', hightree)
            counted.append(treeloc)
            hightree = tree
            print('Count:', len(counted))

# Bottom 2 top
hightree = int(forrest[0][x])
for x in range(99):
    for y in range(98, -1, -1):
        treeloc = str(x) + ',' + str(y)
        tree = int(forrest[y][x])
        prevtree = int(forrest[y][x-1])
        if tree > prevtree and tree > hightree and treeloc not in counted:
            print('Tree', treeloc, 'has size',tree, 'and is bigger that', prevtree,'and highest', hightree)
            counted.append(treeloc)
            hightree = tree
            print('Count:', len(counted))

print()        
print('Total score puzzle 1:', len(counted))
# print('Total score puzzle 2:', total2)
# 1943 too high
# 1935 too high
# 1538 too low
# 1887 is false