import telebot
import webbrowser
bot = telebot.TeleBot('6188529571:AAFmPr7jXeT1t53FLRHC25ol5YNWFgD-rOk')

@bot.message_handler(commands=['site'])
def web_site(message):
	webbrowser.open("url....")
	

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "salom")
	
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "<b><u>Yordam ber</u></b>", parse_mode='html')
	
@bot.message_handler(commands=['info'])
def send_welcome(message):
	bot.send_message(message.chat.id, f'Salom, {message.from_user.first_name} {message.from_user.last_name}')
	
@bot.message_handler()
def get(message):
	if message.text.lower() == 'salom':
		bot.send_message(message.chat.id, f'Salom, {message.from_user.first_name} {message.from_user.last_name}')
	elif message.text.lower() == 'id':
		bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)