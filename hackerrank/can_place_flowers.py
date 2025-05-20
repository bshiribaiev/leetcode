def can_place_flowers(flowerbed, n):
    # Write your code here
    plot = 0
    i = 0
    
    while i < len(flowerbed):
        
        if len(flowerbed) == 1 and flowerbed[i] == 0:
            return n == 1
            
        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                plot += 1
                i += 1
        
        elif i == len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                plot += 1
                i += 1   
        
        elif (flowerbed[i - 1] == 0 and flowerbed [i] == 0 
        and flowerbed[i+1] == 0):
            plot += 1
            i += 1
        
        i += 1    
    
    return plot >= n
