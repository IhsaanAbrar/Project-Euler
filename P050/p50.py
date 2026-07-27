def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False

        divisor += 1

    return True


def solve(limit):
    primes = []

    for number in range(2, limit):
        if is_prime(number):
            primes.append(number)

    length = 1

    while sum(primes[:length]) < limit:
        length += 1

    for length in range(length - 1, 0, -1):
        for start in range(len(primes) - length + 1):
            total = sum(primes[start:start + length])

            if total >= limit:
                break

            if is_prime(total):
                return total

print()
print(solve(1_000_000))
print()