# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
# Functions can return a value
def mean(number):
    average = 0
    for x in number :
        average += x
    average= average/len(number)
    return average 


# You can save the value that is returned
average = [2,5,2]
print(mean(average))

# You can also just print the return value of a function
#print(square(2))
#print(square(3))