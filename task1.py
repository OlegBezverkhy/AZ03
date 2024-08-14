import matplotlib.pyplot as plt
from numpy.random import normal

# Параметры нормального распределения
# Среднее значение:
mean = 0
# Стандартное отклонение:
std_dev = 1
# Количество образцов:
num_samples = 1000

def main():
    # Генерация случайных чисел, распределенных по нормальному распределению
    data = normal(mean, std_dev, num_samples)
    # Строим гистограмму:
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=1000)
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title(f'Нормальное распределение с показателями: среднее={mean} стандартное отклонение={std_dev}')
    # Показываем график:
    plt.show()

if __name__ == '__main__':
    main()
