class StringUtils:
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

print(StringUtils.is_palindrome("deed"))   # Output: True
print(StringUtils.is_palindrome("python")) # Output: False
