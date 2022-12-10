
size = 99
forrest = []
highscore = 0



with open('input8.txt', 'r') as handler:
    for line in handler:
        forrest.append(line[:-1])

for y in range(size):
    for x in range(size):
        left = 0
        right = 0
        up = 0
        down = 0
        treeloc = str(x) + ',' + str(y)
        tree = int(forrest[y][x])
        print()
        print('Checking loc:', treeloc, 'with height', tree)
        # Look left
        for i in range(1, size):
            if x-i < 0:
                print('No more trees')
                break

            print('to the left is',x-i,y, 'with height', forrest[y][x-i])
            left += 1

            if int(forrest[y][x-i]) >= tree:
                print('Same or higher')
                break

        print('Left',left)

        # # Look right
        for i in range(1, size):
            if x+i == size:
                print('Last tree')
                break

            print('to the right is',x+i,y, 'with height', forrest[y][x+i])
            right += 1

            if int(forrest[y][x+i]) >= tree:
                print('Same or higher')
                break

        print('Right', right)

        # # Look down
        for i in range(1, size):
            if y+i == size:
                print('Last tree')
                break

            print('down is',x,y+i, 'with height', forrest[y+i][x])
            down += 1

            if int(forrest[y+i][x]) >= tree:
                print('Same or higher')
                break
            
        print('Down', down)

        # # Look up
        for i in range(1, size):
            if y-i < 0:
                print('Last tree')
                break

            print('up is',x,y-i, 'with height', forrest[y-i][x])
            up += 1

            if int(forrest[y-i][x]) >= tree:
                print('Same or higher')
                break
            
        print('Up', up)
        scene = left * right * up * down
        print('Scene is', scene)
        if scene == 3676716: exit()
        if scene > highscore:
            highscore = scene
            highloc = treeloc
print()        
print('Total score puzzle 2:', highscore, highloc)
