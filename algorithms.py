def factorial(num: int) -> int:
    """Return the factorial of the given number."""
    if num < 0 or not isinstance(num, int):
        raise ValueError('Error: Only factorials of ints can be calculated')
    if num == 0:
        return 1
    return num * factorial(num - 1)


def gcd(a: int, b: int) -> int:
    """Return the greatest common denominator using Euclid's algorithm"""
    return a if b == 0 else gcd(b, a % b)


def is_palindrome(word):
    """Use recursion to return `True` if the word is a palindrome"""
    if len(word) in [0, 1]:
        return True
    return word[0] == word[-1] and is_palindrom(word[1:-1])


def is_anagram(word, candidate):
    """Return `True` if the words are anagrams of each other."""
    normalized_word = sorted(tuple(word.lower()))
    normalized_candidate = sorted(tuple(candidate.lower()))
    return normalized_word == normalized_candidate and word.lower() != candidate.lower()
