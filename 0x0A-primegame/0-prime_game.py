#!/usr/bin/python3
""" Prime Game Module """


def sort_primes(n):
    """Sort prime numbers up to n using Sieve of Eratosthenes."""

    primes = [True for _ in range(n + 1)]
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = primes[1] = False
    return primes


def isWinner(x, nums):
    """
    x is the number of rounds
    nums is an array of n numbers
    should return the name of the player that won the most rounds
    """
    if x < 1 or not nums:
        return None
    max_n = max(nums)
    primes = sort_primes(max_n)
    prime_count_up_to = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count_up_to[i] = prime_count_up_to[i - 1] + (
            1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count_up_to[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
