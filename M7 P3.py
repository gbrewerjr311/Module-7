#Greg Brewer
# 5/28/2023
# Problem 3 Multiply list number

def multiplyListNumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
numbers = [5, 2, 7, -1]
result = multiplyListNumbers(numbers)
print(f"The multiplication of all the numbers in the list is: {result}")


