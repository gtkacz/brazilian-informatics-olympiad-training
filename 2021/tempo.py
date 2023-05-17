def solve(e: list[list[str, int]]) -> int:
    for r, x in e:
        pass


def main():
    n = int(input())
    e = []

    for _ in range(n):
        e.append(input().split())

    print(solve(e))


def tests():
    tests = (
        ('VVPPPV', 2),
        ('PPPPPP', -1),
    )

    for test in tests:
        g, expected = test
        result = solve(g)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
