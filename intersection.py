def intersection(array_1, array_2):
    elements_1 = set()
    intersected = []
    for i in range(0, len(array_1)):
        elements_1.add(array_1[i])
    already_added = set()
    for j in range(0, len(array_2)):
        if array_2[j] in elements_1 and array_2[j] not in already_added:
            intersected.append(array_2[j])
            already_added.add(array_2[j])
    return intersected

array_1=[1, 2, 3, 4, 5, 4, 6]
array_2=[4, 2, 6, 7]


print(intersection(array_1, array_2))