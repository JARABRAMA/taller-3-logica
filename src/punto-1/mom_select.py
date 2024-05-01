from src.utils.methods import input_list


def split_in_five(arr) -> list:
    groups = []
    lts = []
    i = 0
    for number in arr:
        if len(lts) % 5 != 0:
            lts.append(number)
        else:
            if len(lts) != 0:
                groups.append(lts)
            lts = [number]
    if not lts in groups:
        groups.append(lts)
    return groups


def partition(arr, pivot):
    low = []
    high = []
    equal = []
    for item in arr:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        else:
            equal.append(item)
    return low, high, equal


def sort(arr: list) -> list:
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def mom_select(arr: list, k: int) -> int:
    if len(arr) <= 5:
        sorted_arr = sort(arr)
        return sorted_arr[k]

    groups = split_in_five(arr)
    medians = []
    for group in groups:
        sorted_group = sort(group)
        median = sorted_group[len(sorted_group) // 2]
        medians.append(median)

    pivot = mom_select(arr, len(medians) // 2)

    low, high, equal = partition(arr, pivot)

    if k < len(low):
        return mom_select(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return mom_select(high, k - len(low) - len(equal))


def testing_split_in_five():
    lst = [3, 4, 5, 6, 7, 4, 3, 1, 3]
    print(split_in_five(lst))


def testing_sort():
    lts = [4, 5, 67, 42, 2, 3]
    print(sort(lts))


def testing_partition():
    lts = [12, 25, 12, 16, 34, 45, 1, 2]
    print(partition(lts, 12))


def main():
    arr = input_list()
    k = int(input("Enter the k: "))
    print("the k-esim element of the list is: {0}".format(mom_select(arr, k)))


main()
