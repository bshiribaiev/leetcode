def superDigit(n, k):
    # Write your code here
    sum_n = 0
    for i in n:
        sum_n += int(i) * k
    
    if sum_n < 10:
        return sum_n
        
    return superDigit(str(sum_n), 1)
