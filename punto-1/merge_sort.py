def merge_sort(ls: list) -> list:
    if len(ls) <= 1: 
        # the list is sorted
        return list
    
    midle = len(ls) // 2
    
    rigth = ls[midle:]
    left = ls[:midle]
    
    sorted_rigth = merge_sort(rigth)
    sorted_left = merge_sort(left)

    return merge(left, rigth)


def merge(left: list, rigth: list) -> list:
    result = []
    i, j = 0, 0 # iteratives variables 

    while i < len(left) and j < len(rigth): 
        if left[i] < rigth[j]: 
            result.append(left[i])
            i += 1
        else: 
            result.append(rigth[j])
            j += 1
    
    result.extend(left[i:]) # if there is a rest append it to result
    result.extend(rigth[j:])

    return result

def main():
    lts = [4, 7, 3, 1, 2, 9]
    print(merge_sort(lts))


main()
