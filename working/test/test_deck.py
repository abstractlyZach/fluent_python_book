import deck


def test_deck_len(unshuffled_deck):
    assert len(unshuffled_deck) == 52


def test_deck_order(unshuffled_deck):
    expected_cards = [deck.Card(suit="spades", rank=str(rank)) for rank in range(2, 5)]
    assert unshuffled_deck[0:3] == expected_cards


def test_get_aces(unshuffled_deck):
    aces = unshuffled_deck[12::13]
    for card in aces:
        assert card.rank == "A"


def test_can_use_reversed_on_deck(unshuffled_deck):
    expected_cards = [
        deck.Card(suit="hearts", rank=rank) for rank in list("akqjt9".upper())
    ]
    for expected_card, actual_card in zip(expected_cards, reversed(unshuffled_deck)):
        assert expected_card == actual_card
