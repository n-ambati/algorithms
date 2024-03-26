def binary_search(items: list[int], key: int) -> int:
    low, high = 0, len(items)

    while low < high:
        mid = low + (high - low) // 2

        if items[mid] == key:
            return mid
        
        if items[mid] < key:
            low = mid + 1
        else:
            high = mid
    
    return -1