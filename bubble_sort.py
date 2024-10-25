# bubble_sort.py
# Алгоритм пузырьковой сортировки с оценкой сложности

def bubble_sort(arr):
    """
    Сортирует массив методом пузырьковой сортировки.

    Параметры:
    arr (list): Список чисел для сортировки.

    Возвращает:
    list: Отсортированный список.
    """
    n = len(arr)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Пример использования
if __name__ == "__main__":
    array = [10, -3, 7, 2, -5, 6, 0, -8, 9, 1]
    print("Отсортированный массив:", bubble_sort(array))
