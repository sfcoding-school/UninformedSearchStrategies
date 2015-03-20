**Mondo dei Blocchi con Peso e Portata**
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

