<h2>Телеграм бот, который генерирует номера банковских карт для тестирования</h2>


## Цели и Задачи
Помочь QA инженеру быстро получить нужный номер карты при тестировании в тестовой среде.

Бот геренирует номера тестовых банковских карт:
* Номера карт проходят проверку на алгоритм Луна
* Можно получить номер карты: Visa, Maestro, Mastercard, JCB


## Используемые библиотеки

* Библиотека `telebot`
* Библиотека `faker`

## Установка на локальном компьютере

1. Скачать проект
   
2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота

3. Создаём виртуальное окружение внутри папки проекта.

Инструкция для пользователей на MacOS:

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

Инструкция для пользователей на Windows (оболочка PowerShell)

``` markdown
python -m venv venv
```

``` markdown
.\venv\Scripts\activate.ps1
```


4. Устанавливаем библиотеки

Для MacOS:

``` markdown
python3 -m pip install pyTelegramBotAPI
```

``` markdown
python3 -m pip install faker
```
Для Windows:

``` markdown
python -m pip install pyTelegramBotAPI
```

``` markdown
python -m pip install faker
```


5. Запуск

Для MacOS:

``` markdown
python3 card_for_test_bot.py
```

Для Windows:

``` markdown
python card_for_test_bot.py
```

## Автор

Сергей Уточкин (http://t.me/Sergio198821)
