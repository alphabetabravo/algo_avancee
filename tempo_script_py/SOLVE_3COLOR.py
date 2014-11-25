#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

import fileinput
########################################################################
## Programme qui fait la resolution du coloriage à 3 couleur d'un graphe
########################################################################

##Déclaration de la classe graph

class Graph :
    def __init__( self ) :
        self.v = set([])
        self.e = set([])
    ##Ajout d'un sommet dans le graph.
    def add_v( self, x ) :
        try :
            it = iter(x)
            for i in it :
                self.v.add( i )
        except TypeError :
            self.v.add(x)
    ##Ajout d'une arrete dans le graph.
    ##L'ajout d'une arrete induit l'ajout des deux sommets.
    def add_e( self, x ) :
        try :
            it = iter(x)
            for (u,v) in it :
                #self.v.add( u )
                #self.v.add( v )
                self.e.add( (u,v) )
        except TypeError :
            #self.v.add( u )
            #self.v.add( v )
            self.e.add( (u,v) )
            
            
def initialisationGraph(v) :
		list_sommet = []
		for s in v.input() :
		    #print fileinput.filelineno()
		    #print s
		    #Récupération de la premiére ligne
		    if v.filelineno() == 1 :
		        g = Graph()
		    elif v.filelineno() == 2 :
		        #On récupére tous les sommets
		        list_sommet = map(str, s.split(" ") )
		        #On retire le dernier (\n)
		        list_sommet.pop()
		        #On ajoute tous les sommet dans le graphe
		        #print list_sommet
		        g.add_v( [ (i) for i in list_sommet ] )
		    elif len( s.split( '--' ) ) == 2 :
		        #On ajoute toutes les arrêtes sauf pour la derniére ligne
		        #On récupére le couple de sommets
		        (n,m) = map( str, s.split( '--' ) )
		        #On l'ajoute
		        g.add_e( [ (n,m) ] )
		return g

def coloriage3Couleur(G) :
		#Parcour de tous les sommets
		for i in g.v :
			#On verifie si le sommet possede une couleur
			if i.couleur == "":
				#On verifi si on peut attribuer la couleur rouge au sommet i
				if verify(G,i,"rouge") == 0:
					i.couleur = "rouge"
					return coloriage3Couleur(G)
				#On verifi si on peut attribuer la couleur vert au sommet i
				if verify(G,i,"vert") == 0:
					i.couleur = "vert"
					 return coloriage3Couleur(G)
				#On verifi si on peut attribuer la couleur jaune au sommet i
				if verify(G,i,"jaune") == 0:
					i.couleur = "jaune"
					return coloriage3Couleur(G)
				return 1
		return 0

#Paramétre entrée :
	#g : Un graphe
	#i : Le sommet 
	#couleur : La couleur a verifier
#Paramétre sortie :
	#0 : On peut affecter la couleur en paramétre au sommet i
	#1 : Un sommet voisin posséde déja cette couleur
def verify(g,i,couleur):
		#On fixe la couleur de i au paramétre couleurDistance
		i.couleur = couleur
		#Parcour des voisin pour verifie que la couleur peut etre mise sur le sommet i
		#Parcour de tous les sommets
		for j in g.v :
			#On parcours toutes les arrêtes
			for k in g.e :
				#On verifie les sommets des arrêtes
				if (k[0]==i or k[1]==j) and (k[0]==j or k[1]==i):
					#On verifie que k[0] et k[1] ne soit pas les mêmes (== uen arrete qui boucle sur le mêmesommet)
					if k[0] != k[1] :
						#On verifie que le sommet j possédent une couleur
						if j.couleur != "":
							# On peut verifie que la couleur n'est pas la même
							if i.couleur == j.couleur :
								return 1
		return 0

## PARTIE MAIN DU PROGRAMME ##

#On récupére le fichier passé en input
v = fileinput
#On initialise le graph avec les bon sommets et les bonnes arrêtes
g = initialisationGraph(v)

#Affichage des sommets et des arrêtes du graph
for i in g.v :
	print i
for i in g.e :
	print i[0] + "--" + i[1]


