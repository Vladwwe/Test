#це для тесту


def bubble_sort(arr):
    """Бульбашкове сортування"""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort(arr):
    """Сортування вибором"""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


def insertion_sort(arr):
    """Сортування вставкою"""
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# приклад перевірки роботи функцій
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Bubble sort:", bubble_sort(data))
    print("Selection sort:", selection_sort(data))
    print("Insertion sort:", insertion_sort(data))