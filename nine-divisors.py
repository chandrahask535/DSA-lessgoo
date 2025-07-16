import math

class Solution:
    def countNumbers(self, n):
        count = 0
        primes = []

        # Generate primes up to sqrt(n)
        limit = int(math.sqrt(n)) + 1
        is_prime = [True] * (limit + 1)

        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        # Case 1: Numbers of the form p^8
        for p in primes:
            if p ** 8 <= n:
                count += 1

        # Case 2: Numbers of the form p1^2 * p2^2 where p1 ≠ p2
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                val = (primes[i] ** 2) * (primes[j] ** 2)
                if val <= n:
                    count += 1
                else:
                    break

        return count

if __name__ == "__main__":
    n = int(input())  # User enters value like 100
    sol = Solution()
    print(sol.countNumbers(n))

