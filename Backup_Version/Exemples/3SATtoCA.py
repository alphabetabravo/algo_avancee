#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

import fileinput

##Déclaration de la classe graph

class Graph :
    def __init__( self ) :
        self.v = set([])
        self.e = set([])
    ##Ajout d'un sommet dans le graph
    def add_v( self, x ) :
        try :
            it = iter(x)
            for i in it :
                self.v.add( i )
        except TypeError :
            self.v.add(x)
    
    def add_e( self, x ) :
        try :
            it = iter(x)
            for (u,v) in it :
                self.v.add( u )
                self.v.add( v )
                self.e.add( (u,v) )
        except TypeError :
            self.v.add( u )
            self.v.add( v )
            self.e.add( (u,v) )

if __name__ == "__main__" :

    C = 0
    for s in fileinput.input() :
        if s in [ "3SAT {\n", "3-SAT {\n" ] :
            g = Graph()
        elif len( s.split( ' ' ) ) == 2 :
            print( s.split( ' ' ))
            (n,m) = map( int, s.split( ' ' ) )
            g.add_e( [ (i,-i) for i in range( 1, n+1 ) ] )
        elif len( s.split( ' ' ) ) == 3 :
            (a,b,c) = map( int, s.split( ' ' ) )
            C1 = "C" + str(C) + "n1"
            C2 = "C" + str(C) + "n2"
            C3 = "C" + str(C) + "n3"
            g.add_e( [ (C1, C2), (C2,C3), (C1,C3) ] )
            g.add_e( [ ( C1, a ), (C2,b), (C3,c) ] )
            C += 1
    vertices = ""
    for i in g.v :
        vertices += "{} ".format( i )
    edges = ""
    for i in g.e :
        edges += "{}--{}\n".format( i[0], i[1] )
    print( "Graph {" )
    print( vertices )
    print( edges + "}" )
    print( "Entier {{\n{k}\n}}".format( k=n+2*m) )

