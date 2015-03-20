from random import randint

def creoMondo(numeroBlocchi):
	mondoTemp = []
	for x in xrange(0,numeroBlocchi):
		mondoTemp.append([(randint(1,9), randint(1,20))]) # coppia p_i (peso), M_i (quanto puo' reggere)
	return mondoTemp

if __name__ == '__main__':
	mondo = creoMondo(4) #da mettere poi random, iniziamo con 4 per vedere se funziona
	print mondo
