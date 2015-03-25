from mondoDeiBlocchi.funzioniSupportoMondoBlocchi import checkFinito

def sort(queue):
    for i in range(0,len(queue)-1):
        for j in range(0,len(queue)-i-1):
            if queue[j][1]>queue[j+1][1]:
                temp=queue[j]
                queue[j]=queue[j+1]
                queue[j+1]=temp

def solve_ucs(mondo,goal,costi,funzioniSuccessori):
    queue=[([mondo],0)]
    visited=[]
    c_gen=1
    c_vis=0
    c_depth=0
    while True:
        if len(queue)==0:
            print "UCS, nessuna soluzione"
            print "UCS, numero di nodi generati: "+str(c_gen)
            print "UCS, numero di nodi visitati: "+str(c_vis)
            print "UCS, profondita max raggiunta: "+str(c_depth)
            return []
        else:
			fringe=queue[0] #devo portarmi dietro i costi accumulati
			queue=queue[1:] # toglie dalla lista il primo
			head=fringe[0][0] #mod
			c_vis+=1
			c_depth=max(c_depth,len(fringe))
			visited.append(head)
			if checkFinito(head, goal):
				print "UCS - SOLUZIONE: "
				print fringe[0][::-1]
				print "UCS - Generated Nodes: ", c_gen
				print "UCS - Visited Nodes: ", c_vis
				print "UCS - Max reached depth: ", c_depth
				return fringe
			else:
				i=0
				for function in funzioniSuccessori:
					nodiSuccessori = function(head)
					if nodiSuccessori != False: # se uguale a False quella mossa non era possibile
						for successore in nodiSuccessori:
							if successore not in visited:
								queue = [ ( [successore] + fringe[0], costi[i]+fringe[1] ) ] + queue
						c_gen+=len(nodiSuccessori)
					i+=1
			sort(queue)
            #queue=[([temp]+fringe[0],costs[0]+fringe[1])]+queue