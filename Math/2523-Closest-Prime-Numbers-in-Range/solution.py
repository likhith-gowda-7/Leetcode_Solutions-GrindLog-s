class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes to find primes
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
        
        # Collect primes in range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        # If less than 2 primes, return [-1, -1]
        if len(primes) < 2:
            return [-1, -1]
        
        # Find closest pair of primes
        min_diff = float("inf")
        ans1, ans2 = -1, -1
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                ans1, ans2 = primes[i - 1], primes[i]
        
        return [ans1, ans2]
