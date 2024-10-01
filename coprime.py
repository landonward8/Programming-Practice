'''
    CoPrime.py

    Generates a graph of the m x n co-primes
    
    [Landon Ward]
'''

import sys
import math

'''
generates the co-primes in an m x n matrix
'''
def is_copime(a,b):
        while b!=0:
            a,b = b, a%b
        return a == 1

def coprimes(m, n):
    '''
    creates a list of size n each with
    each element initialized to None
    '''
    result = [None] * (m + 1)

    '''
    each element in the list is now a
    list of size m where each value
    is initialized to a space ' '
    '''
    for i in range(0,m+1):
        result[i] = ['^'] * (n + 1)

    '''
    Coprimes
    '''
    for i in range(1, m+1):
        for j in range(1, n+1):
            if is_copime(i, j) == 1:
                result[i][j] = '*'
    '''
    output the contents of result
    '''
    for x in result[::-1]:
        # x[:] is a list "slice"
        for y in x[:]:
            '''
            by putting a comma at the end, we prevent a newline
            '''
            print(y + ' ', end="")
            
        print()

# behaves like main() method

if __name__ == "__main__":
    # some error checking
    if len(sys.argv) != 3:
        print('Usage\n python CoPrime [int] [int]')
        quit()

    coprimes(int(sys.argv[1]), int(sys.argv[2]))
