# Challenge 4: Fibonacci Number Learning points: Finabonacci Algorithm, Function Implementation, Testing & Debugging
# Ada sebuah input 20. Carilah fibonacci number dari inputan tersebut.
# Setelah itu, buatlah testing dan debugging dalam proses perhitungan tersebut.
# Cover semua positive dan negative casenya.

def fibonacci(n):
    if n < 0:
        raise ValueError("Input harus berupa bilangan bulat non-negatif.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

n = 20
try:
    result = fibonacci(n)
    print(f"Fibonacci number dari {n} adalah: {result}")
except ValueError as e:
    print(e)