def binary_addition(arr1, arr2, n):
    size = n + 1
    arr3 = [0] * size
    sum = 0
    for i in range(n-1, -1, -1):
        sum += arr1[i] + arr2[i]

        if sum == 0:
            arr3[i+1] = 0
            sum = 0

        elif sum == 1:
            arr3[i+1] = 1
            sum = 0

        elif sum == 2:
            arr3[i+1] = 0
            sum = 1

        elif sum == 3:
            arr3[i+1] = 1
            sum = 1

    if sum == 1:
        arr3[0] = 1

    return arr3

arr1 = [1, 1, 0]  # 110 binary
arr2 = [0, 1, 1]  # 011 binary

n = 3
result = binary_addition(arr1, arr2, n)

print(result)