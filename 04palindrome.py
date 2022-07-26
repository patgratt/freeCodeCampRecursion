# palindrome = word that is spelled sane forwards and backwards

input1 = "racecar" #true

def isPalindrome(s: str) -> str:
    # base case, simplest easy condition, len=0 or 1
    if len(s) == 0 or len(s) == 1:
        return True

    # if the first letter and last letter are equal
    if s[0] == s[-1]:
        # recursively use function on a string without the first and last lettter
        return isPalindrome(s[1:-1])

    # additional base case where we don't have a palindrome
    return False

print(isPalindrome(input1))
