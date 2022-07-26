input1 = "hello"

def reverseString(str: input) -> str:
    # base case, simplest case, an empty string reversed must still just be 
    # an empty string
    if input == "":
        return ""
    
    return reverseString(input[1: ]) + input[0]

print(reverseString(input1))