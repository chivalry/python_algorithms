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
    return word[0] == word[-1] and is_palindrome(word[1:-1])


def is_anagram(word, candidate):
    """Return `True` if the words are anagrams of each other."""
    normalized_word = sorted(tuple(word.lower()))
    normalized_candidate = sorted(tuple(candidate.lower()))
    return normalized_word == normalized_candidate and word.lower() != candidate.lower()


def is_prime(num: int) -> bool:
    """Uses early prime facts to determine primacy more quickly."""
    if not isinstance(num, int) or num <= 0:
        raise ValueError('Error: Only positive integers can be prime')
    if num in [2, 3, 5, 7]:
        return True
    if num < 2 or num % 2 == 0 or num == 9:
        return False
    if num % 3 == 0:
        return False
    root = int(num ** 0.5)
    fact = 5
    while fact <= root:
        if num % fact == 0 or num % (fact + 2) == 0:
            return False
        fact += 6
    return True

def bubble_sort(lst):
    for pass_num in range(len(lst) - 1, 0, -1):
        for i in range(pass_num):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


def short_bubble_sort(lst):
    exchanges = True
    pass_num = len(lst) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if lst[i] > lst[i + 1]:
                exchanges = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        pass_num -= 1


def selection_sort(lst):
    for slot in range(len(lst) - 1, 0, -1):
        max_pos = 0
        for location in range(1, slot + 1):
            if lst[location] > lst[max_pos]:
                max_pos = location
        lst[slot], lst[max_pos] = lst[max_pos], lst[slot]


def insertion_sort(lst):
    for i in range(1, len(lst)):
        curr = lst[i]
        pos = i
        while pos > 0 and lst[pos - 1] > curr:
            lst[pos] = lst[pos - 1]
            pos = pos - 1
        lst[pos] = curr


def shell_sort(lst):
    gap:memoryview = len(lst) // 2
    while gap > 0:
        for start in range(gap):
            for i in range(start + gap, len(lst), gap):
                curr = lst[i]
                pos = i
                while pos >= gap and lst[pos - gap] > curr:
                    lst[pos] = lst[pos - gap]
                    pos -= gap
                lst[pos] = curr
        gap //= 2


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


def quick_sort(lst, first=0, last=None):
    if not last:
        quick_sort(lst, first, len(lst) - 1)
        return
    if first >= last:
        return
    pivot = lst[first]
    left = first + 1
    right = last
    while True:
        while left <= right and lst[left] <= pivot:
            left += 1
        while lst[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        lst[left], lst[right] = lst[right], lst[left]
    lst[first], lst[right] = lst[right], lst[first]
    split = right
    quick_sort(lst, first, split - 1)
    quick_sort(lst, split + 1, last)


if __name__ == '__main__':
    for i in range(1, 26):
        print(i, is_prime(i))
