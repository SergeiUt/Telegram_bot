from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='Вставьте сюда свой токен', parse_mode='html') # создание бота

faker = Faker() # утилита для генерации номеров кредитных карт

# объект клавиаутры
card_type_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
card_type_keyboard.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)
# второй ряд кнопок
card_type_keyboard.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Какую банковскую карту нужно сгенерировать?\nВыбери тип карты:', # текст сообщения
        reply_markup=card_type_keyboard,
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # проверяем текст сообщения на совпадение с текстом какой либо из кнопок
    # в зависимости от типа карты присваем занчение переменной 'card_type'
    if message.text.lower() == 'visa':
        card_type = 'visa'
    elif message.text.lower() == 'mastercard':
        card_type = 'mastercard'
    elif message.text.lower() == 'maestro':
        card_type = 'maestro'
    elif message.text.lower() == 'jcb':
        card_type = 'jcb'
    else:
        # если введен другой тект, то выводим подсказку
        bot.send_message(
            chat_id=message.chat.id,
            text='Можно выбрать только четыре вида карт: VISA, Mastercard, Maestro и JCB',
        )
        return

    # получаем номер тестовой карты выбранного типа
    # card_type может принимать одно из зачений ['maestro', 'mastercard', 'visa13', 'visa16', 'visa19',
    # 'amex', 'discover', 'diners', 'jcb15', 'jcb16']
    card_number = faker.credit_card_number(card_type)
    # и выводим пользователю
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Тестовая карта {card_type}:\n<code>{card_number}</code>'
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
