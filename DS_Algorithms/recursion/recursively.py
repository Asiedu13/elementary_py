from time import sleep

# countdown 
# def countDown(n):
#     timer = n
    
#     for i in range(timer):
#         print(timer)
#         timer -= 1
#         sleep(1)
#     print('Done!!!')
    
# countdown with recursion
def countDown(n):
    sleep(1)
    print(n)
    if n <= 0:
        print("Done!!!")
    else:
        countDown(n - 1)

def factorial(number):
    if number == 1:
        print('Done')
        return 1
    else:
        return number * factorial(number - 1)

def sum(arr):
    print(arr)
    
    if len(arr) <= 1: 
        return arr[0]

    else:
        return arr[0] + sum(arr[1 : len(arr)])
    
def reversal(string):
    if len(string) <= 1:
        return string
    return reversal(string[1:len(string)]) +  string[0]

def counting_x(string, count=0):
    if len(string) <= 0:
        return count
    else:    
        return counting_x(string[1 : len(string)], count + 1 if string[0] == 'x' else count )
if __name__ == '__main__':
    # countDown(10)
    # print(factorial(4))
    # print(sum([11, 3, 4, 5]))
    # print(reversal('Prince'))
    print(counting_x('examine the thought of xmas'))