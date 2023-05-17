from collections import Counter
from itertools import accumulate


def solve(n: int, s: int, m: tuple[int]) -> int:
    table = Counter()
    total = 0

    for acc in accumulate(m, initial=0):
        total += table[acc - s]
        table[acc] += 1

    return total


def main():
    n = int(input())
    s = int(input())
    m = tuple(map(int, input().split()))

    print(solve(n, s, m))


def tests():
    tests = (
        (6, 2, (0, 2, 0, 1, 0, 1), 6),
        (8, 13, (10, 1, 0, 0, 9, 10, 1, 5), 0),
        (5, 6, (1, 0, 3, 0, 2), 1),
    )

    for test in tests:
        n, s, m, expected = test
        result = solve(n, s, m)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
