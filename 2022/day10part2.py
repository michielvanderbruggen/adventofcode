
x = 1
v = 0
cycle = 1
pos = 0
regel = 0
screen = ['','','','','','','','','']
vertical = 0
endscreen = [40, 80, 120, 160, 200]
# endscreen = [39, 79, 119, 159, 199]

def sprite(_x):
    sprite = [_x-1, _x, _x+1]
    return(sprite)


with open('input10.txt', 'r') as handler:
    for line in handler:
        print()
        regel += 1
        print("Regel:", regel, line[:-1], '  Vertical:', vertical)
        spritepos = ''
        for i in range(x-1):
            spritepos += '.'
        spritepos += '###'
        print(spritepos)

        command = line[:4]
        if command == 'noop':
            print('Clycle:', cycle, '  Pos:', pos, '  X:', x)
            if pos in sprite(x):
                screen[vertical] += '#'
            else:
                screen[vertical] += '.'
            print(screen[vertical])
            pos += 1
            if pos in endscreen: 
                vertical += 1
                pos = 0
            cycle += 1

        if command == 'addx':
            print('Clycle:', cycle, '  Pos:', pos, '  X:', x)
            if pos in sprite(x):
                screen[vertical] += '#'
            else:
                screen[vertical] += '.'
            print(screen[vertical])
            pos += 1
            if pos in endscreen: 
                vertical += 1
                pos = 0
            cycle += 1

            print('Clycle:', cycle, '  Pos:', pos, '  X:', x)
            if pos in sprite(x):
                screen[vertical] += '#'
            else:
                screen[vertical] += '.'
            print(screen[vertical])
            pos += 1
            if cycle in endscreen: 
                vertical += 1
                pos = 0
            cycle += 1

            v = (int(line[5:-1]))
            x += v


print()
for i in range(6):
    print(screen[i])
# print('Total score puzzle 2:', total2)