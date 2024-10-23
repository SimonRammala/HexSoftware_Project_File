#function used to generate the fibonacci sequence
def fibonacci(n):

    #used to return the first two values of the fibonacci sequence
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    
    #used to return the nth value of the fibonacci sequence
    return fibonacci(n -1) + fibonacci(n - 2)

#used to print the first 20 values of the fibonacci sequence
for i in range(1, 20):
     print(fibonacci(i))
    