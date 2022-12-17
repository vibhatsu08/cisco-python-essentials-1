# python program to sort a list of numbers using the bubble sort technique
# taking input for the list
length = int(input("Enter the length of the list: "))
numbers = []
for i in range (length) :
    number = int(input("Enter a random number: "))
    numbers.append(number)

# now sorting the list
swapped = True
while swapped :
    swapped = False
    for i in range (length-1) :
        if (numbers[i] > numbers[i+1]) :
            swapped = True
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            
print(numbers)

# this is how the above program works
# the input list is given.
# a dummy variable is set to True, True means that a swap has taken place, and when it's set to False, it means that a swap hasn't taken place.
# So the initial value is set to True, to get it in the while loop, and keep checking and swapping the numbers if a swap is possible.
# Once the process is completed, the list of numbers is displayed.

# the python method used to sort the list is:
# numbers.sort()

# the method to reverse a given list is:
# numbers.reverse()