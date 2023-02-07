# Уравнение: (x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Решение на Python

import math # Импортируем модуль math для работы с тригонометрическими функциями
import numpy as np # Импортируем модуль numpy для работы с массивами
import matplotlib as plt # Импортируем модуль matplotlib для построения графиков

# Определяем функцию
def func(x):
    return -12*x**4*math.sin(math.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

# Определяем корни уравнения
roots = np.roots([-12, 0, -18, 5, 10, -30])
print('Корни уравнения:', roots)

# Находим интервалы, на которых функция возрастает
x = np.arange(roots[0], roots[1], 0.01)
y = [func(i) for i in x]
for i in range(len(y) - 1):
    if y[i] < y[i + 1]:
        print(f'Функция возрастает на участке от {x[i]:.2f} до {x[i + 1]:.2f}')

# Находим интервалы, на которых функция убывает
x = np.arange(roots[1], roots[2], 0.01)
y = [func(i) for i in x]
for i in range(len(y) - 1):
    if y[i] > y[i + 1]:
        print(f'Функция убывает на участке от {x[i]:.2f} до {x[i + 1]:.2f}')

# Построим график
x = np.arange(-5, 5, 0.01)
y = [func(i) for i in x]
plt.plot(x, y)
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

# Найдем вершину
x_max = np.argmax(y)
y_max = y[x_max]
print(f'Вершина функции находится в точке ({x[x_max]:.2f}, {y_max:.2f})')