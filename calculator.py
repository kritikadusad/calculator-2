"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""
import sys
import string
from arithmetic import *
operations = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod', 'x+', 'cubes+']

while True:
	user_input = input('What do you want to do: ')
	tokens = user_input.split(' ')
	tokens_length = len(tokens)
	try:	
		num1 = float(tokens[1])
		num2 = float(tokens[2])
		num3 = float(tokens[3])
		break
	except ValueError:
		print("Incorrect input. Try again")
		continue
	except IndexError:
		pass
	
	

	
# Initializing operated_result to None
	operated_result = None
	if tokens[0] == 'q':
		print('Goodbye!')
		sys.exit()
	else:
		if tokens[0] not in operations:
			print('Incorrect operator. Please try again!')
			continue
		elif tokens_length == 2:
			if tokens[0] == 'square':
				operated_result = square(num1)
				print(operated_result)
			elif tokens[0] == 'cube':
				operated_result = cube(num1)
				print(operated_result)
		
		elif tokens_length == 3:

			if tokens[0] == '+':
				operated_result = add(num1, num2)
				print(operated_result)
			elif tokens[0] == '-':
				operated_result = subtract(num1, num2)
				print(operated_result)
			elif tokens[0] == '*':
				operated_result = multiply(num1, num2)
				print(operated_result)
			elif tokens[0] == '/':
				operated_result = divide(num1, num2)
				print(operated_result)
			elif tokens[0] == 'pow':
				operated_result = power(num1, num2)
				print(operated_result)
			elif tokens[0] == 'mod':
				operated_result = mod(num1, num2)
				print(operated_result)	
			elif tokens[0] == 'cubes+':
				operated_result = add_cubes(num1, num2)
				print(operated_result)
			else:
				print('You are providing an incorrect input. Try again!')
		
		elif tokens_length == 4:
			
			if tokens[0] == 'x+':
				operated_result = add_mult(num1, num2, num3)
				print(operated_result)
			else:
				print('You are providing an incorrect input. Try again!')
		
		else: 
			print('You are giving too many numbers for this operation. Try again!')
			continue
			# elif tokens[0] == '**':
			# 	operated_result = subtract(num1, num2)
			# 	print(operated_result)			
			



		