#Greg Brewer
# 5/28/2023
# Problem 4 get unique elements

def getUniqueElements(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
def getUniqueElements(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
numbers = [1, 3, 3, 3, 6, 2, 3, 5]
unique_elements = getUniqueElements(numbers)
print(f"The unique elements in the list are: {unique_elements}")


