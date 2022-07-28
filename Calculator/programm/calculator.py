# Метод который считает + - * / 
def CalculateSimpleOperations(lst): 
    temp = 0
    # Умножение
    while '*' in lst:
        temp = lst[lst.index('*')-1] * lst[lst.index('*')+1]
        lst.insert(lst.index('*')-1, temp)
        lst.pop(lst.index('*')-1)
        lst.pop(lst.index('*')+1)
        lst.pop(lst.index('*'))
    # Деление
    while '/' in lst:
        temp = lst[lst.index('/')-1] / lst[lst.index('/')+1]
        lst.insert(lst.index('/')-1, temp)
        lst.pop(lst.index('/')-1)
        lst.pop(lst.index('/')+1)
        lst.pop(lst.index('/'))
    # Сложение
    while '+' in lst:
        temp = lst[lst.index('+')-1] + lst[lst.index('+')+1]
        lst.insert(lst.index('+')-1, temp)
        lst.pop(lst.index('+')-1)
        lst.pop(lst.index('+')+1)
        lst.pop(lst.index('+'))
    # Вычитание
    while '-' in lst:
        temp = lst[lst.index('-')-1] - lst[lst.index('-')+1]
        lst.insert(lst.index('-')-1, temp)
        lst.pop(lst.index('-')-1)
        lst.pop(lst.index('-')+1)
        lst.pop(lst.index('-'))
    return lst[0]

# Метод который считает с учетом скобок
def Calculator(lst):
    tempList = []
    if '(' in lst or ')' in lst:
        # переворачивает список что бы найти последнее вхождение
        revers_lst = lst[::-1].index('(')
        index_of_first_parenthesis = len(lst) - 1 - revers_lst
        index_of_second_parenthesis = lst.index(')', index_of_first_parenthesis)
        # добавляет в tempList элементы между скобками, вычисляет, а затем удаляет их
        for i in range(index_of_first_parenthesis+1, index_of_second_parenthesis):
            tempList.append(lst[i])
        lst.insert(index_of_first_parenthesis, CalculateSimpleOperations(tempList))
        del lst[index_of_first_parenthesis+1:index_of_second_parenthesis+2]
        # рекурсия позволяет вычислить и удалить все скобки
        return Calculator(lst)
    else:
        return CalculateSimpleOperations(lst)
