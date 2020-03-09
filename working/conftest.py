import pytest

import deck


@pytest.fixture()
def unshuffled_deck():
    return deck.FrenchDeck()
