
dir = 'root/'
list = []
file = ''

total1 = 0
total2 = 0

# Create a list with a line per file
with open('input7.txt', 'r') as handler:
    for line in handler:
        line = line[:-1]
        if line[:4] == '$ cd':
            if line == '$ cd /':
                pass
            elif line == '$ cd ..':
                dir = dir[:dir.rfind('/', 0, -1)+1]
            else:
                dir = dir + line[5:] + '/'
        if line[:1].isnumeric():
            file = dir + ' ' + line[line.find(' ')+1:] + '-' + line[:line.find(' ')]
            list.append(file)
            file = ''

# Create a dict with total values per dir
dirtot = {}
for line in list:
    dir = line[:line.find(' ')]
    bytes = int(line[line.find('-')+1:])
    if dir in dirtot:
        dirtot[dir] += bytes
    else:
        dirtot[dir] = bytes
    # Add subdirectories to parent dir
    while len(dir) > 5:
        dir = dir[:dir.rfind('/', 0, -1)+1]
        if dir in dirtot:
            dirtot[dir] += bytes
        else:
            dirtot[dir] = bytes

# Calc sum of dirs smaller than 100000
for key in dirtot:
    if dirtot[key] <= 100000:
        total1 += dirtot[key]

print()
spaceused = dirtot['root/']
spaceavailable = 70000000 - spaceused
spacerequired = 30000000 - spaceavailable
print('Total space in use:', spaceused)
print('Space available:', spaceavailable)
print('Space required:', spacerequired)

dirtotsorted = dict(sorted(dirtot.items(), key=lambda item: item[1], reverse=True))
print()
for key in dirtotsorted:
    if dirtotsorted[key] > spacerequired:
        deldir = key
print('deldir:', deldir , 'with size:', dirtotsorted[deldir])
total2 = dirtotsorted[deldir]

print()        
print('Total score puzzle 1:', total1)
print('Total score puzzle 2:', total2)