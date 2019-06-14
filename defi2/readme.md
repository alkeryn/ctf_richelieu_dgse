# Explications :
Le stack est executable mais du à aslr on ne peut pas savoir ou jumper
donc on overflow d'abort notre stack au moment d'écrire le mot de passe pour réecrire l'adresse de retour vers 0x400538 qui est l'adress d'un gadget qui fait `call rax`
hors rax contient l'adresse de la deuxième ligne du stack a ce moment là et nous fait donc jump sur le stack qu'on controle

Néanmoins on ne peut pas mettre n'importe quelle shellcode car un byte est toujours changé en `\x00` ce qui va donc couper nimporte quelle shellcode trop longue
par une instruction invalide resultant en un segfault

La solution à ce probleme est de mettre au tout début de notre payload un `\xeb\x10` (instruction `jmp 0x10`) qui va nous faire faire sauter de 10 byte / octets en avant juste après le nullbyte et en pleins
dans la nop slide, la nop slide n'étais pas nécésaire si on calculais exactement le jump, mais de toute façon il nous fallais un padding jusqu'au nullbyte et le dépasser un peut ne coute
rien et permet de ne pas se prendre la tête.
ensuite vient notre réel shellcode qui pour ce cas précis execute juste sh.
