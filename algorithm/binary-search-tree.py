def binary_search(element, some_list, offset=None):
    # 값 = element, return inde
    binaryIndex = (len(some_list)/2) if len(some_list)%2 == 0 else (len(some_list)/2) -0.5
    binaryIndex = int(binaryIndex)
    if some_list[binaryIndex]== element:
        if offset :
            return offset -1
        else:
            return binaryIndex
    elif binaryIndex <= 0:
        return None
    elif some_list[binaryIndex] < element:
        if offset is None:
            offset = binaryIndex
        else:
            offset = offset
        return binary_search(element, some_list[binaryIndex:len(some_list)], offset+binaryIndex)
    elif some_list[binaryIndex] > element:
        return binary_search(element, some_list[0: binaryIndex])
        

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
