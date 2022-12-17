# python program to print all the unique numbers in a given list
numbers = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_numbers = []

for number in numbers :
    if number not in unique_numbers :
        unique_numbers.append(number)
        
print(unique_numbers)

# this is how the program works
# the list is provided with the input numbers and duplicates
# first step is to loop through the original list, and the later steps are to compare the value present in the unique list to the original list to check for any duplicates, and once that's done, the next step is to append the non repeating element in the unique list.
# finally, print the output of the program.
