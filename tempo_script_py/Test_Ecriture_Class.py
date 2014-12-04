#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

import fileinput


class MyColor:
    def __init__( self ) :
        self.valColor = set([])
    def add_Color( self, nbColor ) :
								it = iter(nbColor)
								for u in it :
													self.valColor.add( u )
													
class Sommet :
    def __init__( self ,x, color) :
        self.x = x
        self.color = color
        self.listeVoisin = set([])
        self.nbVoisin = 0
        
    def setVoisin( self ,x) :
								self.listeVoisin.add( x )
								self.nbVoisin += 1

								
       
class Graph :
    def __init__( self ) :
        self.v = set([])
        self.e = set([])
    ##Ajout d'un sommet dans le graph.
    def add_v( self, Sommet ) :
									self.v.add( Sommet )
									
				##Ajout d'une arrête dans le graph
    def add_e( self, x ) :
        try :
            it = iter(x)
            for (u,v) in it :
                self.e.add( (u,v) )
        except TypeError :
            self.e.add( (u,v) )

def initialisationGraph(v) :
		list_sommet = []
		#list_SommetCol = []
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
		        #Pour chaque sommet on creer un objet de type Sommet avec la couleur à "nothing"
		        #Puis on l'ajoute dans le graph
		        for i in list_sommet :
																mySommet = Sommet(i,"nothing")
																g.add_v( mySommet )
		    elif len( s.split( '--' ) ) == 2 :
		        #On ajoute toutes les arrêtes sauf pour la derniére ligne
		        #On récupére le couple de sommets
		        s = s.replace('\n', '')
		        (n,m) = map( str, s.split( '--' ) )    
		        #On l'ajoute
		        g.add_e([(n,m)])
		return g



##########################################
########Programme Principale##############

#On récupére le fichier passé en input
v = fileinput
#On initialise le graph avec les bon sommets et les bonnes arrêtes
g = initialisationGraph(v)

#On ajoute les voisins
for j in g.v :
	for i in g.e :
		if i[0] == j.x :
			j.setVoisin(i[1])
		elif i[1] == j.x :
			j.setVoisin(i[0])

#Affichage des sommets et des arrêtes du graph
for i in g.v :
	print "Le sommet est : " + i.x
	print "Sa couleur vaut : " + i.color
	print "Son nombre de voisin est :  " + str(i.nbVoisin)
	print "Les voici : "
	for j in i.listeVoisin :
			print j


#Algo pour résoudre le probléme


#On choisi un sommet , "Le premier de la liste " - On pourrais émettre une heuréstic sur ce choix.
#Colorisation : G: graph i: sommet
#pour chaque voisin de i
#				pour chaque couleurs 
#										si verify_couleur possible
#												On mets la couleur
											
#										si impossible --> echec
#    fin pour
#fin pour
#-->succés

def coloriAge(g,lCol) :
		for i in g.v :
			 if i.color == "nothing" :
						for col in lCol : 
								if verifyCol(i.color,col) == 0 then
										i.color = col
										ret coloriAge(g,lcol)
								else
										ret = 0
		return ret
		

#Ajout du bon nombre de couleur par rapport au choix utilisateur
choiXcol = MyColor()
choiXcol.add_Color(["vert","jaune","rouge"])



