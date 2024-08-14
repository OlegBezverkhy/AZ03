import matplotlib.pyplot as plt
from numpy.random import rand

# Количество случайных чисел
quantity = 5
def main():
    # Генерация случайных чисел
    array_first = rand(quantity)
    array_second = rand(quantity)
    print('Первый массив')
    print(array_first)
    print('Второй массив')
    print(array_second)
    # Строим гистограмму:
    plt.figure(figsize=(10, 6))
    plt.scatter(array_first, array_second, color='blue', marker='*')
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title(f'Диаграмма рассеяния')
    plt.grid(True)
    # Показываем график:
    plt.show()

if __name__ == '__main__':
    main()