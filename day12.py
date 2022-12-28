
map = []
start = []
pos = []
look = []
end = []
dead = []
trail = []


def value(pos_, map_):
    return(ord(map_[pos_[0]][pos_[1]]))

# Read map into list
with open('inputtest.txt', 'r') as handler:
    for line in handler:
        map.append(line[:-1])

# Set borders as dead
for i in range(len(map[0])+2):
    dead.append([i-1, -1])
    dead.append([i-1, (len(map))])

for i in range(len(map)+2):
    dead.append([-1, i-1])
    dead.append([((len(map[0]))), i-1])

# Find start and end
linenr = 0
for i in range(len(map)):
    if 'S' in map[i]:
        x, y = map[i].find('S'), i
        start.append(x)
        start.append(y)

    if 'E' in map[i]:
        x, y = map[i].find('E'), i
        end.append(x)
        end.append(y)

pos = start
look = pos

print(dead)
print('Start:', start)
print('End:', end)
print('Pos:', pos)
print('Look:', look)

while pos != end:
    # try left
    look[0] = pos[0]-1
    print('Pos:', pos, 'Look:', look)
    if ord(map[look[0]][look[1]]) <= ord(map[pos[0]][pos[1]])+1 and look not in dead:
        pos = look
        print('GO')



    break

