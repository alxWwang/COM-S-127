index = [1,2,3,4,5]
array = [3,4,1,2,6,5]


def insertionSort(arr):
    for step in range(len(arr)):
        key = arr[step]
        j = step -1
        
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j -1
        array[j+1] = key
    return arr

print(insertionSort(array))