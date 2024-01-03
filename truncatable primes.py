import math
import time

foundPrimes = []
foundNumbers = []

finalNumber = 0

def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        try:
            for i in range(2, math.ceil(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        except:
            print("Invalid input:", n)

for i in range(1, 799999, 2):
    if isPrime(i):
        foundPrimes.append(i)

for i in foundPrimes:
    tempNumber = str(i)

    while len(tempNumber) >= 2:
        tempNumber = tempNumber[:-1]
        if not isPrime(int(tempNumber)):
            break
    else:
        tempNumber = str(i)

        while len(tempNumber) >= 2:
            tempNumber = tempNumber[1:]
            if not isPrime(int(tempNumber)):
                break
        else:
            foundNumbers.append(i)

print(foundNumbers)

for i in foundNumbers:
    if len(str(i)) >=2:
        finalNumber += i

print(finalNumber)