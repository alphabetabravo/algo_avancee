#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
import sys
import fileinput
########################################################################
## Programme qui fait la resolution du coloriage à 3 couleur d'un graphe
########################################################################

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
        self.visiter = 0

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
		#Verifie si le sommet à une couleur sinon --> Echec
		if i.color == "nothing":
			return 1
    return 0
   
def decolorer_graph(list_sommet):
	#Fonction qui mets la couleur des sommets de la liste en entrée à "nothing"
	for i in list_sommet:
		tmpSommet = recupSommet(graph,i)
		tmpSommet.color = "nothing"
		tmpSommet.visiter = 0
	return 0

def recup_liste_color(k,list_colors):
	list_Colors_Choix = []
	i = 0
	#Fonction qui renvoie la liste de k couleurs
	while i < k:
		list_Colors_Choix.append(list_colors[i])
		i += 1
	return list_Colors_Choix

def test_color_voisin(myGraph,S,myColor):
	#Fonction qui test si une couleur "myColor" peut etre mise sur le sommet S
	#On verifie qu'aucun de ses voisins ne possédent cette couleur
	for j in S.listeVoisin:
		tmpSommet = recupSommet(graph,j)
		if tmpSommet.color == myColor:
			return 1
	return 0

def couleur_possible(myGraph,S,list_colors):
	list_colors_admissible = []
	nbvoisin = 0
	#Fonction qui retourne la liste des couleurs admissible par un sommet en fonction de ses voisins
	for i in list_colors:
		if test_color_voisin(myGraph,S,i) == 0:
			list_colors_admissible.append(i)		
	return list_colors_admissible

def graphRecursive(myGraph,nbColor,allColors,lstSommets,numSommet):
	
	if verification(myGraph) == 0 :
		return 0
	

	sommetEnCour = recupSommet(myGraph,str(lstSommets[numSommet]))
	

	numColor = 0


	
	while numColor < nbColor:

		if test_color_voisin(myGraph,sommetEnCour,allColors[numColor]) == 0:

			sommetEnCour.color = allColors[numColor]

			if graphRecursive(myGraph,nbColor,allColors,lstSommets,numSommet+1) == 0:
				return 0
			sommetEnCour.color = "nothing"

		numColor += 1
		
	return 1
	
def affichage_graph_debug(myGraph):
	#Fonction affichage du graph pour le debug
	nbArrete = 0
	nbsommet = 0
	for i in graph.v :
		nbsommet += 1
	for i in graph.e :
		nbArrete += 1
	print "####################################################"
	print "#####    Nb sommets dans le graph : " + str(nbsommet) +  "         #####"
	print "#####    Nb arrete dans le graph  : " + str(nbArrete) +  "         #####"
	print "####################################################"
	
	for i in myGraph.v :
		print " ---------------------------------------------------"
		print " ---------------------------------------------------"
		print "Le sommet est : " + i.x
		print "Sa couleur vaut : " + i.color
		print "Son nombre de voisin est :  " + str(i.nbVoisin)
		print "Les voici : "
		for j in i.listeVoisin :
				print j
		
		
		
		
		
#Variable contient une liste de couleurs
myListColor = ["vert","jaune","rouge"]
#reglage du nombre de récursion maximum
sys.setrecursionlimit(1000000)
#On récupére l'entrée du pipe
v = fileinput
#On initialise le graph
graph = initialisationGraph(v)


#On ajoute la liste des voisins pour chaque sommets
ajout_Voisin(graph)
#On récupére une liste de coleurs en fonction d'un nombre de couleurs voulu
allColor = recup_liste_color(3,myListColor)


#~ affichage_graph_debug(graph)


#On Choisit un sommet aléatoirement
#Je choisit toujours le premier sommet du graph , aucune heuristique n'est émise
#A REVOIR , pour le choix du premier sommet, choix utilisateur ?
list_sommet = []
for i in graph.v:
	list_sommet.append(i.x)
	
firstSommet = 0

if graphRecursive(graph,3,allColor,list_sommet,0) == 0:
	sys.exit(0)
else:
	sys.exit(1)


#~ #affichage_graph_debug(graph)
#~ #On lance le coloriage du graph
#~ print "####################################################"
#~ print "#####    LANCEMENT DU COLORIAGE GRAPH          #####"
#~ print "####################################################"
#~ 
#~ if graphRecursive(graph,3,allColor,list_sommet,0) == 0:
	#~ print "Coloriage OK du graph"
	#~ print "Voici les couleurs de chaques sommets"
	#~ for i in graph.v:
		#~ print "Sommet : " + i.x + " -- Couleur : " + i.color
#~ else:
	#~ print "Impossible de colorier le graph !"












