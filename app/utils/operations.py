
def power(base: float, exponent: float) -> float:
    """Compute base raised to the power of exponent."""
    return base ** exponent


def fibonacci(n: int) -> int:
    """Compute the n-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError(
            "Fibonacci number cannot be computed for negative index"
        )
    elif n in (0, 1):
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def factorial(n: int) -> int:
    """Compute the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
