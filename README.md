algo_avancee
============

Pyhton , sur algo avancée - Probléme 3-Color graph

En l'état :

--> Le script pour la réduction fonctionne, pour le tester il faut :
    --> Se placer dans votre dossier ou il y a le projet
    --> Lancer la commande suivante dans un terminal
    python2.7 ./Exemples/gen3SAT.py 3 3 | python2.7 ./Reducteur/3SAT_TO_3COLOR.py
    
    Pour info :
    - Je fait avec la version 2.7 de python , a vous d'utiliser la votre ;)
    - Il est possible de virer les appel au compilo python en passant vos fichier en mode executable : chmod +x sur gen3SAT et sur 3SAT_TO_3COLOR.python  , Ce qui donnera la commande suivante :./Exemples./gen3SAT.py 3 3 | ./Reducteur./3SAT_TO_3COLOR.py
    
    - Dernier point , les arguments de gen3SAT définissent le nombre de variable et de clause :D , ne monter pas trop haut.
    ++ Il est également possible de rajouter 1 ou 0 apres les deux 3 pour forcer à avoir des probléme satisfaisable et non-satisfaisable
    
    Allez Good Luck :D

Le 25-11-2014 / 21h00

--> Ajout du PARSER pour le fichier en entrée du SOLVER de Graph3Couleur

Le fichier est présent dans le dossier : tempo_script_py

Le script fonctionne pour n'importe quel graph en entrée (même si les sommets sont de type string)

++ J'ai commencé à réfléchir au fonction pour la résolution


Y'a pas une odeur de pomme pourri sous votre clavier par hasard ?
