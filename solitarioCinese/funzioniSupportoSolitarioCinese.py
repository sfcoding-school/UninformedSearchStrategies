from copy import deepcopy
import os

def checkFinitoSolitario(head, goal):
    if head == goal:
        return True
    return False
        
#MOSSE POSSIBILI
# viene controllata per ogni zona della scacchiera se e' possibile la mossa e in caso si crea un nuovo stato
# e lo si attacca alla lista 'generati' che verra' poi ritornata all'algoritmo in esecuzione
def move_down(head):
    generati = []
    for x in range(0, len(head)):
        for y in range(0, len(head[0])):
            temp = deepcopy(head)
            if head[x][y] == 1:
                if x+2 < len(temp) and temp[x+1][y] == 1 and temp[x+2][y] == 0:
                    temp[x][y] = 0
                    temp[x+1][y] = 0
                    temp[x+2][y] = 1
                    generati.append(temp)
    return generati

def move_up(head):
    generati = []
    for x in range(0, len(head)):
        for y in range(0, len(head[0])):
            temp = deepcopy(head)
            if head[x][y] == 1:
                if x-2 >= 0 and temp[x-1][y] == 1 and temp[x-2][y] == 0:
                    temp[x][y] = 0
                    temp[x-1][y] = 0
                    temp[x-2][y] = 1
                    generati.append(temp)
    return generati

def move_left(head):
    generati = []
    for x in range(0, len(head)):
        for y in range(0, len(head[0])):
            temp = deepcopy(head)
            if head[x][y] == 1:
                if y-2 >= 0 and temp[x][y-1] == 1 and temp[x][y-2] == 0:
                    temp[x][y] = 0
                    temp[x][y-1] = 0
                    temp[x][y-2] = 1
                    generati.append(temp)
    return generati

def move_right(head):
    generati = []
    for x in range(0, len(head)):
        for y in range(0, len(head[0])):
            temp = deepcopy(head)
            if head[x][y] == 1:
                if y+2 < len(temp[0]) and temp[x][y+1] == 1 and temp[x][y+2] == 0:
                    temp[x][y] = 0
                    temp[x][y+1] = 0
                    temp[x][y+2] = 1
                    generati.append(temp)
    return generati

# Funzione che stampa la soluzione su terminale
def print_sol(fringe):
    print
    stack = ""
    for j in range(0, len(fringe[0])+1):
        stack += " -"
    for i in fringe:
        print stack
        for j in i:
            print "|",
            for k in j:
                print str(k),
            print "|"
        print stack
        print

# Funzione che stampa la soluzione su file
def print_sol_File(fringe, whichAlg):
    if not os.path.exists("soluzioni"):
        os.makedirs("soluzioni")
    fname = whichAlg
    file = open(fname, 'w')
    file.write("\n")
    stack = ""
    for j in range(0, len(fringe[0])+1):
            stack += " -"
    for i in fringe:
        file.write(stack + "\n")
        for j in i:
            file.write("|")
            for k in j:
                file.write(" " + str(k))
            file.write(" |\n")
        file.write(stack + "\n\n")