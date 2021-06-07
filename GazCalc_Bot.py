import telebot
from telebot import types

bot = telebot.TeleBot('1855601212:AAGVAVsvu6yHiXy8HIe5vNCugefhHTb6qYE')

result = []

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
		bot.send_message(message.chat.id, 'Выберите автомобиль', reply_markup = keyboard)
		bot.register_next_step_handler(message, get_time)
	else:
		bot.send_message(message.from_user.id, 'Ошибка. Попробуйте еще раз')
	

def get_time(message):
	if message.text == 'Газель Некст':
		auto = 33639
		result.append(auto)
	else:
		auto = 48086
		result.append(auto)
	bot.send_message(message.from_user.id, 'Следующий шаг...')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_time1 = types.KeyboardButton('6 месяцев')
	button_time2 = types.KeyboardButton('1 год')
	button_time3 = types.KeyboardButton('1 год 6 месяцев')
	button_time4 = types.KeyboardButton('2 года')
	button_time5 = types.KeyboardButton('2 год 6 месяцев')
	button_time6 = types.KeyboardButton('3 года')
	keyboard.add(button_time1, button_time2, button_time3, button_time4, button_time5, button_time6)
	bot.send_message(message.chat.id, 'Укажите срок аренды', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_mileage)

def get_mileage(message):
	if message.text == '6 месяцев':
		time = 6
		result.append(time)
	elif message.text == '1 год':
		time = 12
		result.append(time)
	elif message.text == '1 год 6 месяцев':
		time = 18
		result.append(time)
	elif message.text == '2 года':
		time = 24
		result.append(time)
	elif message.text == '2 год 6 месяцев':
		time = 30
		result.append(time)
	else:
		time = 36
		result.append(time)
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
	bot.send_message(message.chat.id, 'Определите необходимый средний пробег за год', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_add1)
			
def get_add1(message):
	if message.text == '30 000':
		mileage = 2750
		result.append(mileage)
	elif message.text == '40 000':
		mileage = 4333
		result.append(mileage)
	elif message.text == '50 000':
		mileage = 6250
		result.append(mileage)
	elif message.text == '60 000':
		mileage = 8000
		result.append(mileage)
	elif message.text == '70 000':
		mileage = 10500
		result.append(mileage)
	elif message.text == '80 000':
		mileage = 14000
		result.append(mileage)
	elif message.text == '90 000':
		mileage = 17250
		result.append(mileage)
	else:
		mileage = 20833
		result.append(mileage)
	bot.send_message(message.from_user.id, 'Следующий шаг...')
	bot.send_message(message.from_user.id, 'Выберите дополнительные услуги')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)	
	button_add1 = types.KeyboardButton('Да, добавить GAZ CONNECT')
	button_add2 = types.KeyboardButton('Нет, пропустить шаг')
	keyboard.add(button_add1, button_add2)
	bot.send_message(message.chat.id, 'Хотите добавить GAZ CONNECT?', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_add2)

def get_add2(message):
	if message.text == 'Да, добавить GAZ CONNECT':
		add1 = 100
		result.append(add1)
	else:
		add1 = 0
		result.append(add1)
	bot.send_message(message.from_user.id, 'Следующий шаг...')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)	
	button_add3 = types.KeyboardButton('Да, добавить подменный автомобиль')
	button_add4 = types.KeyboardButton('Нет, пропустить шаг')
	keyboard.add(button_add3, button_add4)
	bot.send_message(message.chat.id, 'Хотите добавить подменный автомобиль?', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_add3)

def get_add3(message):
	if message.text == 'Да, добавить подменный автомобиль':
		add2 = 2500
		result.append(add2)
	else:
		add2 = 0
		result.append(add2)
	bot.send_message(message.from_user.id, 'Следующий шаг...')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)	
	button_add5 = types.KeyboardButton('Да, добавить консьерж-сервис')
	button_add6 = types.KeyboardButton('Нет, пропустить шаг')
	keyboard.add(button_add5, button_add6)
	bot.send_message(message.chat.id, 'Хотите добавить консьерж-сервис?', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_add4)

def get_add4(message):
	if message.text == 'Да, добавить консьерж-сервис':
		add3 = 250
		result.append(add3)
	else:
		add3 = 0
		result.append(add3)
	bot.send_message(message.from_user.id, 'Следующий шаг...')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)	
	button_add7 = types.KeyboardButton('Да, добавить защиту от поломок')
	button_add8 = types.KeyboardButton('Нет, пропустить шаг')
	keyboard.add(button_add7, button_add8)
	bot.send_message(message.chat.id, 'Хотите добавить защиту от поломок?', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_add5)

def get_add5(message):
	if message.text == 'Да, добавить защиту от поломок':
		add4 = 2500
		result.append(add4)
	else:
		add4 = 0
		result.append(add4)
	bot.send_message(message.from_user.id, 'Следующий шаг...')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)	
	button_add9 = types.KeyboardButton('Да, добавить обучение водителя')
	button_add10 = types.KeyboardButton('Нет, пропустить шаг')
	keyboard.add(button_add9, button_add10)
	bot.send_message(message.chat.id, 'Хотите добавить обучение водителя?', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_finish)

def get_finish(message):
	if message.text == 'Да, добавить обучение водителей':
		add5 = 250
		result.append(add5)
	else:
		add5 = 0
		result.append(add5)
	bot.send_message(message.from_user.id, 'Отлично!')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)	
	button_finish = types.KeyboardButton('Итог')
	keyboard.add(button_finish)
	bot.send_message(message.chat.id, 'Нажмите "Итог", чтобы получить предварительную сумму аренды', reply_markup = keyboard)
	bot.register_next_step_handler(message, finish)
	
def finish(message):
	year = int((result[0]+result[2]+result[3]+result[4]+result[5]+result[6]+result[7])*result[1])
	month = int(year / 12)
	bot.send_message(message.from_user.id, 'Ваш ежемесячный платеж...')
	bot.send_message(message.chat.id, month)
	bot.send_message(message.from_user.id, 'Ваш платеж за выбранный период...')
	bot.send_message(message.chat.id, year)
	
bot.polling()
