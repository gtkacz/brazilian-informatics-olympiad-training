from collections import Counter


def solve(p: str, a: str) -> str:
    if '*' not in a:
        return 'S' if Counter(p) == Counter(a) else 'N'

    return 'N' if Counter(a.replace('*', '')) - Counter(p) else 'S'


def main():
    p = input()
    a = input()

    print(solve(p, a))


def tests():
    tests = (
        ('roma', 'ator', 'N'),
        ('olimpiada', 'poliamida', 'S'),
        ('microfone', '*conform*', 'S'),
    )

    for test in tests:
        p, a, expected = test
        result = solve(p, a)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
