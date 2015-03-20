from random import randint

numeroBlocchi = 4 #da mettere poi random, iniziamo con 4 per vedere se funziona

def creoMondo():
	mondoTemp = []
	for x in xrange(0,numeroBlocchi):
		mondoTemp.append([(randint(1,9), randint(1,20))]) # coppia p_i (peso), M_i (quanto puo' reggere)
	return mondoTemp

# lst[0]  first element of a list
# lst[1:] rest of the elements in the list, after the first
def  checkTorre(torreRverse, pesoAttuale):
    if not torreRverse:         # base case: list is empty
        return True
    elif torreRverse[0][1] >= pesoAttuale : # recursive case: advance to next element in list              
        return checkTorre(torreRverse[1:], pesoAttuale + torreRverse[0][0])
    else:
    	return False

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
	mondo = creoMondo() 
	print "Mondo iniziale: ", mondo
	goal = creaGoal(mondo)
	print "Gaol finale: ", goal