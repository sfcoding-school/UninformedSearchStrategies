# DEEPENING SEARCH ITERATIVA
# si ha un while true in cui il codice gira, da cui si puo' uscire solo se: 
# - la variabile 'go_on == False' ovvero ho superato la distanza massima a cui potevo
#		arrivare in questa iterazione
# - e' stata trovata una soluzione valida ( funzControlloGoal(head, goal) == True )
def solve_deepening(mondo, funzControlloGoal, goal, funzioniSuccessori):
	iteration = 0
	while True:
		iteration += 1
		queue = [[mondo]]
		visited = []
		c_gen = 1
		c_vis = 0
		c_depth = 0
		go_on = False
		while len(queue)!= 0:
			fringe = queue[0]
			queue = queue[1:]
			head = fringe[0]
			c_vis += 1
			c_depth = max(c_depth,len(fringe))
			visited.append(head)
			if funzControlloGoal(head, goal):
				print "Iterative Deepening - SOLUZIONE: "
				print "Iterative Deepening - Nodi Generati: ", c_gen
				print "Iterative Deepening - Nodi Visitati: ", c_vis
				print "Iterative Deepening - Massima profondita' raggiunta: ", c_depth
				print "Iterative Deepening - Soluzione in ", len(fringe), " passi"
				return fringe[::-1]
			else:
				for function in funzioniSuccessori:
					nodiSuccessori = function(head)
					if nodiSuccessori != False: # se uguale a False quella mossa non era possibile
						for successore in nodiSuccessori:
							if successore not in visited:
								if len(fringe) < iteration:
									queue.insert(0, [successore] + fringe)
									c_gen += len(nodiSuccessori)
								else:
									go_on = True
        if not go_on:
			print "Iterative Deepening - Nessuna Soluzione"
			print "Iterative Deepening - Nodi Generati: ", c_gen
			print "Iterative Deepening - Nodi Visitati: ", c_vis
			print "Iterative Deepening - Massima profondita' raggiunta: ", c_depth
			return []