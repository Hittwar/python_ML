#para leer el cuento de aleph de borges
def run():

	with open('aleph.txt') as f:
		for line in f:
			counter += line.count('Beatriz')

	print('Beatriz se encuentra {} en el texto'.format(counter)) 

if __name__ == '__main__':
	run()
