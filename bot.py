import telebot
import wikipediaapi

lang = 'ru'
wiki = wikipediaapi.Wikipedia(lang)
bot = telebot.TeleBot('5040471321:AAEsAZpzc23cvKKHZEXza-mu0VPJg-WUFd0', parse_mode='markdown')

@bot.message_handler(commands=['help', 'start'])
def send_hello(msg):
    bot.send_message(msg.chat.id, 'Type /ru or /en to change Wikipedia language\n')

@bot.message_handler(commands=['ru', 'en'])
def send_hello(msg):
    global lang
    lang = msg.text[1:]
    global wiki
    wiki = wikipediaapi.Wikipedia(lang)
    bot.send_message(msg.chat.id, 'Language has changed to ' + msg.text)


@bot.message_handler(func=lambda m: True)
def send_welcome(msg):
    page = wiki.page(msg.text)
    if page.exists():
        bot.send_message(msg.chat.id, page.summary[0:1000] + '... ' + f'[read more](http://{lang}.wikipedia.org/wiki/{msg.text})')
    else:
        bot.send_message(msg.chat.id, 'Sorry, the page you are looking for does not exist \nTry to change the language or reformulate the request')


print('Bot started polling...')
bot.infinity_polling()