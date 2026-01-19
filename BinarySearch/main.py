def search(target):
    data = [1,2,3,4,5,6,7,8,9,10]
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return True
        elif target < data[mid]:
            right = mid - 1
        elif target > data[mid]:
            left = mid + 1
    return False

def get_result():
    try:
        target = int(input("Введите число для поиска: "))
        result = search(target)
        if result == True:
            print('Данный элемент есть в этой последовательности')
        else:
            print('Элемента нет в последовательности')
    except ValueError:
        print("Ошибка: нужно ввести целое число")


get_result()

