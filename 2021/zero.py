def solve(m: list[int]) -> int:
    while 0 in m:
        curr_idx = m.index(0)
        m.pop(curr_idx-1)
        m.pop(curr_idx-1)

    return sum(m)


def main():
    n = int(input())
    m = list(int(input()) for _ in range(n))

    print(solve(m))


def tests():
    tests = (
        ([3, 0, 4, 0], 0),
        ([1, 3, 5, 4, 0, 0, 7, 0, 0, 6], 7),
    )

    for test in tests:
        m, expected = test
        result = solve(m)
        assert result == expected
        # print(f'{result} == {expected} => {result == expected}')

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
