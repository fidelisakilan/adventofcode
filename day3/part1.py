file = open("input.txt", "r")
sum = 0
doc = file.read()

numberIndex = 0
while numberIndex < len(doc):
    prevIndex = numberIndex
    if doc[numberIndex : numberIndex + 4] == "mul(":
        firstNumber = ""
        secondNumber = ""
        numberIndex += 4
        while doc[numberIndex] >= "0" and doc[numberIndex] <= "9":
            firstNumber += doc[numberIndex]
            numberIndex += 1
        if doc[numberIndex] == ",":
            numberIndex += 1
            while doc[numberIndex] >= "0" and doc[numberIndex] <= "9":
                secondNumber += doc[numberIndex]
                numberIndex += 1
        if doc[numberIndex] == ")":
            sum += int(firstNumber) * int(secondNumber)
            numberIndex += 1
            # print(doc[prevIndex:numberIndex])
            continue
    numberIndex = prevIndex + 1
print(sum)
