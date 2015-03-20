from random import randint

numeroBlocchi = 4 #da mettere poi random, iniziamo con 4 per vedere se funziona

def creoMondo():
	mondoTemp = []
	for x in xrange(0,numeroBlocchi):
		mondoTemp.append([(randint(1,9), randint(1,20))]) # coppia p_i (peso), M_i (quanto puo' reggere)
	return mondoTemp

if __name__ == '__main__':
	mondo = creoMondo() 
	for x in xrange(1,10):
		pass
	print mondo