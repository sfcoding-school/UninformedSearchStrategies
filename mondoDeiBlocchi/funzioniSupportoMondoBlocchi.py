from random import randint
from copy import deepcopy

# crea un tavolo con numero di blocchi fissato e coppie p_i, M_i casuali
def creaTavolo(numeroBlocchi):
	tavoloTemp = []
	for x in xrange(0, numeroBlocchi):
		tavoloTemp.append([(randint(1,9), randint(1,20))]) # coppia p_i (peso), M_i (quanto puo' reggere)
	return tavoloTemp


# questa funzione controlla se una torre puo' esistere o 'crollerebbe'
def  checkTorre(torreRverse, pesoAttuale):
    if not torreRverse: # caso base: la lista e' vuota quindi torno vero
        return True
    elif torreRverse[0][1] >= pesoAttuale :
        return checkTorre(torreRverse[1:], pesoAttuale + torreRverse[0][0]) # lst[1:] ritorna il resto della lista escluso il primo elemento
    else:
    	return False

# Crea un goal casuale a partire dal mondo inziale
# di base crea meno torri possibili utilizzando gli oggetti da destra verso sinistra
def creaGoal(mondo, numeroBlocchi):
	goalTemp = []
	pesoAttuale = 0
	torre = []
	for x in xrange(0,numeroBlocchi):
		if checkTorre((torre + mondo[x])[::-1], 0): # [::-1] serve per invertire la lista
			torre += mondo[x]
		else: 						 # se la torre non puo' sostenere un ulteriore oggetto se ne crea una nuova
			goalTemp.append(torre)
			torre = mondo[x]
	goalTemp.append(torre)
	return goalTemp

#MOSSE POSSIBILI
def putDownDx(mondo):
	if mondo['braccioSx'] != ():
		dict2 = deepcopy(mondo)
		dict2['tavolo'].append([dict2['braccioSx']])
		dict2['braccioSx'] = ()
		return [dict2]
	else:
		return False

def putDownSx(mondo):
	if mondo['braccioDx'] != ():
		dict2 = deepcopy(mondo)
		dict2['tavolo'].append([dict2['braccioDx']])
		dict2['braccioDx'] = ()
		return [dict2]
	else:
		return False

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