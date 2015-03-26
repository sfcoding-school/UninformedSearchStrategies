from copy import deepcopy

def checkFinitoSolitario(head, goal):
    if head == goal:
        return True
    return False
        
# Quattro funzioni che definiscono le possibili mosse.
# Controllo prima di non sforare la scacchiera, poi
# se la mossa e' corretta (e quindi mangio un pezzo).
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

# Funzione che stampa la soluzione passo a passo
def print_sol(fringe):
    print
    for i in fringe:
        for j in range(0, len(i)+2):
            print "-",
        print
        for j in i:
            print "|",
            for k in j:
                print str(k),
            print "|"
        for j in range(0, len(i)+2):
            print "-",
        print
        print