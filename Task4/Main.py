import json


def numberToRoman(num):
    number = ''
    for digit in intToRomanDict.keys():
        number += num // digit * intToRomanDict[digit]
        num %= digit
    return number


def romanToNumber(roman):
    number = 0
    prev = 'M'
    for i in range(len(roman)):
        if roman[i] in romanToIntDict:
            if romanToIntDict[prev] < romanToIntDict[roman[i]]:
                number -= romanToIntDict[prev]*2
                number += romanToIntDict[roman[i]]
            else:
                number += romanToIntDict[roman[i]]
        prev = roman[i]
    return number


f = open("resources/data.json", "r")
romanToIntDict = json.load(f)
intToRomanDict = {value: key for key, value in romanToIntDict.items()}
f.close()

f = open("resources/in.txt", "r")
romans = f.readline().split(" ")
numbers = f.readline().split(" ")
f.close()

f = open("resources/out.txt", "w")
for roman in romans:
    f.write(str(romanToNumber(roman)) + " ")
f.write("\n")
for number in numbers:
    f.write(numberToRoman(int(number)) + " ")
f.close()
