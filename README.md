##Mondo dei Blocchi con Peso e Portata
**Descrizione:** un robot manipola blocchi con le due braccia (Dx=destra, Sx=Sinistra), I blocchi
(implementare per almeno 4 blocchi) hanno peso e portata. Ciascun blocco e’ caratterizzato da
una coppia di interi P i e M i ha un peso P i ed puo’ reggere (direttamente o indirettamente)
blocchi di peso massimo complessivo M i .

**Azioni:** Puton(X,Y) metti blocco X su blocco Y, PutDown(X) metti blocco X sul tavolo,
AfferraDx(X), AfferraSx(X)

**Stati e Goal:** una descrizione delle posizioni iniziali dei blocchi e dei loro parametri di peso e
portata, goal una descrizione delle posizioni finali dei blocchi

**Vincoli:** il robot puo’ prendere/lasciare/portare due blocchi alla volta; un blocco non puo’ essere
afferrato con una mano se essa ha gia’ un blocco; un blocco ha spazio per accogiere alla
sommita’ un solo blocco; un blocco non puo’ essere messo sopra un altro/I solo se ciascun
blocco i della pila sta reggendo un peso uguale o inferiore alla propria portata M i ; sul tavolo puo’
reggere quanti blocchi si vogliono.

#Uninformed Search
An uninformed (a.k.a. blind, brute-force) search algorithm generates the search tree without using any domain specific knowledge.

##The search problem
**State space** S : all valid configurations
**Initial states** (nodes) I: subset of S
**Goal states** G: subset of S
**Successor function** succs(s) is subset of S : states reachable in one step (one arc) from s
The search problem: find a solution path from a state in I to a state in G

###Algorithms
* **Breadth-First Search**
*Strategy: expand the shallowest unexpanded node. Implementation: The fringe is a FIFO queue*
* **Depth-First Search**
*Strategy: expand the deepest unexpanded node. Implementation: The fringe is a LIFO queue (stack)*
* **Uniform Cost Search**
*Strategy: Expand the lowest cost node. Implementation: the fringe is a priority queue: lowest cost node has the highest priority*
* **Iterative Deepening Search**
*This is just a depth-first search with a cutoff depth*

