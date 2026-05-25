def isPalindrome(s: str) -> bool:
    alpha_s = [a.lower() for a in s if a.isalnum()]
    return alpha_s == alpha_s[::-1]

print(isPalindrome("Was it a car or a cat I saw?"))