from collections import defaultdict


def solve(n: int, chains: list) -> list:
    graph = defaultdict(list)
    infected_count = [0] * (n + 1)

    for chain in chains:
        infector, num_infected, *infected = chain
        graph[infector].extend(infected)

        for person in infected:
            infected_count[int(person)] += 1

    patient_zero = []

    for person in range(1, n + 1):
        if infected_count[person] == 0:
            patient_zero.append(person)

    return patient_zero


def main():
    n, c = map(int, input().split())
    chains = [list(map(int, input().split())) for _ in range(c)]

    for i in solve(n, chains):
        print(i)


def tests():
    tests = (
        (13, 16, [], [3]),
    )

    for test in tests:
        n, m, expected = test
        result = solve(n, m)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
