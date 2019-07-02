# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('Задание-1')
def fibonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]


print('fibonacci(1, 6): ', fibonacci(1, 6))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('Задание-2')
def sort_to_max(origin_list):
    g = 0
    d = 1
    while d < len(origin_list):
        while g < (len(origin_list) - 1):
            if origin_list[g] > origin_list[g + 1]:
                origin_list[g], origin_list[g + 1] = origin_list[g + 1], origin_list[g]
            g += 1
        d += 1
        g = 0

origin_list=[2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(origin_list)
print(origin_list)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print('Задание-3')


def filter_func(function, iterable):
    return (item for item in iterable if function(item))


print(list(filter_func(lambda x: True if x % 2 == 0 else False,
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print('Задание-4')
import math
A1, A2, A3, A4 = (2, 3), (0, 2), (4, 1), (6, 2)

def isparall(a, b, c, d):
    '''
    Проверка признаков параллелограмма
    '''
    p1 = False
    p2 = False

    #Противополжные стороны параллельны и равны

    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    if ab == cd and cb == ad:
        print('Равенство сторон: верно')
        p1 = True
    else:
        print('Противоположные стороны НЕ равны')

    #Диагонали O1 и O2 в точках пересечения делятся пополам и равны
    hO1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    hO2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if hO1 == hO2:
        print('Равенство половин диагоналей: верно')
        p2 = True
    else:
        print('Половины диагоналей НЕ равны')

    if p1 and p2:
        print('Вершины A1%s, A2%s, A3%s, A4%s\nобразуют параллелограмм' %
              (a, b, c, d))
    else:
        print('Вершины не образуют параллелограмм')

isparall(A1, A2, A3, A4)

