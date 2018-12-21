#!/usr/bin/env python3

import sys
import time


""" A simple module that will contain all the methods to run the various
fibonacci sequence methods. Each method is designed to return the nth
fibonacci number.
"""

# Global constants for the zeroeth and first Fibonacci Numbers
FIB_0 = 1
FIB_1 = 1


""" Serial implementation of the fibonacci sequence.

Returns the nth fibnacci number and the runtime as tuple (fib, t)

"""
def fibonacci_serial(n):
    fib_curr = None
    fib_prev = None

    t1 = time.time()
    for i in range(0, n):
        # Handle base cases
        if i == 0:
            fib_curr = FIB_0
        elif i == 1:
            fib_prev = fib_curr
            fib_curr = FIB_1
        else:
            # Save the current (n-i)th Fibonacci number in a temp var
            fib_temp = fib_curr

            # Add the previous (n-i-1)th Fibonacci number to the current
            # (n-i)th Fibonacci number to make the new nth Fibonacci number
            fib_curr += fib_prev

            # Make the (n-i)th Fibonacci number the prev Fibonacci number
            fib_prev = fib_temp

    t2 = time.time()

    t = t2 - t1

    return (fib_curr, t)

def run_serial(N):
    value = False

    if value:
        print("  N \t  Time (s) \t  Fib(N)")
        print("----- \t ---------- \t ---------")
    else:
        print("  N \t  Time (s)")
        print("----- \t ----------")
    for n in N:
        fib, t = fibonacci_serial(n)

        if value:
            print("{:.0e} \t {:10.4e} \t {:d}".format(n, t, fib))
        else:
            print("{:.0e} \t {:10.4e}".format(n, t))


if __name__ == '__main__':
    value = False

    if (len(sys.argv) == 0) or (sys.argv[1] == "help"):
        print("Usage: fib n0 n1 ... n")
    else:
        N = [int(sys.argv[i]) for i in range(1, len(sys.argv))]
        run_serial(N)
