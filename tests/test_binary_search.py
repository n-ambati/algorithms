from scripts import binary_search


def test_search_on_empty_list():
    assert binary_search.binary_search([], 5) == -1


def test_search_with_key():
    assert binary_search.binary_search([0, 2, 5, 12, 19, 39], 5) == 2


def test_search_without_key():
    assert binary_search.binary_search([0, 2, 8, 12, 19, 39], 5) == -1