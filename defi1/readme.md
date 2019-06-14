# Explications :

Le programme apelle la fonction system() en lui donnant pour argument `date` au lieu de donner un chemin absolu,
on peut ainsi en changeant la variable d'environment faire en sorte que system() execute plûtot ./date au lieu de /bin/date
