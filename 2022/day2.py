totalscore1 = 0
totalscore2 = 0

with open('input2.txt', 'r') as handler:
    for line in handler:
        match line[:3]:
            case 'A X': score = 1+3
            case 'A Y': score = 2+6
            case 'A Z': score = 3+0
            case 'B X': score = 1+0
            case 'B Y': score = 2+3
            case 'B Z': score = 3+6
            case 'C X': score = 1+6
            case 'C Y': score = 2+0
            case 'C Z': score = 3+3
        totalscore1 += score
        match line[:3]:
            case 'A X': score2 = 3+0
            case 'A Y': score2 = 1+3
            case 'A Z': score2 = 2+6
            case 'B X': score2 = 1+0
            case 'B Y': score2 = 2+3
            case 'B Z': score2 = 3+6
            case 'C X': score2 = 2+0
            case 'C Y': score2 = 3+3
            case 'C Z': score2 = 1+6
        totalscore2 += score2
print('Total score puzzle 1:', totalscore1)
print('Total score puzzle 2:', totalscore2)