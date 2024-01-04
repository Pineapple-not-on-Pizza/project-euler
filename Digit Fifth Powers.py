allFound = []
finalNum = 0

for i in range(1, 1_000_000):
    num = int(i)
    currentNumber = 0
    length = len(str(i))
    
    for l in range(0, length):
        currentNumber += int(str(num)[l])**5
        
    if int(currentNumber) == num:
        allFound.append(int(i))
        
print(allFound)

for i in allFound:
    finalNum += int(i)
    
print(finalNum - 1)