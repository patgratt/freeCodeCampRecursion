def findBinary(dec: int, res: str) -> str:
    # base case, there's no more division to do
    if dec == 0:
        return res
    
    res = str(dec % 2) + res

    return findBinary(dec // 2, res)

print(findBinary(233, ""))
