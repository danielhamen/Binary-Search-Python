def binary_search(arr: list, target: any, is_sorted: bool = True) -> int:
    """
    Performs a binary search on `arr` to search for `target`. If target is not found, `-1` is returned

    `arr` should be sorted; set `is_sorted` to `False` if it is not sorted
    """

    arr if is_sorted else arr.sort()

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage; this will only execute if you run `main.py`
if __name__ == "__main__":
    import random

    n = 10 # Number of random numbers (exclusive)
    numbers = [int(random.random() * 100) for x in range(n)]
    print(
        binary_search(
            numbers,
            random.choice(numbers),
            is_sorted=False
        )
    )
