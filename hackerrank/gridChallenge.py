def gridChallenge(grid):
    for i in range(len(grid)):
        new_r = list(grid[i])
        
        for j in range(len(new_r)-1):
            min = j
            
            for k in range(j+1, len(new_r)):
                if new_r[k] < new_r[min]:
                    min = k
                    
            new_r[j], new_r[min] = new_r[min], new_r[j]
            
        grid[i] = ''.join(new_r)
        
    for i in range(len(grid[0])):
        for j in range(1, len(grid)):

            if grid[j][i] < grid[j-1][i]:
                return "NO"
        
    return "YES"
