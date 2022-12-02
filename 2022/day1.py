
totElf = 0
countElf = 0
topElf = 0
topScore = 0
topList = {}

with open('input1.txt', 'r') as handler:
    for line in handler:
        if line != "\n":
            cal = int(line)
            totElf += cal
        else:
            topList[countElf] = totElf
            countElf += 1
            totElf = 0

for elf in range(len(topList)):
    if topList[elf] > topScore:
        topScore = topList[elf]
        topElf = elf

print('Puzzle 1:')
print(topScore)

top3 = dict(sorted(topList.items(), key=lambda item: item[1]))
print('Puzzle 2:')
print(top3[list(top3)[-1]] + top3[list(top3)[-2]] + top3[list(top3)[-3]])