# python program to print the fibonacci sequence of numbers using recursion.
def printFibonacci(number) :
    if (number <= 0) :
        return 0
    elif (number == 1) :
        return 1
    else :
        return printFibonacci(number-1) + printFibonacci(number-2)

print(printFibonacci(10))