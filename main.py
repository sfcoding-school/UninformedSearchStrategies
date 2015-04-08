# -*- coding: latin-1 -*-

#TESTO
# Esonero n.1 Ricerca nello Spazi degli Stati
# Il progetto consiste nel realizzare un ambiente in cui venga realizzata la ricerca nello spazio degli stati,
# per il problema PegSolitarie e per il problema scelto sulla piattaforma estudium e descritto di seguito.
# Il candidato dovra’ realizzare la ricerca nello spazio degli stati per il problema scelto implementando le
# seguenti strategie:
# ricerca in ampiezza
# ricerca in profondita
# ricerca approfondimento iterative
# ricerca a costo uniforme
# il programma prendera’ in input stato iniziale e goal e dovra’ produrre il piano soluzione (cioe’ la
# sequenza di azioni) o eventualemente fornire l’indicazione che non esistono soluzioni. Oltre alla
# soluzione, Si richiedono in output statistiche sull’esecuzione (numero nodi generati, profondita’
# raggiunta etc.).
# Il candidato dovra’ provare il programma su piu’ istanze di problema di dimensioni diverse e dovra’
# essere possibile per il docente modificare stato iniziale e goal. In particolare si richiede: almeno 2
# problemi con soluzione di lunghezza breve, 1 probema con piano soluzione di lunghezza medio/lunga, 1
# problema senza soluzioni risolto correttamente.
# Per la ricerca a costo uniforme si attribuisca un valore di costo a scelta diverso alle azioni.
# Si consiglia di strutturare il programma in modo tale che Ie diverse strategie siano implementabili con
# semplici modifiche della struttura di base

from mondoDeiBlocchi.funzioniSupportoMondoBlocchi import *
from solitarioCinese.funzioniSupportoSolitarioCinese import *
from algoritmi.dfs import solve_dfs
from algoritmi.bfs import solve_bfs
from algoritmi.deepening import solve_deepening
from algoritmi.uniform import solve_ucs

numeroBlocchi = 4 #numero blocchi di partenza (serve per random)

if __name__ == '__main__':
	print "################## Mondo dei Blocchi ##########################"
	print
	# uno stato e' formato da {'tavolo': #lista di liste di ogni posizione del tavolo#,
	#						   'braccioSx': #elemento presente sul braccio sinistro#,
	#						   'braccioDx': #elemento presente sul braccio destro# }
	
	tavolo = creaTavolo(numeroBlocchi)
	goal = creaGoal(deepcopy(tavolo), numeroBlocchi)
	mondo = {'tavolo': tavolo, 'braccioSx': (), 'braccioDx': ()}
	
	funzSuccessori = [putOnSx, putOnDx, afferraDx, afferraSx, putDownSx, putDownDx]
	costi = (8,8,4,4,2,2)

	#CASO CON GOAL NON VALIDO
	#mondo = {'tavolo': [[(7, 16)], [(5, 19)], [(2, 5)], [(8, 12)]], 'braccioDx': (), 'braccioSx': ()}
	#goal = [[(7, 16), (5, 19), (2, 5), (8, 12)]]

	#CASO LUNGO (BFS e UCS lente) #10min alle 14.24
	#mondo = {'tavolo': [[(7, 16)], [(5, 19)], [(2, 5)], [(8, 12)], [(6, 15)]], 'braccioDx': (), 'braccioSx': ()}
	#goal = [[(7, 16), (5, 19), (2, 5)], [(8, 12), (6, 15)]]

	print "Tavolo iniziale: ", tavolo
	print "Goal finale: ", goal
	print
	

	# TEST ALGORITMI
	testStampa(solve_dfs(mondo, checkFinito, goal, funzSuccessori), "soluzioni/MondoBlocchi-DFS.txt")
	print
	testStampa(solve_bfs(mondo, checkFinito, goal, funzSuccessori), "soluzioni/MondoBlocchi-BFS.txt")
	print
	testStampa(solve_deepening(mondo, checkFinito, goal, funzSuccessori), "soluzioni/MondoBlocchi-Deepening.txt")
	print
	testStampa(solve_ucs(mondo, checkFinito, goal, costi, funzSuccessori), "soluzioni/MondoBlocchi-UCS.txt")

	# SOLITARIO CINESE
	print
	print "################## Solitario Cinese ##########################"

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

	print "Configurazione iniziale"
	print_sol([game_e1])
	print
	print "Goal"
	print_sol([goalSC])


	funzSuccessori = [move_down, move_up, move_left, move_right]
	costi = (1,3,2,0)
	
	# TEST ALGORITMI
	print_sol_File(solve_dfs(game_e1, checkFinitoSolitario, goalSC, funzSuccessori), "soluzioni/SolitarioCinese-DFS.txt")
	print
	print_sol_File(solve_bfs(game_e1, checkFinitoSolitario, goalSC, funzSuccessori), "soluzioni/SolitarioCinese-BFS.txt")
	print
	print_sol_File(solve_deepening(game_e1, checkFinitoSolitario, goalSC, funzSuccessori), "soluzioni/SolitarioCinese-Deepening.txt")
	print
	print_sol_File(solve_ucs(game_e1, checkFinitoSolitario, goalSC, costi, funzSuccessori), "soluzioni/SolitarioCinese-UCS.txt")
