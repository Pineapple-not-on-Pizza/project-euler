import math

number = 23

primes = [2, 3, 5]

def primeChecker(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if number % i == 0:
            return False
    return True

if primeChecker(number):
    

    number += 2