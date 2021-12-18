import random
def stupid(lst:list):
    '''
    Возвращает отсортированный массив.
    Работает на основе алгоритма глупой сортировки, простейшей сортировки обменами
    Работает следующим образом, создаем цикл, который conditional, который
    будет работать до тех пор пока номер текущего итерируемого объекта меньше количества объектов.
    Соответственно мы сразу задаем это условие.
    Начальное значение итерируемого объекта 1. То есть начинаем сравнивать со второго объекта.
    И сравнение идет с ранее идущим.
    Если ранее идущий объект меньше, то они меняются местами.
    Итерируемый объект также остается вторым. и все начинается заново.
    Если условие не выполняется, то происходит перемещение дальше по списку.
    '''
    i, size = 1, len(lst)
    while i < size:
        if lst[i-1] > lst[i]:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            i = 1
        else:
            i += 1
    return lst
listik = [33,5,445,32,65,3456,12,777,333,123]
print(f'stupid sort:{stupid(listik)}')


def dwarf_sort(lst):
    '''
    Здесь значит если у нас второй элемент больше первого (по индексу),
    то мы переходим к третьему элементу и сравниваем его со вторым и так до тех
    пор пока индекс элемента не станет равен последнему индексу для данного массива
    Если итерируемый элемент меньше чем предыдущий, то они меняются местами.
    При этом если это был первый элемент, то цикл просто начинается заново,
    А если это был не первый элемент, то соответственно итерируемым элемент
    сдвигает на 1 назад.
    '''
    i, size = 1, len(lst)
    while i < size:
        if lst[i] > lst[i-1]:
            i +=1
        else:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            if i != 1:
                i -=1
    return lst
print(f'dwarf sort:{dwarf_sort(listik)}')



def bubble(lst):
    '''

    '''
    for i in range(len(lst)):
        for j in range(0, len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst



def quick(lst):
    less = list()
    pivotlist = list()
    more = list()
    if len(lst) <= 1:
        return lst
    else:
        pivot=lst[0]
        for i in lst:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotlist.append(i)

        less = quick(less)
        more = quick(more)

        return less + pivotlist + more
print(f'quicksort {quick(listik)}')





