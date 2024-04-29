def merge_sort(ls: list) -> list:
    if len(ls) <= 1: 
        # the list is sorted
        return list
    
    midle = len(ls) // 2 # 1
    
    rigth = ls[midle:] # 1
    left = ls[:midle] # 1 
    
    sorted_rigth = merge_sort(rigth) # f(n/2)
    sorted_left = merge_sort(left) # f(n/2)

    return merge(left, rigth) # n
    # the complexity of the funtion is n + 2f(n/2)


def merge(left: list, rigth: list) -> list:
    result = [] # 1
    i, j = 0, 0 # iteratives variables 1
    # the complexity if this imperative part is 2
    
    while i < len(left) and j < len(rigth): # n - r
        if left[i] < rigth[j]: # n - r
            result.append(left[i]) # n - r
            i += 1 # n -r
        else: 
            result.append(rigth[j]) # n - r 
            j += 1 # n - r
        # the of the while complexity will be: 2(n - r)
    
    result.extend(left[i:]) # if there is a rest append it to result
    result.extend(rigth[j:]) # r 
    return result
    # the complexity of the function 2n - r 
    # in BigOh O(n)


def main():
    lts = [4, 7, 3, 1, 2, 9]
    print(merge_sort(lts))


main()
