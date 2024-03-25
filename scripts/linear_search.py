def linear_search(items: list[int], key: int) -> int:
    result = -1

    for index, item in enumerate(items):
        if item == key:
            result = index
            break

    return result