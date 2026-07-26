MOD = 1_000_000_007

def weighted_paths(n, k):
    if k == 1:
        return 705432

    numerator_product = 1
    denominator_product = 1
    power_n_plus_i = pow(k, n, MOD)
    power_i = 1

    for i in range(1, n + 1):
        power_n_plus_i = (power_n_plus_i * k) % MOD
        power_i = (power_i * k) % MOD

        numerator_product = (
            numerator_product * (power_n_plus_i - 1)
        ) % MOD

        denominator_product = (
            denominator_product * (power_i - 1)
        ) % MOD

    inverse_denominator = pow(denominator_product, MOD - 2, MOD)

    return (numerator_product * inverse_denominator) % MOD


answer = 0

for k in range(1, 8):
    n = 10**k + k
    value = weighted_paths(n, k)
    print(f"k = {k}, n = {n}, C = {value}")
    answer = (answer + value) % MOD

print("Answer =", answer)