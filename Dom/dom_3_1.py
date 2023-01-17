'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции нечетным индексом.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
print(100*'\n')
#List=[4,6,2,1,19,43,21,3,111,7]

List=[2, 3, 5, 9, 3]

def SumOfOddNumbers(List):
    summa = 0 
    for number in List:
        if number % 2:
            summa += number
    return summa

sum_ = SumOfOddNumbers(List)
print('Сумма нечетных чисел - ', sum_)