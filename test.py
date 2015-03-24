from random import randint
from copy import deepcopy

numeroBlocchi = 4 #da mettere poi random, iniziamo con 4 per vedere se funziona

def creaTavolo():
	tavoloTemp = []
	for x in xrange(0,numeroBlocchi):
		tavoloTemp.append([(randint(1,9), randint(1,20))]) # coppia p_i (peso), M_i (quanto puo' reggere)
	return tavoloTemp

# lst[0]  first element of a list
# lst[1:] rest of the elements in the list, after the first
def  checkTorre(torreRverse, pesoAttuale):
    if not torreRverse:         											# base case: list is empty
        return True
    elif torreRverse[0][1] >= pesoAttuale :
        return checkTorre(torreRverse[1:], pesoAttuale + torreRverse[0][0]) # recursive case: advance to next element in list
    else:
    	return False

# da ricontrollare
def creaGoal(mondo):
	goalTemp = []
	pesoAttuale = 0
	torre = []
	for x in xrange(0,numeroBlocchi):
		if checkTorre((torre + mondo[x])[::-1], 0):
			torre += mondo[x]
		else:
			goalTemp.append(torre)
			torre = mondo[x]
	goalTemp.append(torre)
	# print "lista Goal finale: ", goalTemp
	return goalTemp

if __name__ == '__main__':
	tavolo = creaTavolo()
	print "tavolo iniziale: ", tavolo
	goal = creaGoal(deepcopy(tavolo))
	print "Goal finale: ", goal
	mondo = {'tavolo': tavolo, 'braccioSx': (), 'braccioDx': ()}
	print 'mondo: ', mondo

	#TEST CREAZIONE MOSSE POSSIBILI
	mondoDiMondi = []
	# PutDown(X) braccio sx
	if mondo['braccioSx'] != ():
		dict2 = deepcopy(mondo)
		dict2['tavolo'].append([dict2['braccioSx']])
		dict2['braccioSx'] = ()
		mondoDiMondi.append(dict2)
	# PutDown(X) braccio dx
	if mondo['braccioDx'] != ():
		dict2 = deepcopy(mondo)
		dict2['tavolo'].append([dict2['braccioDx']])
		dict2['braccioDx'] = ()
		mondoDiMondi.append(dict2)
	# AfferraSx(X)
	if mondo['braccioSx'] == ():
		for x in xrange(0, len(mondo['tavolo'])):
			dict2 = deepcopy(mondo)
			dict2['braccioSx'] = dict2['tavolo'][x][-1]
			dict2['tavolo'][x].remove(dict2['tavolo'][x][-1])
			mondoDiMondi.append(dict2)
	# AfferraDx(X)
	if mondo['braccioDx'] == ():
		for x in xrange(0, len(mondo['tavolo'])):
			dict2 = deepcopy(mondo)
			dict2['braccioDx'] = dict2['tavolo'][x][-1]
			dict2['tavolo'][x].remove(dict2['tavolo'][x][-1])
			mondoDiMondi.append(dict2)

	#per mano sx prova Puton(X,Y), per ogni y sul tavolo gia' esistente (con check se la torre si ROMPE), ripeti per mano dx
	if mondo['braccioSx']!=():
		for y in xrange(0,len(mondo['tavolo'])):
			#se non sorregge il peso non faccio niente, neanche deepcopy
			checkresult = checkTorre((mondo['tavolo'][y] + mondo['braccioSx'])[::-1], 0)
			print "checkresult:" + checkresult
			if checkresult:#appoggio e creo un nuovo stato
				dict2 = deepcopy(mondo)
				dict2['braccioSx']=() #la mano si svuota
				mondoDiMondi.append(dict2)

	if mondo['braccioDx']!=():
		for y in xrange(0,len(mondo['tavolo'])):
			#se non sorregge il peso non faccio niente, neanche deepcopy
			checkresult = checkTorre((mondo['tavolo'][y] + mondo['braccioDx'])[::-1], 0)
			print "checkresult:" + checkresult
			if checkresult:#appoggio e creo un nuovo stato
				dict2 = deepcopy(mondo)
				dict2['braccioDx']=() #la mano si svuota
				mondoDiMondi.append(dict2)

	#stampo risultato per controllo
	print 'mondoDiMondi: '
	for x in mondoDiMondi:
		print x

# uno stato e' formato da {'tavolo': #lista di liste di ogni posizione del tavolo#,
#						   'braccioSx': #elemento presente sul braccio sinistro#,
#						   'braccioDx': #elemento presente sul braccio destro# }


	#TEST
	# torna tutti gli elementi in cima ad ogni posizione del tavolo
	#for x in goal:
	#	print x[-1]

	#MOSSE POSSIBILI
	#Puton(X,Y) metti blocco X su blocco Y, PutDown(X) metti blocco X sul tavolo,
	#AfferraDx(X), AfferraSx(X)


