"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from lib import is_palindrome

min = 1000
max = 9999

largest = 0
for a in xrange(min, max):
    for b in xrange(min, max):
        n = a * b
        if (is_palindrome(n) and n > largest):
            print("palindrome %s x %s = %s" % (a, b, n))
            largest = n

print largest
