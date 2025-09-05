import requests #Импортируем библиотеку
from bs4 import BeautifulSoup #Библиотека для парсинга
import pandas as pd
import csv
url = 'https://yupest.github.io/nto/%D0%9D%D0%A2%D0%98-2022/site/' #Ссылка на наш сайт
response = requests.get(url) #Скачиваем файл html
soup = BeautifulSoup(response.text, features="html.parser")
table=soup.find('table') #Нужно посмотреть что находиться внутри div со статистикой
table = soup.find('table')
tbody = table.find('tbody')
pet_heads = soup.find('div', class_='pet-head')
pet_cards = soup.find_all('div', class_='pet-head')
# Получаем заголовки
headers = []
headers.append('Название породы')
headers.append('Страна происхождения')
headers.append('Вес минимальный')
headers.append('Вес максимальный')
headers.append('Рост минимальный')
headers.append('Рост максимальный')
headers.append('Продолжительность жизни минимальная')
headers.append('Продолжительность жизни максимальная')
for xd in pet_heads.find_all('div', class_='s-title'):
    if xd.text != '':
        headers.append(xd.text)
print(headers)
# Собираем данные о всех собаках
all_dogs_data = []

# Предположим, что каждая собака в div с классом 'pet-card'
for pet_card in pet_cards:
    dog_data = []
    # Имя собаки
    name = pet_card.find('h1').text
    dog_data.append(name)

    # Характеристики (span внутри pet_card)
    characteristics = pet_card.find_all('span')
    for char in characteristics:
        dog_data.append(char.text)

    all_dogs_data.append(dog_data)
print(all_dogs_data)
# Создание и запись в CSV файл
with open('table_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)

    # Записываем заголовки
    writer.writerow(headers)

    # Записываем данные всех собак
    for dog in all_dogs_data:
        writer.writerow(dog)

    # Далее нужно по аналогии с заголовком записать все данные в таблицу
tbody = soup.find('table').find('tbody')
pet_heads = soup.find('div', class_='pet-head')
# Получаем заголовки
headers = []
data = []
for th in tbody.find_all('th'):
  headers.append(th.text)
# Создание и запись в CSV файл

for tr in pet_heads.find_all('tr'):
      row=[]
      for td in tr.find_all('td'):
        row.append(td.text)
      data.append(row)

csv = pd.DataFrame(data, columns = headers)

csv.to_csv('table_data1.csv', index=False)
df_clean = pd.read_csv('table_data.csv')
# Выводим 5 первых строк
df_clean.head()

print("CSV файл 'table_data.csv' успешно создан!")
