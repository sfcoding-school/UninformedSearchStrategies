from random import randint
from copy import deepcopy

numeroBlocchi = 4 #da mettere poi random, iniziamo con 4 per vedere se funzion4a

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

#MOSSE POSSIBILI
# PutDown(X) braccio sx
def putDownDx(mondo):
	if mondo['braccioSx'] != ():
		dict2 = deepcopy(mondo)
		dict2['tavolo'].append([dict2['braccioSx']])
		dict2['braccioSx'] = ()
		#print "putDownDx:", dict2
		return [dict2]
	else:
		return False

# PutDown(X) braccio dx
def putDownSx(mondo):
	if mondo['braccioDx'] != ():
		dict2 = deepcopy(mondo)
		dict2['tavolo'].append([dict2['braccioDx']])
		dict2['braccioDx'] = ()
		#print "putDownSx:", dict2
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
		#print "afferraSx: ", generati
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
		#print "afferraDx: ", generati
		return generati
	else:
		return False

def putOnSx(mondo):
	generati = []
	if mondo['braccioSx']!=():
			for y in xrange(0,len(mondo['tavolo'])):
				#se non sorregge il peso non faccio niente, neanche deepcopy
				checkresult = checkTorre((mondo['tavolo'][y] + [mondo['braccioSx']])[::-1], 0) #checkTorre((torre + mondo[x])[::-1], 0):
				#print "checkresult:" + checkresult
				if checkresult:#appoggio e creo un nuovo stato
					dict2 = deepcopy(mondo)
					dict2['tavolo'][y].append(mondo['braccioSx'])
					dict2['braccioSx']=() #la mano si svuota
					generati.append(dict2)
			#print "putOnSx: ", generati
			return generati
	else:
		return False

def putOnDx(mondo):
	generati = []
	if mondo['braccioDx']!=():
		for y in xrange(0,len(mondo['tavolo'])):
			#se non sorregge il peso non faccio niente, neanche deepcopy
			checkresult = checkTorre((mondo['tavolo'][y] + [mondo['braccioDx']])[::-1], 0)
			#print "checkresult:", checkresult
			if checkresult:#appoggio e creo un nuovo stato
				dict2 = deepcopy(mondo)
				dict2['tavolo'][y].append(mondo['braccioDx'])
				dict2['braccioDx']=() #la mano si svuota
				generati.append(dict2)
		#print "putOnDx: ", generati
		return generati
	else:
		return False

def checkFinito(head, goal):
	if head['tavolo'] == goal:
		return True
	return False

# def solve_dfs(mondo, goal):
# 	queue=[[mondo]]
# 	visited=[]
# 	c_gen=1
# 	c_vis=0
# 	c_depth=0
# 	while True:
# 		if len(queue)==0:
# 			print "Depth First Search - Solution: There's no solution"
# 			print "Depth First Search - Generated Nodes: "+str(c_gen)
# 			print "Depth First Search - Visited Nodes: "+str(c_vis)
# 			print "Depth First Search - Max reached depth: "+str(c_depth)
# 			return []
# 		else:			
# 			fringe=queue[0]
# 			print "STAMPO FRINGE"
# 			print fringe
# 			queue=queue[1:] # toglie dalla lista il primo
# 			head=fringe[0]
# 			c_vis+=1
# 			c_depth=max(c_depth,len(fringe))
# 			visited.append(head)
# 			print "TEST"
# 			print "fringe: ", fringe
# 			print "queue: ", queue
# 			# print "len queue: ", len(queue)
# 			# print visited
# 			print "head: ", head
# 			print "END TEST"
# 			raw_input("")
# 			if checkFinito(head, goal):
# 				print "Depth First Search - Solution: "
# 				print fringe[::-1]
# 				print "Depth First Search - Generated Nodes: "+str(c_gen)
# 				print "Depth First Search - Visited Nodes: "+str(c_vis)
# 				print "Depth First Search - Max reached depth: "+str(c_depth)
# 				return fringe[::-1]
# 			else:
# 				temp = putDownDx(head)
# 				if temp!=False and temp not in visited:
# 					queue=[temp+fringe]+queue
# 					c_gen+=1

# 				temp = putDownSx(head)
# 				if temp!=False and temp not in visited:
# 					queue=[temp+fringe]+queue
# 					c_gen+=1

# 				temp = afferraSx(head)
# 				if temp!=False and temp not in visited:
# 					queue=[temp+fringe]+queue
# 					c_gen+=1

# 				temp = afferraDx(head)
# 				if temp!=False and temp not in visited:
# 					queue=[temp+fringe]+queue
# 					c_gen+=1

# 				temp = putOnDx(head)
# 				if temp!=False and temp not in visited:
# 					queue=[temp+fringe]+queue
# 					c_gen+=1

# 				temp = putOnSx(head)
# 				if temp!=False and temp not in visited:
# 					queue=[temp+fringe]+queue
# 					c_gen+=1
# 				print "stampo coda alla fine if "
# 				for x in queue:
# 					print x
# 				print "len queue: ", len(queue)

def solve_dfs2(mondo, goal):
	queue=[[mondo]]
	visited=[]
	c_gen=1
	c_vis=0
	c_depth=0
	while True:
		if len(queue)==0:
			print "Depth First Search - Solution: There's no solution"
			return []
		else:			
			fringe=queue[0]
			queue=queue[1:] # toglie dalla lista il primo
			head=fringe[0]
			c_vis+=1
			c_depth=max(c_depth,len(fringe))
			visited.append(head)
			if checkFinito(head, goal):
				print "Depth First Search - Solution: "
				print fringe[::-1]
				return fringe[::-1]
			else:
				temp = putDownDx(head)
				if temp!= False:
					for x in temp:
						if x not in visited:
							queue.insert(0, [x] + fringe)
					c_gen+=len(temp)

				temp = putDownSx(head)
				if temp!= False:
					for x in temp:
						if x not in visited:
							queue.insert(0, [x] + fringe)
					c_gen+=len(temp)

				temp = afferraSx(head)
				if temp!= False:
					for x in temp:
						if x not in visited:
							queue.insert(0, [x] + fringe)
					c_gen+=len(temp)

				temp = afferraDx(head)
				if temp!= False:
					for x in temp:
						if x not in visited:
							queue.insert(0, [x] + fringe)
					c_gen+=len(temp)

				temp = putOnDx(head)
				if temp!= False:
					for x in temp:
						if x not in visited:
							queue.insert(0, [x] + fringe)
					c_gen+=len(temp)

				temp = putOnSx(head)
				if temp!= False:
					for x in temp:
						if x not in visited:
							queue.insert(0, [x] + fringe)
					c_gen+=len(temp)

				# print "stampo coda alla fine if "
				# for x in queue:
				# 	print x
				# print "len queue: ", len(queue)
				#raw_input("")

if __name__ == '__main__':
	tavolo = creaTavolo()
	print "tavolo iniziale: ", tavolo
	goal = creaGoal(deepcopy(tavolo))
	print "Gaol finale: ", goal
	mondo = {'tavolo': tavolo, 'braccioSx': (), 'braccioDx': ()}
	print 'mondo: ', mondo
	print
	print "TEST DFS"
	solve_dfs2(mondo, goal)

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

	#per mano sx prova Puton(X,Y), per ogni y sul tavolo gia' esistente (con check se la torre si ROMPE), ripeti per mano dx
