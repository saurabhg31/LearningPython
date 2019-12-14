# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:10:27 2015
Python 2.7 code run on Ubuntu 14.04 LTS 64-bit

##### Program to test a very intuitive theory of primality, put forward by Saurabh Ghosh, only to break his hopes- prove it wrong !

Coded by Souvik Parial, 7th Semester
Department of Computer Science & Engineering,
Dibrugarh University

Contact: souvikparial@gmail.com

"""

from math import sqrt


limit = 10000       # Use a limit
prime = []          # prime is a list wher i will store all prime numbers upto a certain limit


for i in range(limit):      # store all integers from 0 to (limit-1) in the list
    prime.append(i)

prime.remove(0)     # prime doesn't contain 0 and 1
prime.remove(1)
    

for i in range(0,int(sqrt(limit)+1)):      # remove mulitples of each integer present in prime, only the primes to remain in the list
    a = 2 * prime[i]
    while(a<=limit):
        if prime.__contains__(a):
            prime.remove(a)
        a = a + prime[i]
        
print '\nAll primes upto {} are: \n'.format(limit), prime, '\n\n'


sum_list = [2, 3]


sum = 2+3           # initial sum = 2 + 3
increment = 2       # initial increment for 2 and 3


k = 2               # index of first number to be added, prime[2] = 5


while sum <= limit:
    number = sum + increment
    print prime.__contains__(number), 'for', number, '---> ', sum_list,'\n'
    
    if increment == 2:
        increment = 3
    elif increment == 3:
        increment =2
    
    next_number = prime[k]
    sum = sum + next_number
    sum_list.append(next_number)
    k = k + 1
