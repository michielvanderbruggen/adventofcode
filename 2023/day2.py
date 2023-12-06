import re

puzzletotal = 0

pullpossible = False

def validatepull(pull):
    pulltotal = {'red': 0, 'green': 0, 'blue': 0}
    gamemax = {'red': 12, 'green': 13, 'blue': 14}
    colortotal = 0
    colors = ['red', 'green', 'blue']
    # print('Pull',pull)
    for color in colors:
        matches = re.findall(f'...{color}', pull)
        # print(f'Matches for {color}:', matches)
        for match in matches:
            colortotal = int(re.findall(r'\d+', match)[0])
            # print(f'Colortotal for {color} is: {colortotal}')
            pulltotal[color] = colortotal
        colortotal = 0
        if pulltotal[color] <= gamemax[color]:
            pullpossible = True
        else:
            pullpossible = False
            break
    # if pullpossible:
    #     print('Pull possible')
    # else:
    #     print('Pull not possible')
    return pullpossible

with open('input2.txt', 'r') as handler:
    for line in handler:
        # print('----------')
        # print(line)
        game = line[5:line.find(':')]
        pulls = line[line.find(':')+1:-1].split(';')
        for pull in pulls:
            pullpossible = validatepull(pull)
            if not pullpossible:
                break
        if pullpossible:
            # print('Gamepossible')
            puzzletotal += int(game)
        # else:
        #     print('Game not possible')

print('Part1:', puzzletotal)

puzzletotal = 0

def totalpull(pull):
    pulltotal = {'red': 0, 'green': 0, 'blue': 0}
    colortotal = 0
    colors = ['red', 'green', 'blue']
    print('Pull',pull)
    for color in colors:
        matches = re.findall(f'...{color}', pull)
        # print(f'Matches for {color}:', matches)
        for match in matches:
            colortotal = int(re.findall(r'\d+', match)[0])
            # print(f'Colortotal for {color} is: {colortotal}')
            pulltotal[color] = colortotal
        colortotal = 0
    return pulltotal

with open('input2.txt', 'r') as handler:
    for line in handler:
        gamemax = {'red': 0, 'green': 0, 'blue': 0}
        print('----------')
        print(line)
        game = line[5:line.find(':')]
        pulls = line[line.find(':')+1:-1].split(';')
        for pull in pulls:
            pulltotal = totalpull(pull)
            for color in pulltotal:
                if pulltotal[color] > gamemax[color]:
                    gamemax[color] = pulltotal[color]
        print('Gamemax:',gamemax)
        print('Score:', gamemax['red'] * gamemax['green'] * gamemax['blue'])
        puzzletotal += gamemax['red'] * gamemax['green'] * gamemax['blue']

print('Part2:', puzzletotal)