
# 99x99
forrest = []
counted = []
highscore = 0

with open('input8.txt', 'r') as handler:
    for line in handler:
        forrest.append(line[:-1])

for y in range(99):
    for x in range(99):
        treeloc = str(x) + ',' + str(y)
        tree = int(forrest[y][x])
        print()
        print('Checking loc:', treeloc)
        if x == 0 or y == 0 or x == 98 or y == 98:
            counted.append(treeloc)
        else:
            # Look left
            visible = True
            for i in range(0, x):
                if int(forrest[y][i]) >= tree:
                    visible = False
                    break
            if visible and treeloc not in counted:
                print('Tree', treeloc, 'height',tree, 'is in sight from the left')
                counted.append(treeloc)
            # Look right
            visible = True
            for i in range(x+1, 99):
                if int(forrest[y][i]) >= tree:
                    visible = False
                    break
            if visible and treeloc not in counted:
                print('Tree', treeloc, 'height',tree, 'is in sight from the right')
                counted.append(treeloc)
            # Look up
            visible = True
            for i in range(0, y):
                if int(forrest[i][x]) >= tree:
                    visible = False
                    break
            if visible and treeloc not in counted:
                print('Tree', treeloc, 'height',tree, 'is in sight from above')
                counted.append(treeloc)
            # Look down
            visible = True
            for i in range(y+1, 99):
                print('i,y=',i,y,'height=', forrest[y][i])
                if int(forrest[i][x]) >= tree:
                    print('forrest higher than tree because:', forrest[y][i],tree)
                    visible = False
                    break
            if visible and treeloc not in counted:
                print('Tree', treeloc, 'height',tree, 'is in sight from the bottom')
                counted.append(treeloc)
                print('Count:', len(counted))

print()        
print('Total score puzzle 1:', len(counted))
# print('Total score puzzle 2:', total2)
