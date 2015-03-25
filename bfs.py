from funzioniSupportoMondoBlocchi import checkFinito

def solve_bfs(mondo, goal, funzioniSuccessori):
	queue=[[mondo]]
	visited=[]
	c_gen=1
	c_vis=0
	c_depth=0
	while True:
		if len(queue)==0:
			print "BFS, nessuna soluzione"
			print "BFS - Generated Nodes: ", c_gen
			print "BFS - Visited Nodes: ", c_vis
			print "BFS - Max reached depth: ", c_depth
			return []
		else:			
			fringe=queue[0]
			queue=queue[1:] # toglie dalla lista il primo
			head=fringe[0]
			c_vis+=1
			c_depth=max(c_depth,len(fringe))
			visited.append(head)
			if checkFinito(head, goal):
				print "BFS - SOLUZIONE: "
				print fringe[::-1]
				print "BFS - Generated Nodes: ", c_gen
				print "BFS - Visited Nodes: ", c_vis
				print "BFS - Max reached depth: ", c_depth
				return fringe[::-1]
			else:
				for function in funzioniSuccessori:
					nodiSuccessori = function(head)
					if nodiSuccessori != False: # se uguale a False quella mossa non era possibile
						for successore in nodiSuccessori:
							if successore not in visited:
								queue.append([successore] + fringe)
						c_gen+=len(nodiSuccessori)