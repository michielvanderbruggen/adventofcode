
total1 = ''
total2 = ''
crane = []
stack = []
stack.append(' ')

# inputtest.txt
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# stack.append(['Z', 'N'])
# stack.append(['M', 'C', 'D'])
# stack.append(['P'])

# input5.txt
# [N]         [C]     [Z]            
# [Q] [G]     [V]     [S]         [V]
# [L] [C]     [M]     [T]     [W] [L]
# [S] [H]     [L]     [C] [D] [H] [S]
# [C] [V] [F] [D]     [D] [B] [Q] [F]
# [Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
# [P] [P] [C] [W] [W] [F] [W] [J] [C]
# [T] [L] [D] [G] [P] [P] [V] [N] [R]
#  1   2   3   4   5   6   7   8   9 
stack.append(['T','P','Z','C','S','L','Q','N'])
stack.append(['L','P','T','V','H','C','G'])
stack.append(['D','C','Z','F'])
stack.append(['G','W','T','D','L','M','V','C'])
stack.append(['P','W','C'])
stack.append(['P','F','J','D','C','T','S','Z'])
stack.append(['V','W','G','B','D'])
stack.append(['N','J','S','Q','H','W'])
stack.append(['R','C','Q','F','S','L','V'])

with open('input5.txt', 'r') as handler:
    for line in handler:
        moveitems = int(line[5:line.find('from')-1])
        fromstack = int(line[line.find('from')+5:line.find('to')-1])
        tostack = int(line[line.find('to')+3:])
        for item in range(moveitems):
            crane.append(stack[fromstack][-1])
            stack[fromstack].pop()      
            stack[tostack].append(crane[-1])
            crane.pop()
for s in range(len(stack)):
    print(stack[s])
    total1 += stack[s][-1]


crane = []
stack = []
stack.append(' ')
stack.append(['T','P','Z','C','S','L','Q','N'])
stack.append(['L','P','T','V','H','C','G'])
stack.append(['D','C','Z','F'])
stack.append(['G','W','T','D','L','M','V','C'])
stack.append(['P','W','C'])
stack.append(['P','F','J','D','C','T','S','Z'])
stack.append(['V','W','G','B','D'])
stack.append(['N','J','S','Q','H','W'])
stack.append(['R','C','Q','F','S','L','V'])
with open('input5.txt', 'r') as handler:
    for line in handler:
        moveitems = int(line[5:line.find('from')-1])
        fromstack = int(line[line.find('from')+5:line.find('to')-1])
        tostack = int(line[line.find('to')+3:])
        for item in range(moveitems):
            crane.append(stack[fromstack][-1])
            stack[fromstack].pop()
        # This line added for puzzle 2:
        for item in range(len(crane)):      
            stack[tostack].append(crane[-1])
            crane.pop()
for s in range(len(stack)):
    print(stack[s])
    total2 += stack[s][-1]


print('Total score puzzle 1:', total1)
print('Total score puzzle 2:', total2)