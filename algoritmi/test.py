lista = [(12, [{'tavolo': [[(5, 12), (5, 16)]], 'braccioDx': (), 'braccioSx': ()}, {'tavolo': [[(5, 12)]], 'braccioDx': (5, 16), 'braccioSx': ()}, {'tavolo': [[(5, 12)], [(5, 16)]], 'braccioDx': (), 'braccioSx': ()}])
,
(10, [{'tavolo': [[(5, 12), (5, 16)]], 'braccioDx': (), 'braccioSx': ()}, {'tavolo': [[(5, 12)]], 'braccioDx': (5, 16), 'braccioSx': ()}, {'tavolo': [[(5, 12)], [(5, 16)]], 'braccioDx': (), 'braccioSx': ()}])
,
(55, [{'tavolo': [[(5, 12), (5, 16)]], 'braccioDx': (), 'braccioSx': ()}, {'tavolo': [[(5, 12)]], 'braccioDx': (5, 16), 'braccioSx': ()}, {'tavolo': [[(5, 12)], [(5, 16)]], 'braccioDx': (), 'braccioSx': ()}])
,
(1, [{'tavolo': [[(5, 12), (5, 16)]], 'braccioDx': (), 'braccioSx': ()}, {'tavolo': [[(5, 12)]], 'braccioDx': (5, 16), 'braccioSx': ()}, {'tavolo': [[(5, 12)], [(5, 16)]], 'braccioDx': (), 'braccioSx': ()}])
]


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

sqc = [(12, [{'tavolo': [[(5, 12), (5, 16)]], 'braccioDx': (), 'braccioSx': ()}, {'tavolo': [[(5, 12)]], 'braccioDx': (5, 16), 'braccioSx': ()}, {'tavolo': [[(5, 12)], [(5, 16)]], 'braccioDx': (), 'braccioSx': ()}])
,
(10, [{'tavolo': [[(5, 12), (5, 16)]], 'braccioDx': (), 'braccioSx': ()}, {'tavolo': [[(5, 12)]], 'braccioDx': (5, 16), 'braccioSx': ()}, {'tavolo': [[(5, 12)], [(5, 16)]], 'braccioDx': (), 'braccioSx': ()}])
,
(55, [{'tavolo': [[(5, 12), (5, 16)]], 'braccioDx': (), 'braccioSx': ()}, {'tavolo': [[(5, 12)]], 'braccioDx': (5, 16), 'braccioSx': ()}, {'tavolo': [[(5, 12)], [(5, 16)]], 'braccioDx': (), 'braccioSx': ()}])
,
(1, [{'tavolo': [[(5, 12), (5, 16)]], 'braccioDx': (), 'braccioSx': ()}, {'tavolo': [[(5, 12)]], 'braccioDx': (5, 16), 'braccioSx': ()}, {'tavolo': [[(5, 12)], [(5, 16)]], 'braccioDx': (), 'braccioSx': ()}])
]
heap_sort(sqc)
for x in sqc:
	print x