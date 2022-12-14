forrest = []
counted = []

with open('input8.txt', 'r') as handler:
    for line in handler:
        forrest.append(line[:-1])

# Left 2 right
y=1
hightree = int(forrest[y][0])
for x in range(1, 98):
    treeloc = str(x) + ',' + str(y)
    tree = int(forrest[y][x])
    prevtree = int(forrest[y][x-1])
    print()
    print('treeloc=',treeloc)
    print('tree=', tree)
    print('prevtree=',prevtree)
    if tree > prevtree and tree > hightree and treeloc not in counted:
        print('Tree', treeloc, 'has size',tree, 'and is bigger that', prevtree,'and highest', hightree)
        counted.append(treeloc)
        hightree = tree
        print('Count:', len(counted))

# 301324204451515335252342253126503010214314026675523135330307170405066545120014006214521335013332134
#           i