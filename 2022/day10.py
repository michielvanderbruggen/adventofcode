
x = 1
v = 0
cycle = 0
total1 = 0
signal = [220, 180, 140, 100, 60, 20]

def checkSignal(_cycle, _total1, _x, _signal):
    if _cycle in signal:
        _total1 += _x * _cycle
        print(_cycle, _total1)
        _signal.pop()
    return(_total1, _signal)

with open('input10.txt', 'r') as handler:
    for line in handler:
        cycle += 1
        total1, signal = checkSignal(cycle, total1, x, signal)
        command = line[:4]
        if command == 'addx':
            v = (int(line[5:-1]))
            cycle += 1
        total1, signal = checkSignal(cycle, total1, x, signal)
        if command == 'addx':
            x += v
        print('Cycle:', cycle, '  x:', x, '  v:', v)

print()        
print('Total score puzzle 1:', total1)
# print('Total score puzzle 2:', total2)