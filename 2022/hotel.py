def solve(d: int, a: int, n: int) -> int:
    days = n

    if n > 15:
        days = n
        n = 15

    if n == 1:
        return 31*d

    else:
        return (32 - days) * (d + (a * (n-1)))


def main():
    d = int(input())
    a = int(input())
    n = int(input())

    print(solve(d, a, n))


def tests():
    tests = (
        (100, 10, 1, 3100),
        (100, 20, 15, 6460),
        (100, 5, 16, 2720),
    )

    for test in tests:
        d, a, n, expected = test
        result = solve(d, a, n)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
