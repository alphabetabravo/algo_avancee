import fileinput

class MyColor:
    def __init__( self):
        self.valColor = set([])
    def add_Color(self, nbColor):
        it = iter(nbColor)
        for u in it:
            self.valColor.add(u)

class Sommet:
    def __init__( self,x ,color):
        self.x = x
        self.color = color
        self.listeVoisin = set([])
        self.nbVoisin = 0

    def setVoisin(self,Sommet):
        self.listeVoisin.add(Sommet)
        self.nbVoisin +=1

class Graph :
    def __init__( self ) :
        self.v = set([])
        self.e = set([])

    def add_v( self, Sommet ) :
        self.v.add( Sommet )
    
    def add_e( self, x ) :
        try :
            it = iter(x)
            for (u,v) in it :
                self.e.add( (u,v) )
        except TypeError :
            self.e.add( (u,v) )
 
def recupSommet(graph,x) :
    for i in graph.v:
        if i.x == x:
            ptrSommet = i
    return ptrSommet

def initialisationGraph(v):
    list_sommet = []
    for i in v.input() :
        if v.filelineno() == 1 :
            graph = Graph()
        if v.filelineno() == 2:
            list_sommet = map(str, i.split(" "))
            list_sommet.pop()
            for j in list_sommet:
                mysommet = Sommet(j,"nothing")
                graph.add_v(mysommet)    
        elif len( i.split( '--' ) ) == 2 :
            i = i.replace('\n', '')
            (n,m) = map( str, i.split( '--' ) )
            graph.add_e( [ (n,m) ] )    
    return graph

def initialisationCouleur(v, graph):
    list_sommet = []
    for i in v.input() :
        if len( i.split( '--' ) ) == 3 :
            (n,m,o) = map( str, i.split( '--' ) )
            mySommet = recupSommet(graph,m)
            mySommet.color = o

def ajout_Voisin(graph):
    for j in graph.v:
        for i in graph.e:
            if i[0] == j.x:
                j.setVoisin(i[1])
            elif i[1] == j.x:
                j.setVoisin(i[0])

def verification(graph):
    #on parcours les sommets
    for i in graph.v:
        #pour chaque sommet on parcours ces voisins
        for j in i.listeVoisin:
            mySommet = recupSommet(graph,j)
            if mySommet.color == i.color:
                return 1
    return 0

v = fileinput

graph = initialisationGraph(v)
initialisationCouleur(v,graph)
ajout_Voisin(graph)

#for i in graph.v:
    #print i.x
    #print i.color

valreturn = verification(graph)
print valreturn














		

