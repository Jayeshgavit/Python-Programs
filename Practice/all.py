memo = {}
def factorial_memory(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_memory(n - 1)
    return memo[n]

print(factorial_memory(2))
print(memo)