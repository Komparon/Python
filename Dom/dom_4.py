# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print(100*'\n')
print('Введите номер четверти:')

x = int(input('Четверть номер = '))

if x == 1:
    print ('- по 0:Х и что-то по оу')
elif x==2:
    print('+ по 0:Х  и что-то по оу')
elif x==3:
    print('по 0:Х  и что-то по оу')
else:
    print('что-то по ох и что-то по оу')
