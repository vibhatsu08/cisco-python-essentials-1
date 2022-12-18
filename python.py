# python program to calculate the BMI of a person based on their weight and height.
# the function takes in two parameters, height and weight
def calculateBMI (height, weight):
    # returns the weight/height**2
    return ((weight)/(height)**2)

print(calculateBMI(1.72, 74))