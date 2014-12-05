#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
import fileinput
import sys
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
        elif len( i.split( '--' ) ) == 3 :
				(n,m,o) = map( str, i.split( '--' ) )
				mySommet = recupSommet(graph,m)
				mySommet.color = o
    return graph

def initialisationCouleur(v, graph):
	print "OK FONCTION !"
	for i in v.input() :
		print "La ligne est : " + str(i)
		

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


if __name__ == "__main__" :
	v = fileinput

	graph = initialisationGraph(v)
	ajout_Voisin(graph)

	#affichage_graph_debug(graph)

	#~ print "####################################################"
	#~ print "#####    Lancement de la verification          #####"
	#~ print "####################################################"

	ret = verification(graph)
	sys.exit(ret)
















		

