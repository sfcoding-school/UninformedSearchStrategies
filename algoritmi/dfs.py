# from mondoDeiBlocchi.funzioniSupportoMondoBlocchi import checkFinito

def solve_dfs(mondo, funzControlloGoal, goal, funzioniSuccessori):
	queue=[[mondo]]
	visited=[]
	c_gen=1
	c_vis=0
	c_depth=0
	while True:
		if len(queue)==0:
			print "Depth First Search - Solution: There's no solution"
			print "Depth First Search - Generated Nodes: ", c_gen
			print "Depth First Search - Visited Nodes: ", c_vis
			print "Depth First Search - Max reached depth: ", c_depth
			return []
		else:			
			fringe=queue[0]
			queue=queue[1:] # toglie dalla lista il primo
			head=fringe[0]
			c_vis+=1
			c_depth=max(c_depth,len(fringe))
			visited.append(head)
			if funzControlloGoal(head, goal):
				print "Depth First Search - Solution: "
				print fringe[::-1]
				print "Depth First Search - Generated Nodes: ", c_gen
				print "Depth First Search - Visited Nodes: ", c_vis
				print "Depth First Search - Max reached depth: ", c_depth
				return fringe[::-1]
			else:
				for function in funzioniSuccessori:
					nodiSuccessori = function(head)
					if nodiSuccessori != False: # se uguale a False quella mossa non era possibile
						for successore in nodiSuccessori:
							if successore not in visited:
								queue.insert(0, [successore] + fringe)
						c_gen+=len(nodiSuccessori)