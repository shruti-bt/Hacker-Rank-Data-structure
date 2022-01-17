

import math
import os
import random
import re
import sys

def reverseArray(a):
    # Write your code here
    return a[::-1]
    
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    res = reverseArray(arr)
    print(res)


