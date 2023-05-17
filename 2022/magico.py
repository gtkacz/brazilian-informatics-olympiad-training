def solve(n: int, m: tuple[tuple[int]]) -> int:
    zero_x, zero_y = None, None
    should_break = False

    for i in range(n):
        for j in range(n):
            if m[i][j] == 0:
                zero_x, zero_y = i, j
                should_break = True
                break

        if should_break:
            break

    magic_idx = 0 if zero_x != 0 else 1
    magic_sum = sum(m[magic_idx])
    magic_number = magic_sum - sum(m[zero_x])

    return magic_number, zero_x+1, zero_y+1


def main():
    n = int(input())
    m = tuple(tuple(map(int, input().split())) for _ in range(n))

    for o in solve(n, m):
        print(o)


def tests():
    tests = (
        (3, ((2, 9, 4), (7, 0, 3), (6, 1, 8)), (5, 2, 2)),
        (4, ((11, 8, 5, 0), (14, 1, 4, 15), (2, 13, 16, 3), (7, 12, 9, 6)), (10, 1, 4)),
    )

    for test in tests:
        n, m, expected = test
        result = solve(n, m)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
