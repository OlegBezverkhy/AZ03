import csv
import matplotlib.pyplot as plt
from os import path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from time import sleep


URL = 'https://www.divan.ru/volgograd/category/divany-i-kresla'
OUTPUT_FILE = 'output_price.csv'
SLEEP_TIME = 3

def check_browser_and_launch():
    ''' Определяет установленный браузер. Если это не Chrome или Firefox, то
    сообщает об ошибке'''
    # Путь к Chrome
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    # Путь к Firefox
    firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

    chrome_installed = path.exists(chrome_path)
    firefox_installed = path.exists(firefox_path)

    if chrome_installed:
        print('Найден браузер Chrome.')
        try:
            # Запуск Chrome через Selenium
            current_browser = webdriver.Chrome()
            return current_browser
        except WebDriverException as er:
            print(f'Ошибка при запуске Chrome: {er}')
    elif firefox_installed:
        print('Найден браузер Firefox.')
        try:
            # Запуск Firefox через Selenium
            current_browser = webdriver.Firefox()
            return current_browser
        except WebDriverException as er:
            print(f'Ошибка при запуске Firefox: {er}')
    else:
        print('Ни один из браузеров (Chrome или Firefox) не найден.')
        exit(1)


def clean(price):
    ''' Очищает данные переданные в переменной price от пробелов и выражения "руб."
    преобразует в целочисленный тип '''
    return int(price.replace('руб.', '').replace(' ', ''))


def histograma(data):
    ''' Построоение диаграмм'''
    plt.figure(figsize=(10, 6))
    plt.title(f'Гистограмма цен диванов c сайта:  {URL}')
    plt.xlabel('Цена дивана')
    plt.ylabel('Частота')
    plt.hist(data, bins=20, edgecolor='white')
    plt.show()


def main():
    print('Программа работает только с браузерами Chrome или Firefox. Проверьте их наличие')
    browser = check_browser_and_launch()
    browser.get(URL)
    sleep(SLEEP_TIME)

    #Парсинг цен и очистка данных
    prices = browser.find_elements(By.XPATH, '//div[@class="pY3d2"]//span[@data-testid="price"]')
    clean_prices = [clean(price.text) for price in prices]

    # Записываем очищенные даннные в файл
    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Записываем заголовок столбца
        writer.writerow(['Price'])
        for price in clean_prices:
            writer.writerow([price])
    print(f'Данные сохранены в файл {OUTPUT_FILE}')

    # Построение гистограммы
    histograma(clean_prices)

    # Закрытие драйвера
    browser.quit()

if __name__ == '__main__':
    main()