from funzioniSupportoMondoBlocchi import *
from dfs import solve_dfs
from bfs import solve_bfs
from deepening import solve_deepening

numeroBlocchi = 4 #da mettere poi random, iniziamo con 4 per vedere se funzion4a

if __name__ == '__main__':
	tavolo = creaTavolo(numeroBlocchi)
	print "tavolo iniziale: ", tavolo
	goal = creaGoal(deepcopy(tavolo), numeroBlocchi)
	print "Gaol finale: ", goal
	mondo = {'tavolo': tavolo, 'braccioSx': (), 'braccioDx': ()}
	print 'mondo: ', mondo
	print
	print "TEST DFS"
	solve_dfs(mondo, goal, [putOnSx, putOnDx, afferraDx, afferraSx, putDownSx, putDownDx])
	print "TEST BFS"
	solve_bfs(mondo, goal, [putOnSx, putOnDx, afferraDx, afferraSx, putDownSx, putDownDx])
	print "TEST DEEPENING"
	solve_deepening(mondo, goal, [putOnSx, putOnDx, afferraDx, afferraSx, putDownSx, putDownDx])

# uno stato e' formato da {'tavolo': #lista di liste di ogni posizione del tavolo#,
#						   'braccioSx': #elemento presente sul braccio sinistro#,
#						   'braccioDx': #elemento presente sul braccio destro# }