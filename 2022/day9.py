
visited = ['0,0']
head = [0,0]
tail = [0,0]

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
            if dir == 'R': head[0] += 1
            if dir == 'L': head[0] -= 1
            if dir == 'U': head[1] += 1
            if dir == 'D': head[1] -= 1
            print('Head is gegaan naar:', dir)

            print('Head:', head, 'Tail:', tail)
            actions = distance(head, tail)
            print('De actie wordt:', actions)

            if 'right' in actions: tail[0] += 1
            if 'left' in actions: tail[0] -= 1
            if 'up' in actions: tail[1] += 1
            if 'down' in actions: tail[1] -= 1

            print('Head:', head, 'Tail:', tail)
            if position(tail) not in visited:
                print('Log location')
                visited.append(position(tail))

print(visited)


print()        
print('Total score puzzle 1:', len(visited))
# print('Total score puzzle 2:', total2)

# 2887, 2999 too low