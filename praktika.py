"""
хотим калькулятор выражений -2 + 3.5 * 2 - 3 ^ 2
"""

#считать строчку от пользователя

#почистить строку
#"-2 + 3.5 * 2 - 3 ^ 2" -> "-2+3.5*2-3^2"

#распарсить

""""
на вход строку
(+ * - ^)
(-2 3.5 2 3 2)
на выход ?структура данных? с операциями +- и значениями
""""

#вычислить операции 1го приоритета (возведение в степень)

"""
на вход наш набор значение и операции
на выход обновленная ?структура данных? с операциями +- и значениями

-2 + 3.5 * 2 - 3 ^ 2
-2 + 3.5 * 2 - 9
""""

#вычислить операции 2го приоритета (умножение и деление)

"""
на вход наш набор значение и операции
на выход обновленная ?структура данных? с операциями +- и значениями

-2 + 3.5 * 2 - 9
-2 + 7 - 9
""""

#вычислить операции 3го приоритета (сложение и вычитание)

#-2 + 7 - 9 = -4

#вывести результат

