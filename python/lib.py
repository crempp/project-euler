"""
A library of functions created for Project Euler problems
"""

def enumerate_odd(m, n):
    '''
    Enumerate the odd integers from m to n
    '''
    if 0 == m % 2: i = m - 1
    else: i = m - 2
    while i <= n:
        i += 2
        yield i

def enumerate_multiples(x, n):
    '''
    Enumerate the multiples of x up to n
    '''
    mult = 2
    z = x
    while z <= n:
        yield z
        z = mult * x
        mult += 1

def eratosthenes(n):
    '''
    Use the Sieve of Eratosthenes to generate a list of primes from 2 to n
    '''
    p = 2
    integers = range(p, n)
    primes = [p]
    while len(integers) > 0:
        for z in enumerate_multiples(p, n):
            try:
                integers.remove(z)
            except:
                pass
        # The first element in the sieved list is a prime
        p = integers.pop(0)
        primes.append(p)
    return primes

def enumerate_primes(n):
    '''
    Use the Sieve of Eratosthenes to enumerate a list of primes from 2 to n
    '''
    p = 2
    integers = range(p, n)
    while len(integers) > 0:
        yield p
        # TODO: Optimize the following loop
        for z in enumerate_multiples(p, n):
            try:
                integers.remove(z)
            except:
                pass
        # The first element in the sieved list is a prime
        p = integers.pop(0)

def factorize(N):
    '''
    Factorize the integer N
    '''
    import math
    factorization = {}
    sqrtN = (int)(math.ceil(math.sqrt(N)))
    for x in enumerate_primes(sqrtN):
        r = N % x
        if (0 == r):
            N = N / x
            if x in factorization.keys():
                factorization[x] += 1
            else:
                factorization[x] = 1
        if 1 == N:
            break
    return factorization

def is_palindrome(n):
    '''
    Check if the integer/string/list n is palindromic
    '''
    if type(n) is int:
        n = list(str(n))
    elif type(n) is str:
        n = list(n)
    elif type(n) is not list:
        # TODO: change this to TypeException
        raise Exception()

    if len(n) % 2 is not 0:
        return False

    while len(n) > 0:
        i = n.pop(0)
        j = n.pop(-1)

        if i is not j:
            return False

    return True
