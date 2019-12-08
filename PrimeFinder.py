import os
import sys
import math

divisors = []

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def isPrime(x, f=2):
    if x == 2 or x == 3:
        return True
    elif x < 2:
        return False
    elif x > 2:
        while f <= math.ceil(math.sqrt(x)):
            if x % f == 0:
                print("\n", x, " is divisible by ", f, "\n")
                try:
                    divisors.index(f)
                except (ValueError, IndexError):
                    divisors.append(f)
                return False
            else:
                f += 1
    return (x % f)

# TODO: check why this method detects list of primes as not prime, called from line 63
def arePrimes(numbers):
    notPrimes = []
    primes = 0
    for number in numbers:
        # print("\nChecking if",number,"is prime")
        if isPrime(number):
            primes += 1
        else:
            notPrimes.append(number)
    print(primes, "Primes found:\n")
    return notPrimes

def main():
    print('Program to calculate prime numbers in a given range (includes the range values itself).\n')
    limit_low = int(input("Enter lower limit of range: "))
    limit_high = int(input("Enter upper limit of range: "))
    primeCount = 0
    primes = []
    lowVal = limit_low
    while limit_low <= limit_high:
        if isPrime(limit_low):
            primeCount += 1
            primes.append(limit_low)
        limit_low += 1
    print("Primes: \n")
    print(primes)
    print("\n",primeCount, " primes found in range [",lowVal,",",limit_high,"]\n")
    print("Divisors in range: \n")
    print(divisors)
    reply = input("\nCheck if all divisors are prime ? (yes/no): ")
    if reply == 'yes':
        print("\nChecking if all divisors are prime...\n")
        # if arePrimes(divisors):
        #     print("All divisors are prime.")
        # else:
        #     print("All divisors are not prime.")
        nonPrimeDivisors = arePrimes(divisors)
        print("Divisors that are not primes:\n")
        print(nonPrimeDivisors)
    return True


while int(input("\nRun prime finding program ?\n1. Yes, 0. No\n")):
    ch = int(input("1. Detect if a number is prime\n2. Find prime numbers within a given range\n"))
    if ch == 1:
        x = input("Enter test number: ")
        while isInt(x) == False:
            print("\nInvalid integer. Please enter again...\n")
            x = input("Enter test number: ")
            if isInt(x) == False:
                print("Repeated invalid data entered. Re-running program...")
                os.execl(sys.executable, sys.executable, *sys.argv)
        x = int(x)
        if isPrime(x):
            print("The number is prime\n")
        else:
            print("The number is not prime\n")
    elif ch == 2:
        main()
    else:
        print("Invalid choice input")
exit()
