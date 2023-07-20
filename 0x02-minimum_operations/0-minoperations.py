#!/usr/bin/python3
'''A module for working with text files.
'''

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    :param n: an integer, the desired number of H characters
    :return: an integer, the fewest number of operations needed to achieve n H characters
    """
    if n <= 1:
        return 0
    num_operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            num_operations += divisor
            n /= divisor
        divisor += 1
    return num_operations
