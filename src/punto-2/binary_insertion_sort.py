def binary_search(arr: list, start: int, end: int, key: int) -> int:
    while start < end:
        mid = (end + start) // 2
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid
    return start


# iterative method
def binary_insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        insertion = binary_search(arr, 0, i, key)
        for j in range(i, insertion, -1):
            arr[j] = arr[j - 1]
        arr[insertion] = key


def binary_insertion_sort_recursive(arr: list, index: int = 0):
    if index >= len(arr):
        return
    else:
        key = arr[index]
        insertion = binary_search(arr, 0, index, key)
        swap(insertion, index, arr)
        arr[insertion] = key
    binary_insertion_sort_recursive(arr, index + 1)


def swap(insertion, index, arr):
    if index <= insertion:
        return
    else:
        arr[index] = arr[index - 1]
    swap(insertion, index - 1, arr)


def main():
    lts = [5, 3, 2, 6, 1]
    binary_insertion_sort_recursive(lts)
    print(lts)


main()
