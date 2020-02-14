# -*- coding: utf-8 -*-

def protected(func):
	def wrapper(password):
		if password == 'platzi':
			return func()
		else:
			print('Password incorrecto')
	return wrapper

@protected 
def protected_func():
	print('Tu contraseña es correcta')


if __name__ == '__main__':
	password = str(raw_input('Ingresa tu contraseña: '))

	protected_func(password)