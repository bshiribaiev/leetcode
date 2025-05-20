def matrix_flip(matrix):
    max_sum = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            fr, lr = i, len(matrix) - i - 1
            fc, lc = j, len(matrix) - j - 1

            max_val = matrix[fr][fc]
            if matrix[fr][lc] > max_val:
                max_val = matrix[fr][lc]
            if matrix[lr][fc] > max_val:
                max_val = matrix[lr][fc]
            if matrix[lr][lc] > max_val:
                max_val = matrix[lr][lc]
            
            max_sum += max_val

    return max_sum

arr = [
    [1, 2],
    [4, 5]
]

sum = matrix_flip(arr)
print(sum)


