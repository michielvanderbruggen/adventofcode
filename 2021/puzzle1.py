value1 = 151
increments = 0

with open('input.txt', 'r') as handler:
    for line in handler:
        value2 = int(line)
        print('VAlue1:', value1, ' . Value2:', value2)
        if value2 > value1:
            increments += 1
        value1 = value2
    print('Number of increments:', increments)

