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

if __name__ == '__main__':
    # countDown(10)
    print(factorial(4))
  