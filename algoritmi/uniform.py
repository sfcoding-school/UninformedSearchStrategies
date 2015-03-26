def solve_ucs(mondo, funzControlloGoal, goal, costi, funzioniSuccessori):
    queue = [([mondo],0)]
    visited = []
    c_gen = 1
    c_vis = 0
    c_depth = 0
    while True:
        if len(queue) == 0:
            print "UCS - Nessuna Soluzione"
            print "UCS - numero di nodi generati: ", c_gen
            print "UCS - numero di nodi visitati: ", c_vis
            print "UCS - profondita max raggiunta: ", c_depth
            return []
        else:
			fringe = queue[0] #devo portarmi dietro i costi accumulati
			queue = queue[1:] # toglie dalla lista il primo
			head = fringe[0][0] #mod
			c_vis += 1
			c_depth = max(c_depth,len(fringe))
			visited.append(head)
			if funzControlloGoal(head, goal):
				print "UCS - SOLUZIONE: "
				print "UCS - numero di nodi generati: ", c_gen
				print "UCS - numero di nodi visitati: ", c_vis
				print "UCS - profondita max raggiunta: ", c_depth
				return fringe[0][::-1]
			else:
				i = 0
				for function in funzioniSuccessori:
					nodiSuccessori = function(head)
					if nodiSuccessori != False: # se uguale a False quella mossa non era possibile
						for successore in nodiSuccessori:
							if successore not in visited:
								queue = [ ( [successore] + fringe[0], costi[i] + fringe[1] ) ] + queue
						c_gen += len(nodiSuccessori)
					i += 1
			heap_sort(queue)

#BUBBLESORT
def bubble_sort(queue):
    for i in range(0, len(queue)-1):
        for j in range(0, len(queue)-i-1):
            if queue[j][1] > queue[j+1][1]:
                temp = queue[j]
                queue[j] = queue[j+1]
                queue[j+1] = temp


#HEAPSORT
def swap(sqc,i, j):                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 

def heapify(sqc,end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and sqc[i][0] < sqc[l][0]:   
        max = l   
    if r < end and sqc[max][0] < sqc[r][0]:   
        max = r   
    if max != i:   
        swap(sqc,i, max)   
        heapify(sqc,end, max)   

def heap_sort(sqc):     
    end = len(sqc)   
    start = end / 2 - 1
    for i in range(start, -1, -1):   
        heapify(sqc,end, i)   
    for i in range(end-1, 0, -1):   
        swap(sqc,i, 0)   
        heapify(sqc,i, 0)
