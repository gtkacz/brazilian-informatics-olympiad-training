def solve(n: int, m: int, s: int) -> int:
    r = tuple(range(m, n, -1))

    for i in r:
        if sum(tuple(map(int, tuple(str(i))))) == s:
            return i
        
    return -1


def main():
    n = int(input())
    m = int(input())
    s = int(input())

    print(solve(n, m, s))


def tests():
    tests = (
        (1, 100, 6, 60),
        (1000, 1001, 3, -1),
        (80, 500, 12, 480),
    )

    for test in tests:
        n, m, s, expected = test
        result = solve(n, m, s)
        assert result == expected

    print('All tests passed successfully!')

if __name__ == '__main__':
    main()
    # tests()
