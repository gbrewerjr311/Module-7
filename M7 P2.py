#Greg Brewer
# 5/28/2023
# Problem 2 check number in range

def checkNumberInRange(number):
    if number in range(1, 10):
        print(f"The number {number} is in the range.")
    else:
        print(f"The number {number} is not in the range.")
checkNumberInRange(5)
checkNumberInRange(12)
