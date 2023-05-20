def solve(n: str, m: str) -> int:
    return m + (m - n)


def main():
    n = int(input())
    m = int(input())

    print(solve(n, m))


def tests():
    tests = (
        (13, 16, 19),
        (14, 14, 14),
    )

    for test in tests:
        n, m, expected = test
        result = solve(n, m)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
