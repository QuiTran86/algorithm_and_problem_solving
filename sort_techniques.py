"""Sort techniques will be implemented in this file
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
"""


def bubble_sort(items):
    """
    The time complexity: O(n^2) and space complexity: O(1)
    :param items:
    :return:
    """
    if not items:
        return

    for i in range(len(items) - 1, 0, -1):
        for j in range(i):
            if items[j] > items[j + 1]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
    return items


def selection_sort(items):
    """
    The time complexity: O(n^2) and space complexity: O(1)
    :param items:
    :return:
    """
    if not items:
        return

    for i in range(len(items)):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[min_index] > items[j]:
                min_index = j
        if min_index != i:
            items[min_index], items[i] = items[i], items[min_index]

    return items


def insertion_sort(items):
    """
    The time complexity: O(n^2), space complexity: O(1)
    :param items:
    :return:
    """
    if not items:
        return

    for i in range(1, len(items)):
        temp = items[i]
        j = i - 1
        while temp < items[j] and j >= 0:
            items[j + 1] = items[j]
            items[j] = temp
            j -= 1
    return items


items = [1, 6, 11, 9, 7, 3, 2, 5]
print(insertion_sort(items))
