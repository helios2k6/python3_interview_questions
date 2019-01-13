
def urlify(s, trueLength):
    numSpaces = 0
    for i in range(trueLength):
        if s[i] == ' ':
            numSpaces += 1
    
    cursor = (numSpaces * 2) + trueLength
    for i in reversed(range(trueLength)):
        if s[i] == ' ':
            s[cursor - 1] = '0'
            s[cursor - 2] = '2'
            s[cursor - 3] = '%'
            cursor -= 3
        else:
            s[cursor - 1] = s[i]
            cursor -= 1

test1 = list("Mr Smith  ")
urlify(test1, 8)
print(test1)