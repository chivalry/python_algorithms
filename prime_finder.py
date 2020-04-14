from algorithms import is_prime


class PrimeFinder:
    """A dynamic programming implementation of a prime finder."""

    def __init__(self):
        self.found_primes = []

    def is_prime(self, num: int) -> bool:
        """Uses early prime facts to determine primacy more quickly."""
        if not isinstance(num, int) or num <= 0:
            raise ValueError('Error: Only positive integers can be prime')
        if self.found_primes and num in self.found_primes:
            return True
        if self.found_primes and num < max(self.found_primes):
            return False
        is_p = is_prime(num)
        if is_p:
            self.found_primes.append(num)
        return is_p


if __name__ == '__main__':
    prime_finder = PrimeFinder()
    for i in range(1, 101):
        prime_finder.is_prime(i)
    print(prime_finder.found_primes)
