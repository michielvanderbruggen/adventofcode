
visited = ['0,0']

rope = {}
for knot in range(11):
    rope[knot] = [0,0]
print(rope)


def distance(head_, tail_):
    moves = []
    if abs(head_[0] - tail_[0]) + abs(head_[1] - tail_[1]) == 3:
        print('Diagonaal')
        if head_[0] - tail_[0] > 0:
            moves.append('right')
        if head_[0] - tail_[0] < 0:
            moves.append('left')
        if head_[1] - tail_[1] > 0:
            moves.append('up')
        if head_[1] - tail_[1] < 0:
            moves.append('down')
        return(moves)

    if abs(head_[0] - tail_[0]) > 1 or abs(head_[1] - tail_[1]) > 1:
        print('Straight')
        if head_[0] - tail_[0] > 1:
            moves.append('right')
        if head_[0] - tail_[0] < -1:
            moves.append('left')
        if head_[1] - tail_[1] > 1:
            moves.append('up')
        if head_[1] - tail_[1] < -1:
            moves.append('down')
        return(moves)
    
    else:
        print('Stay')
        return(moves)

def position(tail_):
    string = str(tail_[0]) + ',' + str(tail_[1])
    return(string)

with open('input9.txt', 'r') as handler:
    for line in handler:
        dir = line[:1]
        for steps in range(int(line[2:])):
            print()
            if dir == 'R': rope[0][0] += 1
            if dir == 'L': rope[0][0] -= 1
            if dir == 'U': rope[0][1] += 1
            if dir == 'D': rope[0][1] -= 1
            print('Head is gegaan naar:', dir)

            for knot in range(0, 10):
                print('knot:', knot, 'pos:',rope[knot], 'next knot:', knot+1, 'pos:', rope[knot+1])
                actions = distance(rope[knot], rope[knot+1])
                print('De actie wordt:', actions)

                if 'right' in actions: rope[knot+1][0] += 1
                if 'left' in actions: rope[knot+1][0] -= 1
                if 'up' in actions: rope[knot+1][1] += 1
                if 'down' in actions: rope[knot+1][1] -= 1

            tail = rope[9]
            if position(tail) not in visited:
                print('Log location')
                visited.append(position(tail))

print(visited)


print()        
print('Total score puzzle 1:', len(visited))
# print('Total score puzzle 2:', total2)
