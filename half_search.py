def search(array, number, left_index, right_index):
    print(array, number, left_index, right_index)
    if left_index <= right_index:
        middle_index = (left_index + right_index)//2
        print("middle_index:", middle_index)
        if array[middle_index] == number:
            return middle_index
        elif array[middle_index] < number:
            return search(array, number, middle_index + 1, right_index)
        else:
            return search(array, number, left_index, middle_index - 1)
    else:
        return None

array1 = [1, 2, 3, 4, 5, 6, 7]

print(search(array1, 2, 0, len(array1)))