import bpy
C = bpy.context
with open(r"H:\Il mio Drive\università\python ssas\FINALE pySSAS\progetto clemente\mioglobina_umano.fa", "r") as seq1:
    seq1 = seq1.readlines()[1]
with open(r"H:\Il mio Drive\università\python ssas\FINALE pySSAS\progetto clemente\mioglobina_topo.fa", "r") as seq2:
    seq2 = seq2.readlines()[1]

"""
PARTE 1 
BIOLOGIA
"""


def match_finder(seq1, seq2, min_len = 10, max_len = len(seq1)): #output: LISTA di DUE LISTE: una contiene le sequenze match, l'altra gli indici delle basi interessate
    
    #gli input: seq1 e seq2, due STRINGHE che contengono la sequenza di basi
    #min_len: un INTERO che indica la lunghezza minima del match. default è 10
    #max_len: un INTERO; indica la lunghezza massima del match. default è la lunghezza della sequenza stessa

    match_list = []
    index_list = []
    for i in range(min_len, max_len+1):
        for j in range(0, len(seq1)-i):
            combo = seq1[j:j+i]
            if combo in seq2:
                match_list.append(combo)
                index_list.append([index for index in range(j,j+i)])

    return [match_list, index_list]


#PARTE 2 BLENDER

def base_reveal(sequence, start_y = 0): #funzione per visualizzare una sola sequenza di nucleotidi
    count = 0
    x = 0
    y=start_y
    z=0.5
    
    for base in sequence:
        
        if base == "\n":
            continue
        else:
            
            bpy.ops.mesh.primitive_cube_add(size = 1, location = (x,y,z))
            item = C.object
            item.data.materials.append(bpy.data.materials[str(base)])
            

            if count == 25:
                z = z + 1
                x = 0
                count = 0
            else:
                x = x + 1
                count += 1
                
def match_reveal(seq1, seq2, min_len = 10): #funzione per visualizzare due sequenze. evidenzia i punti in cui combaciano 
    
    # negli input: due sequenze da confrontare (STRINGHE)
    # min_len è un INTERO: viene passato alla funzione match_finder()
    
    #il programma crea un cubo per ogni base nella stringa
    count = 0
    x = 0
    y = 0
    z=0.5


    m_found = match_finder(seq1, seq2, min_len,len(seq1))
    index_list = []
    for match in m_found[1]:
        for i in match:
            index_list.append(i)
            
            
    for i in range(0, len(seq1)):
        base = seq1[i]
        if base == "\n":
            continue
        else:
            
            bpy.ops.mesh.primitive_cube_add(size = 1, location = (x,y,z))
            item = C.object
            if i in index_list:
                item.data.materials.append(bpy.data.materials[str(base + "_match")])
                #se questo indice è presente nella lista degli indici "match", allora la base sarà evidenziata
            else:
                item.data.materials.append(bpy.data.materials[str(base)])
                #altrimenti no
            

            if count == 25:
                z = z + 1
                x = 0
                count = 0
            else:
                x = x + 1
                count += 1
                
                
    #ora si ripete lo stesso procedimento, per l'altra proteina.
    count = 0
    x = 0
    y = 10
    z=0.5


    m_found = match_finder(seq2, seq1, min_len,len(seq2))
    index_list = []
    for match in m_found[1]:
        for i in match:
            index_list.append(i)
            
                
                
    for i in range(0, len(seq2)):
        base = seq2[i]
        if base == "\n":
            continue
        else:
            
            bpy.ops.mesh.primitive_cube_add(size = 1, location = (x,y,z))
            item = C.object
            if i in index_list:
                item.data.materials.append(bpy.data.materials[str(base + "_match")])
            else:
                item.data.materials.append(bpy.data.materials[str(base)])
            

            if count == 25:
                z = z + 1
                x = 0
                count = 0
            else:
                x = x + 1
                count += 1
                    
                    
match_reveal(seq1,seq2)