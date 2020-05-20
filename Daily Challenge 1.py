#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


numbers = [10,15,3,8,9,1,16,15,2,7,10]
num = numbers.copy()
k = int(input("Enter number you want to check sum of: "))
count = range(len(num))
for number in num:

    for i in count:
        num_to_add = numbers[i]

        sum = num_to_add + number
        if sum == k:
            print(True)
            print(f"Sum of {num_to_add} + {number} is equal to {k}")
