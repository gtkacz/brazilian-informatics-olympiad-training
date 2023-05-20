def solve(d: int) -> int:
    traveled = (d - 3) % 8

    match traveled:
        case 3:
            return 1
        case 4:
            return 2
        case 5:
            return 3
        case _:
            raise ValueError('Invalid input')


def main():
    d = int(input())

    print(solve(d))


def tests():
    tests = (
        (23, 2),
        (6, 1),
        (9192, 3),
    )

    for test in tests:
        d, expected = test
        result = solve(d)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
