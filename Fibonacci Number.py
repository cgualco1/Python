'''Function to calculate the n-th value of the Fibonacci sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,....'''
from functools import lru_cache
@lru_cache(maxsize = 1000)
def fib(n):
    #check for the base case
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    
    
def main():
    index = int(input('Enter a Fibonacci index: '))
    result = fib(index)
    print (f'The Fibonacci number is: {result}')
    
if __name__ == "__main__":
    main()