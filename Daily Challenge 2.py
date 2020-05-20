class Point():

    def move(self):
        print(f"This is move def {self}")
    def draw(self):
        print("this is draw def")


#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers
# in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

numbers = [7,6,8,3,5] #make it dynamic
i = len(numbers)
output = []
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

for number in numbers:
    new_list = numbers.copy()
    new_list.remove(number)
    output.append(multiplyList(new_list))
print(output)



