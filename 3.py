def add(x,y):
	return x + y

def sub(x,y):
	return x - y

def mult(x,y):
	return x * y

def div(x,y):
	return x / y

while True:

	user_input = input('Choose (add, sub, mult, div:)')
	if user_input == 'exit':
		break

	first_input = int(input('enter value: '))
	second_input = int(input('enter value: '))

	if user_input == 'add':
		print(add(first_input, second_input))

	elif user_input == 'sub':
		print(sub(first_input, second_input))

	elif user_input == 'mult':
		print(mult(first_input, second_input))

	elif user_input == 'div':
		print(div(first_input, second_input))

	else:
		print('invalid')