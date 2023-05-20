def solve(t: tuple[int], p: int, m: int) -> str:
    small = t.count(1)
    medium = len(t) - small

    if (p >= small) and (m >= medium):
        return 'S'

    return 'N'


def main():
    n = int(input())
    t = tuple(map(int, input().split()))
    p = int(input())
    m = int(input())

    print(solve(t, p, m))


def tests():
    tests = (
        ((1, 1, 2, 1, 2), 3, 2, 'S'),
        ((2, 2, 2, 2), 1, 3, 'N'),
        ((1, 1, 1, 2, 1, 1), 4, 4, 'N'),
    )

    for test in tests:
        t, p, m, expected = test
        result = solve(t, p, m)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
