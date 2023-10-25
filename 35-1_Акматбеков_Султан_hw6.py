def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


print(bubble_sort([6, 1, 4, 2, 6, 9]))


def binary_search(lst, val):
    n = len(lst)
    left, right = 0, n - 1
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == val:
            print("Element found")
            return middle
        elif lst[middle] > val:
            right = middle - 1
        else:
            left = middle + 1
    print('Element wasn\'t found')
    return -1


print(binary_search([1, 3, 4, 6, 8, 9], 7))