"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

m = 1
n = 10

# Setup the list of divisors
# We put this list in reverse order so that the largest divisor always comes
# first
divisors = range(m, n + 1)
divisors.reverse()

# Setup the multiples data struct
multiples = dict.fromkeys(divisors)
for i in

while True:
    largest =
    for x in divisors:
        print x
    break
