from scripts import linear_search


def test_search_on_empty_list():
    assert linear_search.linear_search([], 5) == -1


def test_search_with_key():
    assert linear_search.linear_search([12, 19, 5, 2, 0, 19], 5) == 2


def test_search_without_key():
    assert linear_search.linear_search([12, 19, 35, 2, 0, 19], 5) == -1