import telebot
import os
import requests as r


token = os.environ.get('TELEGRAM_KEY')
bot = telebot.TeleBot(token)  # сам бот

answers = {
    'help': '''Введи запрос для поиска в формате 
    <i>"GIT запрос язык_программирования"</i> 
    и я дам тебе список ссылок.'''
}


def get_search(query, language='python'):
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': query,
        'l': language
    }
    res = r.get(url, params=params).json()
    message = ''
    for repo in res['items'][:5]:
        message += f'<a href="{repo["svn_url"]}">{repo["name"]}</a>\n'
    return message



@bot.message_handler(commands=['start', 'help'])
def start(message):  # параметр - это сообщение от пользователя
    if message.text == '/start':
        bot.send_message(message.chat.id, f"Hello, {message.chat.username}!👋")
    elif message.text == '/help':
        bot.send_message(message.chat.id, text=answers['help'], parse_mode='html')


@bot.message_handler(content_types=['text'])  # эта функция обрабатывает текст
def text_messages(message):
    if message.text.startswith('GIT'):  # если текст сообщения начинается с букв GIT
        msg = message.text.split()  # разбиваем сообщение на список
        res = get_search(msg[1], msg[2])  # ['GIT', 'requests', 'python']
        ans = "Вот, что я нашел:\n" + res   # объединяем список репозиториев с текстом
        bot.send_message(message.chat.id, text=ans, parse_mode='html')


if __name__ == "__main__":  # это точка входа в приложение, условие будет выполняться только в том случае, если запускается ЭТОТ файл
    bot.polling()
