numbers = ''
letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
letterreplace = {'one': 'o1ne', 'two': 't2wo', 'three': 't3hree', 'four': 'f4our','five': 'f5ive', 'six': 's6ix', 'seven': 's7even', 'eight': 'e8ight', 'nine': 'n9ine'}
total = 0

with open('input1.txt', 'r') as handler:
    for line in handler:
        print('----------')
        print(line)

        # part 2
        for letter in letters:
            line = line.replace(letter, str(letterreplace[letter]))
        print(line)
        
        for char in line:
            if char.isdigit():
                numbers += char
            # part 2

        number1 = numbers[0]
        number2 = numbers[len(numbers)-1]
        value = int(number1 + number2)
        print(value)
        total += value
        numbers = ''


print('total is:', total)