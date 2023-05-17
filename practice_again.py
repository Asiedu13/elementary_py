def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n - 1) + fib(n - 2)

# Enhanced fib

def e_fib(n:int, memo:dict):
    # set the base case
    if n == 0 or n == 1:
        return n
    
    # Check if the value has not already been cached
    if not memo.get():
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
    
        

if __name__ == "__main__":
    print(fib(10))
    