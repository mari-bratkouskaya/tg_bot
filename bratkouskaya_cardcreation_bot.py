from telebot import TeleBot, types
from faker import Faker

bot = TeleBot(token='TOKEN', parse_mode='html')

faker = Faker()

card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)

card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)

card_type_keybaord.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)

card_type_keybaord.row(
    types.KeyboardButton(text='American Express'),
    types.KeyboardButton(text='Discover'),
)


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    
    bot.send_message(
        chat_id=message.chat.id, 
        text='Hi! I know how to generate a test bank card number\nSelect a card type:', # текст сообщения
        reply_markup=card_type_keybaord,
    )


@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'
    elif message.text == 'Maestro':
        card_type = 'maestro'
    elif message.text == 'JCB':
        card_type = 'jcb'
    elif message.text == 'American Express':
        card_type = 'amex'
    elif message.text == 'Discover':
        card_type = 'discover'
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="I don't understand you :(",
        )
        return

    card_number = faker.credit_card_number(card_type)
    
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Bank card for testing {card_type}:\n<code>{card_number}</code>'
    )

def main():
    
    bot.infinity_polling()


if __name__ == '__main__':
    main()
