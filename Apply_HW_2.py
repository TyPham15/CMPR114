#Tyler Pham
#February 15, 2023
#CMPR114
#Apply: HW#2 Projects 1-3

def Project_1():
	month = int(input('Enter any month as a number: '))
	if month > 12 or month < 1:
		print ('Invalid input. Try Again.')
		Project_1()

	if month >= 1 and month <= 3:
		print ('The month is in the first quarter.')
	elif month >= 4 and month <= 6:
		print ('The month is in the second quarter.')
	elif month >= 7 and month <= 9:
		print ('The month is in the third quarter.')
	elif month >= 10 and month <= 12:
		print ('The month is in the fourth quarter.')
	return str


def Project_2():
	import math

	people = int(input('Enter how many people are attending the cookout: '))
	given_hotdog = int(input('Enter how many hot dogs are given to each person: '))
	
	hotdog_need = given_hotdog * people
	hotdog_package = math.ceil(hotdog_need / 10)
	hotdogbun_package = math.ceil(hotdog_need / 8)
	hotdog_left = (hotdog_package * 10) - hotdog_need
	hotdogbun_left = (hotdogbun_package * 8) - hotdog_need

	print ('You need at least' , hotdog_package , 'hot dog packages for the cookout.')
	print ('You need at least' , hotdogbun_package , 'hot dog bun packages for the cookout.')

	if hotdog_left != 0:
		print ('There are' , hotdog_left , 'hot dogs left over.')
	
	if hotdogbun_left != 0:
		print ('There are' , hotdogbun_left , 'hot dog buns left over.')

	return str


def Project_3():
	quantity = int(input('Enter how many packages you wish to purchase: '))
	price = quantity * 99


	if quantity >= 0 and quantity < 10:
		print ('There is no discount for your purchase.')
		print ('The total for your purchase is $' + str(price) + '.')

	elif quantity >= 10 and quantity <= 19:
		discount = price * 0.10
		total = price - discount
		print ('Your discount is $' + str(round(discount, 2)) + '.')
		print ('The total for your purchase is $' + str(round(total, 2)) + '.')

	elif quantity >= 20 and quantity <= 49:
		discount = price * 0.20
		total = price - discount
		print ('Your discount is $' + str(round(discount, 2)) + '.')
		print ('The total for your purchase is $' + str(round(total, 2)) + '.')

	elif quantity >= 50 and quantity <= 99:
		discount = price * 0.30
		total = price - discount
		print ('Your discount is $' + str(round(discount, 2)) + '.')
		print ('The total for your purchase is $' + str(round(total, 2)) + '.')

	elif quantity >= 100:
		discount = price * 0.40
		total = price - discount
		print ('Your discount is $' + str(round(discount, 2)) + '.')
		print ('The total for your purchase is $' + str(round(total, 2)) + '.')


	return str
Project_3()