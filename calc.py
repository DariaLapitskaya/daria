#simple div

str_command = input("Please type command a + b or a-b: ")

sign_A = ''
str_A = ''

sign_B = ''
str_B = ''

operation = ''

for letter in str_command:
	print(letter)
	if letter == '+' or letter == '-' or letter == '*' or letter == '/' or letter == '^':
		if str_A == '':
			sign_A = letter
		elif operation != '':
			sign_B = letter
		else:
			operation = letter
	else:	
		if operation == '':
			str_A = str_A + letter
		else:
			str_B = str_B + letter

str_A = sign_A + str_A.strip()
str_B = sign_B + str_B.strip()
print(str_A)
print(str_B)

#str_input = input("A: ")

delimoe = float(str_A)
#print(type(delimoe))

#operation = input ("+ / * - ^ : ") 

#str_input2 = input("B: ")
delitel = float(str_B)
#print(type(delitel))
result = None

if operation == '/':
    if delitel == 0:
    	result = 'Inf'
    else:
    	result = delimoe / delitel
#print(type(result))
elif operation == '+':
	result= delimoe + delitel
elif operation == '-':
	result = delimoe - delitel
elif operation == '*':
	result = delimoe * delitel
elif operation == '^':
	result = delimoe ** delitel

else: 
	result = "unknown"
#print(type(result))

print("Result: " + str(result))
input("Нажмите Enter для выхода.")