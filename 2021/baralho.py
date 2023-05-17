def solve(c: str) -> tuple[int | str]:
    suits = {'C': [], 'E': [], 'U': [], 'P': []}
    cards: tuple[str] = tuple(c[i:i+3] for i in range(0, len(c), 3))

    for card in cards:
        card_number = int(card[:2])
        card_suit = card[2]

        suits[card_suit].append(card_number)

    response = []
    
    def evaluate_suit(cards: list[int]) -> int | str:
        if len(set(cards)) != len(cards):
            return 'erro'
        
        elif len(cards) == 13:
            return 0
        
        else:
            return 13 - len(cards)
    
    for cards in suits.values():
        response.append(evaluate_suit(cards))

    return tuple(response)


def main():
    c = input()

    for r in solve(c):
        print(r)


def tests():
    tests = (
        ('11P01C02C01U02U03U04U', (11, 13, 9, 12)),
        ('13P02P01P03P04P05P06P07P08P09P10P11P12P', (13, 13, 13, 0)),
        ('01C02C03C04C05C07C09C10C11C02E02E03E11U', (4, 'erro', 12, 13)),
    )

    for test in tests:
        g, expected = test
        result = solve(g)
        assert result == expected

    print('All tests passed successfully!')


if __name__ == '__main__':
    main()
    # tests()
