def find_smallest_multiple(n: int) -> int:
    if n == 1:
        return 1

    x = 1
    while True:
        divisible = True
        for i in range(1, n + 1):
            if x % i != 0:
                divisible = False
                break
        if divisible:
            return x
        x += 1
