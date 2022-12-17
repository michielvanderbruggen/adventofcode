

nr = 0
monkeys = []
input = []
rounds = 20

class monk():
    def __init__(self, name_) -> None:
        self.name = name_
        self.items = []
        self.operation = ''
        self.test = 0
        self.true = 0
        self.false = 0
        self.inspected = 0
    
    def inspect(self):
        old = int(self.items.pop())
        new = int(eval(self.operation)/3)
        print('Old:',old, 'New:', new)
        if new % int(self.test) == 0:
            print('True, throw to monkey', self.true)
            monkeys[int(self.true)].items.append(new)
        else:
            print('False, throw to monkey', self.false)
            monkeys[int(self.false)].items.append(new)
        self.inspected += 1


with open('input11.txt', 'r') as handler:
    for line in handler:
        input.append(line)

for i in range(len(input)):
    line = input[i]
    if 'Monkey' in input[i]:
        monkeys.append(monk(nr))
        print('monkey', nr)
        i += 1
        #  li = list(string.split(" "))
        monkeys[nr].items = list(input[i][input[i].find(':')+2:-1].split(', '))
        print(monkeys[nr].items)
        i += 1
        monkeys[nr].operation = input[i][input[i].find('=')+2:-1]
        print(monkeys[nr].operation)
        i += 1
        monkeys[nr].test = input[i][input[i].find('by')+3:-1]
        print(monkeys[nr].test)   
        i += 1
        monkeys[nr].true = input[i][input[i].find('monkey')+7:-1]
        print(monkeys[nr].true)
        i += 1
        monkeys[nr].false = input[i][input[i].find('monkey')+7:-1]
        print(monkeys[nr].false)        
        nr += 1

for round in range(rounds):
    print('##### Round', round,'#####')
    for monkeynr in range(nr):
        for i in range(len(monkeys[monkeynr].items)):
            print()
            print('Inspect monkey', monkeynr)
            monkeys[monkeynr].inspect()

for monkeynr in range(nr):
    print()
    print('Items monkey', monkeynr)
    print(monkeys[monkeynr].items)

topmonkeys = {}
for monkeynr in range(nr):
    print()
    print('Number of inspected items monkey', monkeynr)
    print(monkeys[monkeynr].inspected)
    topmonkeys[monkeynr] = monkeys[monkeynr].inspected


top = dict(sorted(topmonkeys.items(), key=lambda item: item[1]))
total1 = top[list(top)[-1]] * top[list(top)[-2]]

print()        
print('Total score puzzle 1:', total1)
# print('Total score puzzle 2:', total2)