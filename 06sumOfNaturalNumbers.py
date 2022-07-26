inputNum1 = 10

def recursiveSummation(inputNum: int) -> int:
    # base case
    if inputNum <= 1:
        return inputNum
    
    return inputNum + recursiveSummation(inputNum - 1)

print(recursiveSummation(inputNum1))