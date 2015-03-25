from mondoDeiBlocchi.funzioniSupportoMondoBlocchi import checkFinito

def solve_deepening(mondo, goal, funzioniSuccessori):
	iteration=0
	while True:
		iteration+=1
		queue=[[mondo]]
		visited=[]
		c_gen=1
		c_vis=0
		c_depth=0
		go_on=False
		while len(queue)!=0:
			fringe=queue[0]
			queue=queue[1:]
			head=fringe[0]
			c_vis+=1
			c_depth=max(c_depth,len(fringe))
			visited.append(head)
			if checkFinito(head, goal):
				print "Iterative Deepening - Solution: "
				print fringe[::-1]
				print "Iterative Deepening - Generated Nodes: ", c_gen
				print "Iterative Deepening - Visited Nodes: ", c_vis
				print "Iterative Deepening - Max reached depth: ", c_depth
				return fringe[::-1]
			else:
				for function in funzioniSuccessori:
					nodiSuccessori = function(head)
					if nodiSuccessori != False: # se uguale a False quella mossa non era possibile
						for successore in nodiSuccessori:
							if successore not in visited:
								if len(fringe)<iteration:
									queue.insert(0, [successore] + fringe)
									c_gen+=len(nodiSuccessori)
								else:
									go_on=True
        if not go_on:
			print "Iterative Deepening - Solution: There's no solution"
			print "Iterative Deepening - Generated Nodes: ", c_gen
			print "Iterative Deepening - Visited Nodes: ", c_vis
			print "Iterative Deepening - Max reached depth: ", c_depth
			return []