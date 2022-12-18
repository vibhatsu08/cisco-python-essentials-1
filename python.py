# python program to print the factorial of a given number.
def printFactorial (number) :
    product = 1
    for digit in range (1, number+1):
        product *= digit
    return product
    
print (printFactorial(0))