from mondoDeiBlocchi.funzioniSupportoMondoBlocchi import *
from solitarioCinese.funzioniSupportoSolitarioCinese import *
from algoritmi.dfs import solve_dfs
from algoritmi.bfs import solve_bfs
from algoritmi.deepening import solve_deepening
from algoritmi.uniform import solve_ucs

numeroBlocchi = 2 #da mettere poi random, iniziamo con 4 per vedere se funziona

if __name__ == '__main__':
	tavolo = creaTavolo(numeroBlocchi)
	print "tavolo iniziale: ", tavolo
	goal = creaGoal(deepcopy(tavolo), numeroBlocchi)
	print "goal finale: ", goal
	mondo = {'tavolo': tavolo, 'braccioSx': (), 'braccioDx': ()}
	print 'mondo: ', mondo
	print
	funzSuccessori = [putOnSx, putOnDx, afferraDx, afferraSx, putDownSx, putDownDx]
	print "################## Mondo dei Blocchi ##########################"
	print "TEST DFS"
	solve_dfs(mondo, checkFinito, goal, funzSuccessori)
	print "TEST BFS"
	solve_bfs(mondo, checkFinito, goal, funzSuccessori)
	print "TEST DEEPENING"
	solve_deepening(mondo, checkFinito, goal, funzSuccessori)
	print "TEST UCS"
	costi = (8,8,4,4,2,2)#COSTI(putOnSx, putOnDx, afferraDx, afferraSx, putDownSx, putDownDx)
	solve_ucs(mondo, checkFinito, goal, costi, funzSuccessori)

	# TEST SOLITARIO CINESE

	game_e1=[[" "," ",1,1,0," "," "],
			[" "," ",0,1,1," "," "],
			[0,0,0,0,0,0,0],
			[0,0,0,1,1,0,0],
			[0,0,0,0,0,1,0],
			[" "," ",0,0,0," "," "],
			[" "," ",0,0,0," "," "]]

	goalSC=[[" "," ",0,0,0," "," "],
			[" "," ",0,0,0," "," "],
			[0,0,0,0,0,0,0],
			[0,0,0,1,0,0,0],
			[0,0,0,0,0,0,0],
			[" "," ",0,0,0," "," "],
			[" "," ",0,0,0," "," "]]

	print
	print "################## Solitario Cinese ##########################"
	print "TEST DFS"
	funzSuccessori = [move_down, move_up, move_left, move_right]
	solve_dfs(game_e1, checkFinitoSolitario, goalSC, funzSuccessori)
	print "TEST BFS"
	solve_bfs(game_e1, checkFinitoSolitario, goalSC, funzSuccessori)
	print "TEST DEEPENING"
	solve_deepening(game_e1, checkFinitoSolitario, goalSC, funzSuccessori)
	print "TEST UCS"
	costi = (1,3,2,0)
	solve_ucs(game_e1, checkFinitoSolitario, goalSC, costi, funzSuccessori)

# uno stato e' formato da {'tavolo': #lista di liste di ogni posizione del tavolo#,
#						   'braccioSx': #elemento presente sul braccio sinistro#,
#						   'braccioDx': #elemento presente sul braccio destro# }