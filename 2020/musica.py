def solve(n: int, c: int, i: tuple[tuple[int, int]]) -> int:
    satisfaction = [False] * n
    s = 0

    if set(a for a, _ in i) == set(d for _, d in i):
        return -1

    while not all(satisfaction):
        for index, (a, d) in enumerate(i):
            if d == c:
                c = a
                satisfaction[index] = False
                s += 1

            else:
                satisfaction[index] = True

    return s


def main():
    n, m, c = map(int, input().split())
    i = tuple(tuple(map(int, input().split())) for _ in range(n))

    print(solve(n, c, i))


def tests():
    tests = (
        (3, 2, ((1, 2), (2, 3), (3, 2)), 1),
        (4, 2, ((1, 3), (2, 3), (3, 2), (5, 1)), 3),
        (3, 1, ((1, 2), (2, 3), (3, 1)), -1)
    )

    for test in tests:
        n, c, i, expected = test
        result = solve(n, c, i)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
