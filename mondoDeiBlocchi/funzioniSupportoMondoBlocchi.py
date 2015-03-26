from random import randint
from copy import deepcopy

def creaTavolo(numeroBlocchi):
	tavoloTemp = []
	for x in xrange(0, numeroBlocchi):
		tavoloTemp.append([(randint(1,9), randint(1,20))]) # coppia p_i (peso), M_i (quanto puo' reggere)
	return tavoloTemp

# lst[1:] rest of the elements in the list, after the first
def  checkTorre(torreRverse, pesoAttuale):
    if not torreRverse: # base case: list is empty
        return True
    elif torreRverse[0][1] >= pesoAttuale :
        return checkTorre(torreRverse[1:], pesoAttuale + torreRverse[0][0]) # recursive case: advance to next element in list
    else:
    	return False

# da ricontrollare
def creaGoal(mondo, numeroBlocchi):
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
	return goalTemp

#MOSSE POSSIBILI
# PutDown(X) braccio sx
def putDownDx(mondo):
	if mondo['braccioSx'] != ():
		dict2 = deepcopy(mondo)
		dict2['tavolo'].append([dict2['braccioSx']])
		dict2['braccioSx'] = ()
		return [dict2]
	else:
		return False

# PutDown(X) braccio dx
def putDownSx(mondo):
	if mondo['braccioDx'] != ():
		dict2 = deepcopy(mondo)
		dict2['tavolo'].append([dict2['braccioDx']])
		dict2['braccioDx'] = ()
		return [dict2]
	else:
		return False

# AfferraSx(X)
def afferraSx(mondo):
	generati = []
	if mondo['braccioSx'] == ():
		for x in xrange(0, len(mondo['tavolo'])):
			dict2 = deepcopy(mondo)
			dict2['braccioSx'] = dict2['tavolo'][x][-1]
			if len(dict2['tavolo'][x]) == 1: #se era da solo rimuovere lista
				dict2['tavolo'].remove(dict2['tavolo'][x])
			else:
				dict2['tavolo'][x].remove(dict2['tavolo'][x][-1])
			generati.append(dict2)
		return generati
	else:
		return False

def afferraDx(mondo):
	generati = []
	if mondo['braccioDx'] == ():
		for x in xrange(0, len(mondo['tavolo'])):
			dict2 = deepcopy(mondo)
			dict2['braccioDx'] = dict2['tavolo'][x][-1]
			if len(dict2['tavolo'][x]) == 1: #se era da solo rimuovere lista
				dict2['tavolo'].remove(dict2['tavolo'][x])
			else:
				dict2['tavolo'][x].remove(dict2['tavolo'][x][-1])
			generati.append(dict2)
		return generati
	else:
		return False

def putOnSx(mondo):
	generati = []
	if mondo['braccioSx'] != ():
			for y in xrange(0, len(mondo['tavolo'])):
				#se non sorregge il peso non faccio niente, neanche deepcopy
				checkresult = checkTorre((mondo['tavolo'][y] + [mondo['braccioSx']])[::-1], 0) #checkTorre((torre + mondo[x])[::-1], 0):
				if checkresult: #appoggio e creo un nuovo stato
					dict2 = deepcopy(mondo)
					dict2['tavolo'][y].append(mondo['braccioSx'])
					dict2['braccioSx'] = () #la mano si svuota
					generati.append(dict2)
			return generati
	else:
		return False

def putOnDx(mondo):
	generati = []
	if mondo['braccioDx'] != ():
		for y in xrange(0, len(mondo['tavolo'])):
			#se non sorregge il peso non faccio niente, neanche deepcopy
			checkresult = checkTorre((mondo['tavolo'][y] + [mondo['braccioDx']])[::-1], 0)
			if checkresult: #appoggio e creo un nuovo stato
				dict2 = deepcopy(mondo)
				dict2['tavolo'][y].append(mondo['braccioDx'])
				dict2['braccioDx'] = () #la mano si svuota
				generati.append(dict2)
		return generati
	else:
		return False

def checkFinito(head, goal):
	if head['tavolo'] == goal:
		return True
	return False