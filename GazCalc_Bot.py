import telebot
from telebot import types

bot = telebot.TeleBot('1855601212:AAGVAVsvu6yHiXy8HIe5vNCugefhHTb6qYE')

@bot.message_handler(content_types=['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Напишите "Старт" для начала расчета')
	bot.register_next_step_handler(message, get_auto) 
	
def get_auto(message):
	if message.text == 'Старт':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		button_auto1 = types.KeyboardButton('Газель Некст')
		button_auto2 = types.KeyboardButton('Газон Некст')
		keyboard.add(button_auto1, button_auto2)
		bot.send_message(message.chat.id, 'Выберете автомобиль', reply_markup = keyboard)
		bot.register_next_step_handler(message, get_time)
	else:
		bot.send_message(message.from_user.id, 'Ошибка. Попробуйте еще раз')

def get_time(message):
	bot.send_message(message.from_user.id, 'Отлично!')
	bot.send_message(message.from_user.id, 'Следующий шаг...')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_time1 = types.KeyboardButton('6 месяцев')
	button_time2 = types.KeyboardButton('1 год')
	button_time3 = types.KeyboardButton('1 год 6 месяцев')
	button_time4 = types.KeyboardButton('2 года')
	button_time5 = types.KeyboardButton('1 год 6 месяцев')
	button_time6 = types.KeyboardButton('2 года')
	button_time7 = types.KeyboardButton('2 года 6 месяцев')
	button_time8 = types.KeyboardButton('3 года')
	keyboard.add(button_time1, button_time2, button_time3, button_time4, button_time5, button_time6, button_time7, button_time8)
	bot.send_message(message.chat.id, 'Укажите срок аренды автомобиля', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_mileage)

def get_mileage(message):
	bot.send_message(message.from_user.id, 'Отлично!')
	bot.send_message(message.from_user.id, 'Следующий шаг...')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)	
	button_mileage1 = types.KeyboardButton('30 000')
	button_mileage2 = types.KeyboardButton('40 000')
	button_mileage3 = types.KeyboardButton('50 000')
	button_mileage4 = types.KeyboardButton('60 000')
	button_mileage5 = types.KeyboardButton('70 000')
	button_mileage6 = types.KeyboardButton('80 000')
	button_mileage7 = types.KeyboardButton('90 000')
	button_mileage8 = types.KeyboardButton('100 000')
	keyboard.add(button_mileage1, button_mileage2, button_mileage3, button_mileage4, button_mileage5, button_mileage6, button_mileage7, button_mileage8)
	bot.send_message(message.chat.id, 'Определите необходимый средний пробег автомобиля за год', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_mileagee)
			
def get_mileagee(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	m = list(range(30000, 110000, 10000))
	if message.text != m:
		bot.send_message(message.chat.id, 'Ошибка. Попробуйте еще раз')	
		return
		bot.send_message(message.from_user.id, 'Определите необходимый средний пробег автомобиля за год: от 30000 до 100000')
	else:
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу GAZ CONNECT')
		bot.register_next_step_handler(message, get_add1)

def get_add1(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text == 'Да':
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу подменного парка')
		bot.register_next_step_handler(message, get_add2)
	else:
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу подменного парка')
		bot.register_next_step_handler(message, get_add2)

def get_add2(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text == 'Да':
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу консьерж-сервиса')
		bot.register_next_step_handler(message, get_add3)
	else:
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу консьерж-сервиса')
		bot.register_next_step_handler(message, get_add3)

def get_add3(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text == 'Да':
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу защиты от поломок')
		bot.register_next_step_handler(message, get_add4)
	else:
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу защиты от поломок')
		bot.register_next_step_handler(message, get_add4)

def get_add4(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text == 'Да':
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу обучения водителей')
		bot.register_next_step_handler(message, get_add5)
	else:
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Следующий шаг...')
		bot.send_message(message.from_user.id, 'Напишите "Да", если хотите добавить услугу обучения водителей')
		bot.register_next_step_handler(message, get_add5)

def get_add5(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text == 'Да':
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Напишите "Итог" для получения предварительной суммы аренды')
		bot.register_next_step_handler(message, finish)
	else:
		bot.send_message(message.from_user.id, 'Отлично!')
		bot.send_message(message.from_user.id, 'Напишите "Итог" для получения предварительной суммы аренды')
		bot.register_next_step_handler(message, finish)

def finish(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text != 'Итог':
		bot.send_message(message.chat.id, 'Ошибка. Попробуйте еще раз')
		return
		bot.send_message(message.from_user.id, 'Напишите "Итог" для получения предварительной суммы аренды')
	else:	
		bot.send_message(message.from_user.id, 'Отлично!')
			
bot.polling()

"""
хотим создать калькулятор аренды автомобиля

шаг 1. выберите автомобиль
создаем словарь, где ключи - модификации автомобилей, а их значения - стоимость
дать выбрать пользователю модификацию автомобиля 

шаг 2. укажите срок аренды
создаем список с числовыми значениями от 6 до 36
дать выбрать пользователю срок
умножить срок на значение ключа из словаря 


шаг 3. определите необходимый средний пробег автомобиля
создаем список с числовыми значениями от 30000 до 100000
дать выбрать пользователю пробег
если 30000
	умножить выбранное значение на 1,1 рубля и поделить на 12
если 40000
	умножить выбранное значение на 1,3 рубля и поделить на 12
если 50000
	умножить выбранное значение на 1,5 рубля и поделить на 12
если 60000
	умножить выбранное значение на 1,6 рубля и поделить на 12
если 70000
	умножить выбранное значение на 1,8 рубля и поделить на 12
если 80000
	умножить выбранное значение на 2,1 рубля и поделить на 12
если 90000
	умножить выбранное значение на 2,3 рубля и поделить на 12
если 100000
	умножить выбранное значение на 2,5 рубля и поделить на 12
вывести пользователю полученное значение ("Стоимость сервисного контракта за месяц")
умножить полученное значение на срок
вывести пользователю полученное значение ("Стоимость сервисного контракта за период")
сложить значения: шаг 2 + шаг 3


шаг 4. выберите дополнитьльные услуги
создаем словарь, где ключи - дополнительные услуги, а их значения - стоимость
дать выбрать пользователю дополнительные услуги
умножить значение ключа (выбранной услуги) на срок
сложить значения: шаг 3 + шаг 4


вывести результат ("Сумма платежа за период")
вывести результат поделенный на срок аренды ("Сумма платежа в месяц")
"""