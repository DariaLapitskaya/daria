import telebot

bot = telebot.TeleBot('1855601212:AAGVAVsvu6yHiXy8HIe5vNCugefhHTb6qYE')

auto = list()
time = list()
mileage = list()

@bot.message_handler(content_types=['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Здравствуйте! Напишите "Старт" для начала расчета')
	bot.register_next_step_handler(message, get_start)

def get_start(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if (message.text == "Привет"):
		bot.send_message(message.chat.id, 'Выберете автомобиль: Газель Некст или Газон Некст')
		bot.register_next_step_handler(message, get_auto)
	else:	
		bot.send_message(message.chat.id, 'Ошибка. Попробуйте еще раз')
		start(message)

def get_auto(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if (message.text == "Газель Некст"):	
		bot.send_message(message.chat.id, 'Укажите срок аренды автомобиля в месяцах: от 6 до 36 месяцев')
		bot.register_next_step_handler(message, get_time)
		auto.append(10)
	elif (message.text == "Газон Некст"):
		bot.send_message(message.chat.id, 'Укажите срок аренды автомобиля в месяцах: от 6 до 36 месяцев')
		bot.register_next_step_handler(message, get_time)
		auto.append(15)
	else:	
		bot.send_message(message.chat.id, 'Ошибка. Попробуйте еще раз')
		get_start(message)

def get_time(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	while message.text in range (6, 37):	
		bot.send_message(message.chat.id, 'Определите необходимый средний пробег автомобиля за год: от 30000 до 100000')
		bot.register_next_step_handler(message, get_mileage)
		time.append(message.text)
	else:	
		bot.send_message(message.chat.id, 'Ошибка. Попробуйте еще раз')
	bot.register_next_step_handler(message, get_mileage)

def get_mileage(message):
	mileage = message.text
			
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