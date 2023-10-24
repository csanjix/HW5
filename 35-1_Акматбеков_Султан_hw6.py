def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Отсортированный массив:", my_list)

sort_lst = []


def bubble_sort(lst):
    while len(lst) != 0:
        m = lst.index(max(lst))
        sort_lst.append(lst.pop(m))
    return f"отсортированный список - {sort_lst}"


print(bubble_sort([111, 54, 44, 14, 62, 112, 32]))
