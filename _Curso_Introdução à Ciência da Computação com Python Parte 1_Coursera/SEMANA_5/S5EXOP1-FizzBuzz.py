# coding: utf-8

print('-=-' * 15)
print('FizzBuzz')
print('-=-' * 15)


def fizzbuzz(num):
	if (num % 3 == 0) and (num % 5 != 0):
		return 'Fizz'
	elif (num % 3 != 0) and (num % 5 == 0):
		return 'Buzz'
	elif (num % 3 == 0) and (num % 5 == 0):
		return 'FizzBuzz'
	elif (num % 3 != 0) and (num % 5 != 0):
		return num


num = int(input('\nInforme um número natural: '))

fizzbuzz(num)