def find_smallerOne(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex


def selection_array(arr):
    newArray = []
    copiedArray = list(arr)
    for _ in range(len(copiedArray)):
       smallest =  find_smallerOne(copiedArray)
       newArray.append(copiedArray.pop(smallest))
    return newArray


print(selection_array([3, 4, 5, 2, 1, 6, 7, 8, 9, 10]))