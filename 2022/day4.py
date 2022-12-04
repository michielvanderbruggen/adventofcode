
section1 = []
section2 = []
total1 = 0
total2 = 0

with open('input4.txt', 'r') as handler:
    for line in handler:
        sect1 = line[:line.find(',')]
        sect1b = int(sect1[:sect1.find('-')])
        sect1e = int(sect1[sect1.find('-')+1:])+1
        sect2 = line[line.find(',')+1:-1]
        sect2b = int(sect2[:sect2.find('-')])
        sect2e = int(sect2[sect2.find('-')+1:])+1

        for i in range(sect1b, sect1e):
            section1.append(i)
        for i in range(sect2b, sect2e):
            section2.append(i)

        tot = [x for x in section1 or x in section2 if x in section1 and x in section2]
        if tot == section1 or tot == section2:
            total1 += 1

        tot2 = [x for x in section1 + section2 if x in section1 and x in section2]
        if len(tot2) > 0:
            total2 += 1

        section1.clear()
        section2.clear()

print('Total score puzzle 1:', total1)
print('Total score puzzle 2:', total2)