import os
import sys
import math
import threading

divisors = []
quickTestsAvailableFor = [2, 3, 5, 7, 11] # values within must always be in ascending order

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
    file.close()
    return chars.strip()

def logFileCheck(filename = "primeNumbers.log", separator = ' ', encoding = 'utf-8'):
    if not os.path.exists(filename):
        raise Exception(" ".join(["File:", filename, "not present!"]))
    lastPrime = read_until_first_space_from_end(filename, separator, encoding)
    if lastPrime.isdigit():
        lastPrime = int(lastPrime)
    return lastPrime

def sumOfDigits(num):
    sum = 0
    i = 1
    num = str(num)
    while i < len(num)+1:
        sum += int(num[0-i])
        i += 1
    return sum

"""
    quickPrimeChecks: num will not be prime if this function return False for num passed as argument
    @param string/integer num
    @return boolean
"""
def quickPrimeChecks(num):
    num = str(num)
    if num[-1] == 5: # checking for 5
        divisors.append(5)
        return False
    if int(num[-1]) % 2 == 0: # checking for 2
        divisors.append(2)
        return False
    if sumOfDigits(num) % 3 == 0: # checking for 3
        divisors.append(3)
        return False
    # checking for 7
    tmpNum = int(num[0:-1])
    if (tmpNum - int(num[-1])) % 7 == 0:
        divisors.append(7)
        return False
    # checking for 11
    even_sum = odd_sum = 0
    for index, digit in enumerate(num):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if (odd_sum - even_sum) % 11 == 0:
        divisors.append(11)
        return False
    # TODO: add code to check for 13
    """
    To check if a large number is divisible by 13, use the following mathematical rule:
        1. Remove the last digit from the number.
        2. Subtract 9 times the last digit from the remaining number.
        3. Repeat the process with the result until the number is small enough to determine its divisibility by 13.
        
        Example: Check if 2028 is divisible by 13.

        1. Separate the last digit: 202 and 8.
        2. Calculate the new number: 202 - (9 X 8) = 202 = 130
        3. Repeat the process until result (130) is below 200.
        5. Check if the result is divisible by 13: 130 % 13 = 0 (remainder)
        conclusion: 2028 is divisible by 13.
    """
    return True

def isPrime(x, f=2):
    if x < 2:
        return False
    elif x > 2:
        digitsBasedCheck = quickPrimeChecks(x)
        if not digitsBasedCheck:
            return False
        while f <= math.floor(math.sqrt(x)):
            if len(str(x)) > 3 and (f < quickTestsAvailableFor[-1] and f in quickTestsAvailableFor):
                continue
            if x % f == 0:
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

def findPrimesInRangeViaThread(min, max, chunkname, separator = " "):
    file = open('fileChunks/' + chunkname, 'w')
    while min <= max:
        if isPrime(min):
            file.write(str(min) + separator)
        min += 1

def main():
    # environment vars
    separator = " "
    encoding = 'utf-8'
    filename = "primeNumbers.log"
    useMultipleThreads = False

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
    incrementSwitch = False
    print("\nPrime numbers are as follows:\n")
    if useMultipleThreads:
        # TODO: Add multithreading code
        threading.Thread(target=findPrimesInRangeViaThread, args=(limit_low, limit_high, 'c1.log'), name='Thread-1')
        threading.Thread(target=findPrimesInRangeViaThread, args=(limit_low, limit_high, 'c2.log'), name='Thread-2')
    else:
        while limit_low <= limit_high:
            if isPrime(limit_low):
                incrementSwitch = True
                primeCount += 1
                print(formatNumber(limit_low), end=" || ")
                file.write(str(limit_low) + separator)
            limit_low = limit_low + 2 if incrementSwitch else limit_low + 1
        file.close()
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
            print("The number is not prime.", "Divisible by:", divisors[-1], "\n\n", divisors[-1], "X", int(x/divisors[-1]), "=", x)
    elif ch == 2:
        main()
    else:
        print("Invalid choice input")

exit()
