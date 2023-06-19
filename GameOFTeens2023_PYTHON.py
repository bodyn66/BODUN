import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('Bot Token')


@bot.message_handler(commands=['about'])
def about(message):
    bot.send_photo(message.chat.id,'https://imgtr.ee/images/2023/06/17/YdrbF.jpg', caption="«Lifecell» » — українська телекомунікаційна компанія, третій за величиною оператор мобільного зв'язку в Україні. Належить компанії Euroasia Telecommunications Holding BV, якою в свою чергу володіє турецький оператор Turkcell. Ми прагнемо до швидкого та якісно зв'зку на відстані щоб ви могли говорити з рідними та друзями навіть за з-закордону ")
    bot.send_message(message.chat.id, "В нашому боті також є корисні команди якими ви можете скористатися:\n /start - початок користування нашим ботом \n /about - більше про нас та список команд \n /site - посилання на наш офіційний сайт \n /support - наша служба підтримка \n /shop - карта наших магазинів \n /application - наш додаток на телефон \n /privacy - наша політика конфіденційності")


@bot.message_handler(commands=['site'])
def about(message):
    bot.send_photo(message.chat.id,"https://imgtr.ee/images/2023/06/17/YddR0.jpg", caption="Посилання на наш " + "[офіційний сайт](https://www.lifecell.ua/uk/pro_lifecell/golovna/)", parse_mode='Markdown')

@bot.message_handler(commands=['support'])
def about(message):
    bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Yd1hM.jpg", caption="Якщо у вас виникли запитання або проблеми ви можете звернутися до служби " + "[підримки Lifecell](https://www.lifecell.ua/uk/pidtrimka/)", parse_mode='Markdown')

@bot.message_handler(commands=['shop'])
def about(message):
    bot.send_photo(message.chat.id,"https://imgtr.ee/images/2023/06/17/YdwbD.jpg", caption="Якщо ви шукаєте наш магазин або центр ви можете знайти його на " + "[цій карті](https://www.lifecell.ua/uk/tsentry-obslugovuvannya-abonentiv/)", parse_mode='Markdown')

@bot.message_handler(commands=['application'])
def about(message):
    bot.send_photo(message.chat.id,"https://imgtr.ee/images/2023/06/17/Ydpl1.jpg", caption="Завантажте наш додаток щоб швидко та зручно скористатися нашими послугами та перевірити свій тариф\n " + "[Посилання на скачування](https://play.google.com/store/apps/details?id=com.life.my&hl=ua&pli=1)", parse_mode='Markdown')

@bot.message_handler(commands=['privacy'])
def about(message):
    bot.send_photo(message.chat.id,"https://imgtr.ee/images/2023/06/17/YdYY3.jpg", caption="Посилання для перегляду нашої " + "[політики конфіденційності](https://ds.lifecell.ua/page/45)", parse_mode='Markdown')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Пройти Опитування')
    markup.add(btn1)
    bot.send_photo(message.from_user.id,"https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Logo_lifecell.jpg/800px-Logo_lifecell.jpg", caption=f'Вітаю👋 ,{message.from_user.first_name} я твій бот помічник від компанії Lifecell. Давай разом знайдемо для тебе найліпший тариф!\nВи можете дізнатись більше за допомогою команди /about', reply_markup=markup)
    bot.send_message(message.chat.id, "Для цього вам потрібно відповісти на п'ять простих запитань🧑‍💻")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Пройти Опитування':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #1 batton
        btn1 = types.KeyboardButton('0-150 грн')
        btn2 = types.KeyboardButton('150-250, 375 грн')
        btn3 = types.KeyboardButton('250-500 грн')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3,btn4)
        bot.send_message(message.from_user.id, '💵 В якій ціновій категорії повинен бути ваш тариф ?', reply_markup=markup)
    if message.text == '0-150 грн':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #2 batton
        btn1 = types.KeyboardButton('0-500 МБ')
        btn2 = types.KeyboardButton('0-8 ГБ')
        btn3 = types.KeyboardButton('8-25 ГБ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3,btn4)
        bot.send_message(message.from_user.id, '🌐 Скільки вам потрібно ГБ інтернету ?', reply_markup=markup)
    if message.text == '150-250, 375 грн':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('20-50 ГБ')
        btn2 = types.KeyboardButton('50-∞ ГБ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4 )
        bot.send_message(message.from_user.id, '🌐 Скільки вам потрібно ГБ інтернету ?', reply_markup=markup)
    if message.text == '250-500 грн':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('50 ГБ')
        btn2 = types.KeyboardButton('50-∞ ГБ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '🌐 Скільки вам потрібно ГБ інтернету ?', reply_markup=markup)
    if message.text == '0-500 МБ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #3 batton
        btn1 = types.KeyboardButton('15 хв')
        btn2 = types.KeyboardButton('50 хв')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '📞 Скільки вам потрібно хвилин  ?', reply_markup=markup)
    if message.text == '0-8 ГБ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('300 хв')
        btn2 = types.KeyboardButton('Безліміт хв')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '📞 Скільки вам потрібно хвилин  ?', reply_markup=markup)
    if message.text == '8-25 ГБ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('300 хв')
        btn2 = types.KeyboardButton('800 хв')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4 )
        bot.send_message(message.from_user.id, '📞 Скільки вам потрібно хвилин  ?', reply_markup=markup)
    if message.text == '20-50 ГБ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('800 хв')
        btn2 = types.KeyboardButton('500 хв')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '📞 Скільки вам потрібно хвилин  ?', reply_markup=markup)
    if message.text == '50 ГБ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1500 хв')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4)
        bot.send_message(message.from_user.id, '📞 Скільки вам потрібно хвилин  ?', reply_markup=markup)
    if message.text == '50-∞ ГБ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1600 хв')
        btn2 = types.KeyboardButton('3000 хв')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '📞 Скільки вам потрібно хвилин  ?', reply_markup=markup)
       #SMS SMS SMS SMSㅤ
    #---------------------------------------------------------------------------------------------------------------------
    if message.text == '15 хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #+
        btn1 = types.KeyboardButton('Такㅤ')
        btn2 = types.KeyboardButton('Ніㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
    if message.text == '50 хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #
        btn1 = types.KeyboardButton('Такㅤㅤ')
        btn2 = types.KeyboardButton('Ніㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
    if message.text == '300 хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #+
        btn1 = types.KeyboardButton('Такㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ніㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
    if message.text == 'Безліміт хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #
        btn1 = types.KeyboardButton('Такㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ніㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
    if message.text == '800 хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #
        btn1 = types.KeyboardButton('Такㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ніㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
    if message.text == '500 хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #+
        btn1 = types.KeyboardButton('Такㅤㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ніㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
    if message.text == '1500 хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #+
        btn1 = types.KeyboardButton('Такㅤㅤㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ніㅤㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
    if message.text == '1600 хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Такㅤㅤㅤㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ніㅤㅤㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
    if message.text == '3000 хв':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Такㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ніㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_message(message.from_user.id, '💬 Чи потрібні вам SMS ?', reply_markup=markup)
#--------------------------------------------------------------------------------------------------------------------
    if message.text == 'Такㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # +
        btn1 = types.KeyboardButton('Визначити тарифㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4)
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Такㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тариф без смсㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4)
        bot.send_message(message.from_user.id, 'Нажаль такого пакета з SMS нема😥', reply_markup=markup)
    if message.text == 'Визначити тариф без смсㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2
        btn1 = types.KeyboardButton('Так, Підходитьㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6FsY.jpg")
        bot.send_message(message.from_user.id,
                         'Тариф Ґаджет Смарт 🌐Інтернет: 500 МБ на день ,📞Дзвінки 50 хв на день  ,💬50 SMS , Ціна 150 грн/4 тижні. Чи підходить вам цей тариф ?',
                         reply_markup=markup)
    if message.text == 'Такㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # +
        btn1 = types.KeyboardButton('Визначити тариф без смс')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Нажаль такого пакета з SMS нема😥', reply_markup=markup) # 0-150 0-8 300
    if message.text == 'Визначити тариф без смс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 3
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y63AD.jpg")
        bot.send_message(message.from_user.id,
                         'Тариф Просто Лайф 🌐Інтернет: 8 ГБ ,📞Дзвінки 300 хв  ,  Ціна 90 грн/4 тижні. Чи підходить вам цей тариф ?',
                         reply_markup=markup)

    if message.text == 'Такㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тариф без смсㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4)
        bot.send_message(message.from_user.id, 'Нажаль такого пакета з SMS нема😥', reply_markup=markup)
    if message.text == 'Визначити тариф без смсㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 4
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6jSs.jpg")
        bot.send_message(message.from_user.id, 'Тариф Шкільний Лайф 🌐Інтернет: 7 ГБ ,📞Дзвінки Безліміт  ,  Ціна 150 грн/4 тижні. Чи підходить вам цей тариф ?', reply_markup=markup)
    if message.text == 'Такㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тариф без смсㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Нажаль такого пакета з SMS нема😥', reply_markup=markup) # 0-150 8-25 800
    if message.text == 'Визначити тариф без смсㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 5
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6gFX.jpg")
        bot.send_message(message.from_user.id,'Тариф Смарт Лайф 🌐Інтернет: 25 ГБ ,📞Дзвінки 800 хв ,  Ціна 120 грн/4 тижні. Чи підходить вам цей тариф ?',reply_markup=markup)
    if message.text == 'Такㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # +
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Такㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # +
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Такㅤㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тариф без смсㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Нажаль такого пакета з SMS нема😥', reply_markup=markup)
    if message.text == 'Визначити тариф без смсㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 8
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6gFX.jpg")
        bot.send_message(message.from_user.id,"Тариф Вільний Лайф 🌐Інтернет: Безліміт ,📞Дзвінки 1600 хв ,  Ціна 180 грн/4 тижні. Чи підходить вам цей тариф ?",reply_markup=markup)
    if message.text == 'Такㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
#-----------------------------------------------------------------------------------------------------------------
    if message.text == 'Ніㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #   #символ(ㅤ)
        btn1 = types.KeyboardButton('Визначити тарифㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Ніㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Ніㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Ніㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Ніㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Ніㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Ніㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Ніㅤㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
    if message.text == 'Ніㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Визначити тарифㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4 )
        bot.send_message(message.from_user.id, 'Все готово для визначення тарифу !', reply_markup=markup)
#------------------------------------------------------------------------------------------------------------------
    if message.text == 'Визначити тарифㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 1
        btn1 = types.KeyboardButton('Так, Підходить')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6XL1.jpg")
        bot.send_message(message.from_user.id, 'Тариф Ґаджет Безпека🌐Інтернет: 150 МБ на день ,📞Дзвінки 15 хв на день  ,💬15 SMS , Ціна 90 грн/12 тижнів. Чи підходить вам цей тариф ?', reply_markup=markup)
    if message.text == 'Так, Підходить':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # +
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти за посиланням:\n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/ \nі заказати Пакет')
    if message.text == 'Визначити тарифㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2
        btn1 = types.KeyboardButton('Так, Підходитьㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6FsY.jpg")
        bot.send_message(message.from_user.id, 'Тариф Ґаджет Смарт 🌐Інтернет: 500 МБ на день ,📞Дзвінки 50 хв на день  ,💬SMS 50 SMS , Ціна 150 грн/4 тижні. Чи підходить вам цей тариф ?', reply_markup=markup)
    if message.text == 'Так, Підходитьㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # +
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти за посиланням:\nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/ \nі заказати Пакет')
    if message.text == 'Визначити тарифㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 3
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y63AD.jpg")
        bot.send_message(message.from_user.id, 'Тариф Просто Лайф 🌐Інтернет: 8 ГБ ,📞Дзвінки 300 хв  ,  Ціна 90 грн/4 тижні. Чи підходить вам цей тариф ?', reply_markup=markup)
    if message.text == 'Так, Підходитьㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # +
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти за посиланням:\nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/ \nі заказати Пакет')
    if message.text == 'Визначити тарифㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 4
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6jSs.jpg")
        bot.send_message(message.from_user.id, 'Тариф Шкільний Лайф 🌐Інтернет: 7 ГБ ,📞Дзвінки Безліміт  ,  Ціна 150 грн/4 тижні. Чи підходить вам цей тариф ?', reply_markup=markup)
    if message.text == 'Так, Підходитьㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # +
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти а посиланням:\nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/ \nі заказати Пакет')
    if message.text == 'Визначити тарифㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 5
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6gFX.jpg")
        bot.send_message(message.from_user.id,'Тариф Смарт Лайф 🌐Інтернет: 25 ГБ ,📞Дзвінки 800 хв ,  Ціна 120 грн/4 тижні. Чи підходить вам цей тариф ?',reply_markup=markup)
    if message.text == 'Так, Підходитьㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти за посиланням:\nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/ \nі заказати Пакет')
    if message.text == 'Визначити тарифㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 6
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6iOq.jpg")
        bot.send_message(message.from_user.id,"Тариф Смарт Сім'я S 🌐Інтернет: 20 ГБ ,📞Дзвінки 500 хв ,  Ціна 375 грн/4 тижні. Можливість об'єднувати до 5 номерів lifecell та користуватися спільно інтернетом, хвилинами та SMS пакету послуг тарифного плану.\nЧи підходить вам цей тариф ?",reply_markup=markup)
    if message.text == 'Так, Підходитьㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти за посиланням:\nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/ \nі заказати Пакет')
    if message.text == 'Визначити тарифㅤㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 8
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6gFX.jpg")
        bot.send_message(message.from_user.id,"Тариф Вільний Лайф 🌐Інтернет: Безліміт ,📞Дзвінки 1600 хв ,  Ціна 180 грн/4 тижні. Чи підходить вам цей тариф ?",reply_markup=markup)
    if message.text == 'Так, Підходитьㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти за посиланням:\nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/ \nі заказати Пакет')
    if message.text == 'Визначити тарифㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #  7
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2, btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6iOq.jpg")
        bot.send_message(message.from_user.id,"Тариф Смарт Сім'я L 🌐Інтернет: 50ГБ ,📞Дзвінки 1500 хв ,  Ціна 500 грн/4 тижні. Можливість об'єднувати до 5 номерів lifecell та користуватися спільно інтернетом, хвилинами та SMS пакету послуг тарифного плану.\nЧи підходить вам цей тариф ?",reply_markup=markup)
    if message.text == 'Так, Підходитьㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти за посиланням:\nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/ \nі заказати Пакет')
    if message.text == 'Визначити тарифㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 5
        btn1 = types.KeyboardButton('Так, Підходитьㅤㅤㅤㅤㅤㅤㅤㅤ')
        btn2 = types.KeyboardButton('Ні, не підходить')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2,btn4)
        bot.send_photo(message.chat.id, "https://imgtr.ee/images/2023/06/17/Y6PHM.jpg")
        bot.send_message(message.from_user.id,'Тариф Platinum Лайф 🌐Інтернет: Безліміт ,📞Дзвінки 3000 хв , 💬50 SMS,  Ціна 250 грн/4 тижні. Чи підходить вам цей тариф ?',reply_markup=markup)
    if message.text == 'Так, Підходитьㅤㅤㅤㅤㅤㅤㅤㅤ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_photo(message.from_user.id, "https://imgtr.ee/images/2023/06/17/YxmWs.jpg", caption=f'Тоді ви можете перейти за посиланням:\nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/ \nі заказати Пакет')
    if    message.text == 'Ні, не підходить':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #
        btn1 = types.KeyboardButton('Пройти Опитування')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1,btn4)
        bot.send_message(message.from_user.id, 'Тоді ви можете пройти опитуваня ще раз!', reply_markup=markup)
    if message.text == 'Назад':
        start(message)
#------------------------------------------------------------------------------------------------------------------



bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
