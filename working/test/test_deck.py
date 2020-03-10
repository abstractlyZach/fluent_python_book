import random

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


def test_deck_check_for_in_operator(unshuffled_deck):
    card = deck.Card(suit="spades", rank="8")
    assert card in unshuffled_deck


def test_deck_card_not_in_deck(unshuffled_deck):
    card = deck.Card(suit="spades", rank="beasts")
    assert card not in unshuffled_deck


def test_sorting_deck_low_cards(unshuffled_deck):
    low_cards = [
        deck.Card("2", suit) for suit in "clubs diamonds hearts spades".split()
    ] + [deck.Card("3", "clubs")]
    sorted_deck = sorted(unshuffled_deck, key=deck.spades_high)
    for expected_card, actual_card in zip(low_cards, sorted_deck):
        assert expected_card == actual_card


def test_sorting_deck_high_cards(unshuffled_deck):
    high_cards = [deck.Card("K", "spades")] + [
        deck.Card("A", suit) for suit in "clubs diamonds hearts spades".split()
    ]
    sorted_deck = sorted(unshuffled_deck, key=deck.spades_high)
    for expected_card, actual_card in zip(high_cards, sorted_deck[-len(high_cards) :]):
        assert expected_card == actual_card


def test_random_card_draw_doesnt_throw_error(unshuffled_deck):
    random.choice(unshuffled_deck)
