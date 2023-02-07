# Импортируем библиотеку для работы с функциями
import numpy as np

# Определяем функцию
def f(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

# Находим корни уравнения
roots = np.roots([-12, 0, -18, 5, 10, -30])

# Находим интервалы, на которых функция возрастает
x_values = np.linspace(roots[0], roots[-1], 1000)
increasing_intervals = []
for i in range(len(x_values) - 1):
    if f(x_values[i]) < f(x_values[i+1]):
        increasing_intervals.append((x_values[i], x_values[i+1]))

# Находим интервалы, на которых функция убывает
decreasing_intervals = []
for i in range(len(x_values) - 1):
    if f(x_values[i]) > f(x_values[i+1]):
        decreasing_intervals.append((x_values[i], x_values[i+1]))

# Построим график функции
import matplotlib.pyplot as plt
plt.plot(x_values, f(x_values))
plt.show()

# Найдем вершину графика
maximum = max(f(x_values))
maximum_x = x_values[np.argmax(f(x_values))]
print('Вершина графика: x = {}, y = {}'.format(maximum_x, maximum))