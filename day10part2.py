
x = 1
v = 0
cycle = 1
regel = 0
screen = ['','','','','','']
vertical = 0
endscreen = [40, 80, 120, 160, 200, 240]

def sprite(_x):
    sprite = [_x-1, _x, _x+1]
    return(sprite)


with open('inputtest.txt', 'r') as handler:
    for line in handler:
        print()
        regel += 1
        print("Regel:", regel, line[:-1])

        command = line[:4]
        if command == 'noob':
            print('Clycle:', cycle, '  X:', x)
            if cycle in sprite(x):
                screen[vertical] += '#'
            else:
                screen[vertical] += '.'
            cycle += 1
            print(screen[vertical])

        if command == 'addx':
            print('Clycle:', cycle, '  X:', x)
            if cycle in sprite(x):
                screen[vertical] += '#'
            else:
                screen[vertical] += '.'
            cycle += 1
            print(screen[vertical])

            if cycle in endscreen: 
                vertical += 1

            print('Clycle:', cycle, '  X:', x)
            if cycle in sprite(x):
                screen[vertical] += '#'
            else:
                screen[vertical] += '.'
            cycle += 1
            print(screen[vertical])

            v = (int(line[5:-1]))
            x += v
        if cycle in endscreen: 
            vertical += 1



print()
for i in range(6):
    print(screen[1])
# print('Total score puzzle 2:', total2)