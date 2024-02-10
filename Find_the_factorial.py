def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        result = 1
        for i in range (2, n + 1):
            result *= i
        return result
num = 5
fact = factorial(num)
print("Factorail of is", fact)