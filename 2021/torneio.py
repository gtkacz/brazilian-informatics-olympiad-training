def solve(g: str) -> int:
    v_count = g.count('V')

    if v_count == 0:
        return -1

    elif v_count < 3:
        return 3

    elif v_count < 5:
        return 2

    else:
        return 1


def main():
    g = ''.join(tuple(input() for _ in range(6)))

    print(solve(g))


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
