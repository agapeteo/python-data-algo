import math


def primes(limit):
    sieve_list = [False] * limit
    for i in range(2, math.floor(math.sqrt(limit))):
        if sieve_list[i]:
            continue

        for j in range(i + i, limit, i):
            sieve_list[j] = True

    result = []
    for k in range(2, limit):
        if not sieve_list[k]:
            result.append(k)
    return result


print(primes(100))
