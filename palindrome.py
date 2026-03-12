def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome.
    Ignores case and considers only alphanumeric characters.
    """
    normalized = ''.join(ch.lower() for ch in s if ch.isalnum())
    return normalized == normalized[::-1]

if __name__ == '__main__':
    user_input = input("Enter a word or phrase: ")
    if is_palindrome(user_input):
        print("It is a palindrome!")
    else:
        print("It is not a palindrome.")