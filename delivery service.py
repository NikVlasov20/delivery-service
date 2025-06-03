# id - 139004822
# Создание и заполнение кортежа значениями весов отдельных роботов
weight: tuple = tuple(int(number) for number in input().split())
# Максимальное значение грузоподъёмности
limit: int = int(input())
# Сортировка кортежа
sorted(weight)
# Инициализация результирующей переменной
result: int = 0
# Объявление указателей
left_pointer: int = 0
right_pointer: int = len(weight) - 1
# Основной цикл программы, работающий до того, пока 2 указателя не встретятся
while left_pointer <= right_pointer:
    # Если сумма минимального и максимального элементов кортежа <= limit,
    # указатели смещаются на 1 элемент ближе к середине массива
    # и результат увеличивается на 1
    if weight[left_pointer] + weight[right_pointer] <= limit:
        left_pointer += 1
        right_pointer -= 1
        result += 1
    # Иначе только правый указатель смещается на 1 элемент к середине массива
    # и значение результата увеличивается на 1 
    else:
        right_pointer -= 1
        result += 1

print(result)