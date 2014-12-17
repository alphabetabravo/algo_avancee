#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
from sys  import argv, exit, path
from random import randint, random
from itertools import product

MAX_ITER = 100000

class TroisClause :
	def __init__( self, x, y ,z ) :
		self.literaux = (x,y,z)

	def val( self, variables ) :
		x,y,z = self.literaux
		if x > 0 :
			lx = variables[x-1]
		else :
			lx = not variables[-x-1]

		if y > 0 :
			ly = variables[y-1]
		else :
			ly = not variables[-y-1]

		if z > 0 :
			lz = variables[z-1]
		else :
			lz = not variables[-z-1]
		return lx or ly or lz

	def __repr__( self ) :
		x,y,z = self.literaux
		return "{} {} {}".format( x, y, z )

class TroisSAT :
	def __init__( self, n, m ) :
		self.nb_var = n
		self.nb_clauses = m
		self.clauses = []

	def add_clause( self, x, y, z ) :
		if not( 1 <= abs( x ) <= self.nb_var ) or \
		   not( 1 <= abs( y ) <= self.nb_var ) or \
		   not( 1 <= abs( z ) <= self.nb_var ) :
			print( "Nombre de variables invalide" )
			exit( 1 )
		self.clauses.append( TroisClause( x, y, z ) )
	
	def satisfaisable( self, affiche_sol = False ) :
		if len( self.clauses ) != self.nb_clauses :
			print( "Erreur, nombre de clauses incorrect" )
			exit( 1 )
		l = [ True, False ]
		s = "product( l "
		for i in range( self.nb_var-1 ) :
			s += ", l"
		s += " )"
		for variables in eval( s ) :
			ok = True
			for c in self.clauses :
				ok = c.val( variables )
				if not ok :
					break
			if ok :
				if affiche_sol :
					print( variables )
				return True
		return False

	def __repr__( self ) :
		s = "3SAT {\n"
		s += "{} {}\n".format( self.nb_var, self.nb_clauses )
		for c in self.clauses :
			s += "{}\n".format( c )
		s += "}"
		return s

	def __iter__( self ) :
		return iter( self.clauses )



def usage() :
    print( "Usage : " + argv[0] + " n m [s]" )
    print( "  Génère une instance de 3sat aléatoirement" )
    print( "  Paramètres :" )
    print( "  n : (entier) nombre de variables" )
    print( "  m : (entier) nombre de clauses" )
    print( "  s : (0 ou 1) paramètre optionnel, si spécifié, 1 force la génération"  )
    print( "      d'une instance satisfaisable alors que 0 force une instance" )
    print( "      non-satisfaisable" )
    print( "" )
    print( "Exemples : " )
    print( argv[0] + " 3 4" )
    print( argv[0] + " 4 4 0" )
    print( argv[0] + " 5 4 1" )


def sign() :
    if random() < 0.5 :
        return 1
    else :
        return -1

def genTroisSAT( n, m ) :
    I = TroisSAT( n, m )
    for i in range(m) :
        x = sign() * randint( 1, n )
        y = sign() * randint( 1, n )
        z = sign() * randint( 1, n )
        I.add_clause( x, y, z )
    return I

if __name__ == "__main__" :
    if len( argv ) < 2 :
        usage()
        exit( 1 )
    n = int( argv[1] )
    m = int( argv[2] )

    I = genTroisSAT( n, m )
    if len( argv ) == 3 :
        print( I )
    else :
        if argv[3] == "1" :
            satis = True
        elif argv[3] == "0" :
            satis = False
        k = 0
        while I.satisfaisable() != satis and k < MAX_ITER :
            I = genTroisSAT( n, m )
            k += 1
        if k == MAX_ITER :
            s = "Erreur : aucune instance "
            if not satis :
                s += "non-"
            s += "satisfaisable à {} variables et {} clauses trouvée".format( n, m )
            print( s )
            exit( 1 )
        print( I )
    exit( 0 )

