def merge_sort(ls: list) -> list:
    if len(ls) <= 1: 
        # the list is sorted
        return ls
    
    mid = len(ls) // 2 # 1
    
    right = ls[mid:] # 1
    left = ls[:mid] # 1 
    
    sorted_right = merge_sort(right) # f(n/2)
    sorted_left = merge_sort(left) # f(n/2)

    return merge(sorted_left, sorted_right) # n
    # the complexity of the function is n + 2f(n/2)


def merge(left: list, right: list) -> list:
    result = [] # 1
    i, j = 0, 0 # iterative variables 1
    # the complexity if this imperative part is 2
    
    while i < len(left) and j < len(right): # n - r
        if left[i] < right[j]: # n - r
            result.append(left[i]) # n - r
            i += 1 # n -r
        else: 
            result.append(right[j]) # n - r 
            j += 1 # n - r
        # the of the while complexity will be: 2(n - r)
    
    result.extend(left[i:]) # if there is a rest append it to result
    result.extend(right[j:]) # r 
    return result
    # the complexity of the function 2n - r 
    # in BigOh O(n)


def main():
    lts = [4, 7, 3, 1, 2, 9]
    print(merge_sort(lts))


main()
