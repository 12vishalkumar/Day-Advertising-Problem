import math
import os
import random
import re
import sys

# Complete the 'viralAdvertising' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

def viralAdvertising(n):
    # Write your code here
    S = 5
    cum = 0
    for i in range(1, n+1):
        L = int(S/2)
        S = L*3
        cum += L
    return cum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()