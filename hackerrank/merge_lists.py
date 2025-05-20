def merge_sorted_lists(lst1, lst2):
    # Write your code here
    size = len(lst1) + len(lst2) 
    lst3 = [0] * size 
    l = 0
    r = 0
    i = 0
    if size == 0:
        return lst3
        
    while l < len(lst1) and r < len(lst2):
        if lst1[l] < lst2[r]:
            lst3[i] = lst1[l]
            l += 1
        else:
            lst3[i] = lst2[r]
            r += 1
        
        i += 1
    
    while l < len(lst1):
        lst3[i] = lst1[l]
        l += 1
        i += 1
    
    while r < len(lst2):
        lst3[i] = lst2[r]
        r += 1
        i += 1
    
    return lst3
