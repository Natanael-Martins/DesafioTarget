def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a == n or b == n

num = int(input("Informe um número: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
