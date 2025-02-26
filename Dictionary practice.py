dict = {}

dict[4] = 3
dict.get(4)

#print(dict.items()) 

arr1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
left = 0
right = 0 
for i in range (0, len(arr)):
    left = left + arr[i][i]
    for j in range(len(arr), 0, -1):
        right = right + arr[i][len(arr)]

difr = left - right
'''

def sortbek(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr  




#print(difr)


#print(array[0][0])