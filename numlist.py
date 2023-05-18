firstNum = 52
secondNum = 10
if firstNum > secondNum:
    #Flip numbers so first < second
    x = secondNum
    secondNum = firstNum
    firstNum = x

outputStr = ""
for i in range(firstNum,secondNum+1):
    outputStr = outputStr + f"{i},"
outputStr = outputStr[:-1] #remove last comma

print(outputStr)