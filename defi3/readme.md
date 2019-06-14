# Explications :

Pour faire simple la faille est un "use after free"

On peut creer et suprimer des éléments mais le programme oublie de suprimer leur pointeurs auquels ont as encore accès.

On peut donc les réecrire pour changer l'adresse d'écriture dans la heap (à condition de créer et suprimer le bon nombre d'élements et ensuite de modifier les bon car ils vont ainsi se "chevaucher")

Avant tout je leak une adresse et j'y soustrait `0xb8` ce qui me permet de calculer l'adresse que je dois ecrire avec nom2 et vers où nom3 va donc pointer

ce qui me permet de modifier nom3 ce qui vas changer l'adresse vers ou id 0 va écrire.
je fait ça car on ne peut ecrire que 7 byte avec le noms mais on peut en ecrire jusqu'a 50 avec l'id

L'adresse que j'ai choisie vers laquelle va pointe id0 est donc celle ou se trouve l'adresse de la fonction atoll() dans la GOT (Global Offset Table si vous cherchez)

une fois que celà est fait je peut donc lire lire id0 pour obtenir cette adresse et ensuite je n'ai plus qu'a la rajouter à la différence entre l'adresse de la fonction system() et celle de atoll() dans libc
pour connaitre celle de system() malgrès l'aslr

une fois que cela est fait, je n'ai plus qu'a réecrire vers ou *atoll pointe dans la plt avec cette adresse en modifiant id0 et ainsi la prochaine fois que atoll() seras appelé
ce seras system() qui seras appelé à la place avec pour argument ceux que atoll() prenais originellement, ces arguments sont normalement le nom qu'on doit entrer quand on veut rajouter
un nouvel élément.
Plus qu'a mettre `/bin/bash` à la place du nom et atoll() étant maintenant system() va être appelé avec `/bin/bash` comme argument et ainsi nous donner un shell.

Voilà, n'hesitez pas à ouvrir une "issue" si vous avez des problèmes ou quelques chose doit être corrigé(cela inclu l'orthographe, pas mon fort haha), bonne continuation :).

Ah et j'ai aussi suprimé le TAG du dernier drapeau.

Pour le noaslr.py, vous devez mettre l'adresse de system (`p &system` dans gdb) et le lancer sans aslr soit avec gdb ou `(./noaslr.py;cat) | rarun2 aslr=no system=./prog.bin` 
