import os
import sys
import math

divisors = []

def formatNumber(number):
    return "{:,.0f}".format(number)

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def read_until_first_space_from_end(file_path, separator, encoding):
    chars = ''
    position = -2
    file = open(file_path, 'rb')
    # Move to the end of the file & seek
    while chars.count(separator) != 2:
        try:
            file.seek(position, 2)
            chars = file.read().decode(encoding)
            position -= 1
        except OSError:
            # Reached beginning of file 
            break
    return chars.strip()

def logFileCheck(filename = "primeNumbers.log", separator = ' ', encoding = 'utf-8'):
    if not os.path.exists(filename):
        raise Exception(" ".join(["File:", filename, "not present!"]))
    lastPrime = read_until_first_space_from_end(filename, separator, encoding)
    if lastPrime.isdigit():
        lastPrime = int(lastPrime)
    return lastPrime

def isPrime(x, f=2):
    if x == 2 or x == 3:
        return True
    elif x < 2:
        return False
    elif x > 2:
        while f <= math.ceil(math.sqrt(x)):
            if x % f == 0:
                # print("\n", x, " is divisible by ", f, "\n")
                try:
                    divisors.index(f)
                except (ValueError, IndexError):
                    divisors.append(f)
                return False
            else:
                f += 1
    return (x % f)

def arePrimes(numbers):
    notPrimes = []
    primes = 0
    for number in numbers:
        if isPrime(number):
            primes += 1
        else:
            notPrimes.append(number)
    print(primes, "Primes found:\n")
    return notPrimes

def main():
    # environment vars
    separator = " "
    encoding = 'utf-8'
    filename = "primeNumbers.log"

    # code logic
    lastLoggedPrime = logFileCheck(filename, separator, encoding) # doing log file checks
    file = open(filename, 'a') # opening the file in append mode (file must be present)
    print('\nProgram to calculate prime numbers in a given range (includes the range values itself).\n')
    if lastLoggedPrime:
        print('Last recorded prime: ', formatNumber(lastLoggedPrime))
        limit_low = lastLoggedPrime + 2
        print('Lower limit set to: ', lastLoggedPrime)
    else:
        limit_low = int(input("Enter lower limit of range: "))
    limit_high = int(input("Enter upper limit of range: "))
    primeCount = 0
    # primes = []
    lowVal = limit_low
    print("\nPrime numbers are as follows:\n")
    while limit_low <= limit_high:
        if isPrime(limit_low):
            primeCount += 1
            # primes.append(limit_low)
            print(formatNumber(limit_low), end=" ")
            file.write(str(limit_low) + separator)
        limit_low += 1
    print("\n")
    print(formatNumber(primeCount), " primes found in range [",formatNumber(lowVal),",",formatNumber(limit_high),"]\n")
    print('Done.')
    print("Divisors in range: \n")
    print(divisors)
    reply = input("\nCheck if all divisors are prime ? (yes/no): ")
    if reply == 'yes':
        print("\nChecking if all divisors are prime...\n")
        nonPrimeDivisors = arePrimes(divisors)
        print("Divisors that are not primes:\n")
        print(nonPrimeDivisors)
    if divisors:
        print("\nMax Divisor:",divisors[-1],"\n")
    else:
        print("\nNo Divisors found!\n")
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
