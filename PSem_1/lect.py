# print ("hello world")
# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#    
#    Примеры:
#    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90

num1 = int (input ('Введите первое число - '))
num2 = int (input ('Введите второе число - '))
num3 = int (input ('Введите третье число - '))
num4 = int (input ('Введите четвертое число - '))
num5 = int (input ('Введите пятое число - 4'))

max = num1

if (max < num2):
    max = num2
if (max < num3):
    max = num3
if (max < num4):
    max = num4
if (max < num5):
    max = num5    

print(max)