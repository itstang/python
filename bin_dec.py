def binaryToDecimal(binary):
	decimal = 0
	index = 0

	while binary > 0:
		lastDigit = binary % 10
		binary = int(binary / 10)
		decimal += (lastDigit * (2**index))
		index += 1
	return decimal

def decimalToBinary(decimal):
	binary = ""
	remainders = []

	while decimal > 0:
		remainders.append(str(decimal % 2))
		decimal /= 2
	remainders.reverse()
	binary = "".join(remainders)
	
	return 0 if binary == "" else binary

choice = int(input("Make a choice: "))

if choice == 1:
	binary = int(input("Binary to convert: "))
	print("The binary number " + str(binary) + " in decimal is " + str(binaryToDecimal(binary)))
elif choice == 2:
	decimal = int(input("Decimal to convert: "))
	print("The decimal number " + str(decimal) + " in binary is " + str(decimalToBinary(decimal)))
else:
	print("Invalid choice")
