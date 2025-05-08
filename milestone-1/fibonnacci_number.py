def fib(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using an iterative list-building approach.

        The Fibonacci sequence is defined as:
            F(0) = 0
            F(1) = 1
            F(n) = F(n-1) + F(n-2) for n > 1

        Args:
            n (int): The index (0-based) of the Fibonacci number to return.

        Returns:
            int: The n-th Fibonacci number.
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    # List containing the first two Fib numbers i.e 1 and 2
    fib_list = [0, 1]

    # keep calculating and appending the Fib number un till len(fib_list) == n
    while len(fib_list) <= n:
        next_fib = fib_list[-1] + fib_list[-2]  # sum of two last numbers
        fib_list.append(next_fib)

    return fib_list[n]


print(fib(10)) # 55
print(fib(1)) # 1
print(fib(0)) # 0