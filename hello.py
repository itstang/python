import sys

contype = {'distance': '1', 'volume': '2', 'mass': '3', 'energy': '4'}
flag = 1
choice = input("What would you like to convert?\n")

if choice in contype:
	the_choice = contype[choice]
else:
	print("I don't know that conversion!")

while flag:
	if the_choice == '1':
		conversion = float(input("Convert how many inches to a meter: "))
	elif the_choice == '2':
		conversion = float(input("Convert how many milliters to a pint: "))
	elif the_choice == '3':
		conversion = float(input("Convert how many pounds to a ton: "))
	else:
		conversion = float(input("Convert how many calories to BTU: "))

	try:
		check = int(conversion)
		flag = 0
	except ValueError:
		flag = 1
		print("That's not a valid number")

if the_choice == '1':
	print(str(conversion/12) + " meters")
elif the_choice == '2':
	print(str(conversion/100) + " pints")
elif the_choice == '3':
	print(str(conversion/2000) + " tons")
else:
	print(str(conversion/100) + " BTUs")
