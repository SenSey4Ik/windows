from tkinter import *
from bs4 import BeautifulSoup
import requests

#Создаем верхнее окно
root = Tk()

#Название окна
root.title('Погода')

#Размеры окна
root.geometry('300x400')

def sinh_pog():
    """Вызываем get запрос 1 раз"""

    #Ссылка на сайт
    url='https://www.meteovesti.ru/pogoda_10/29947'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    #Отправляем запрос на сайт с командой получить
    response = requests.get(url, headers=headers)

    # просим у сайта вернуть красиво отформатированный текст
    soup = BeautifulSoup(response.text, 'lxml')

    #Парсим класс в котором хранится погода
    data = soup.find('span', class_="_h3 align-top me-1 d-inline-block").text

    label_gradusi = Label(root, text=f'{data}')
    label_gradusi.pack()



#Чтобы никто не мог изменять параметры окна
root.resizable(width=False, height=False)


#Тексты
label_city = Label(root, text= 'город: Бийск',font=40,bg='yellow',)
label_city.pack(pady=20)

label_temp = Label(root, text=f'Температура:\n', font=40)
label_temp.pack(pady=70)

#Кнопки
button = Button(root, text='Узнать погоду',font=40,command=sinh_pog)
button.pack(side=BOTTOM, pady=40)




#Цикл, чтобы окно не закрывалось
root.mainloop()