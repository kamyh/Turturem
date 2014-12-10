Turturem
========

Le Turturem est un langage basé sur le latin servant à généré des scripts pour la bibliothèque Turtle en python.

Mot Clef
========
goto	ire

for	quia

step	gradus

end	finis

end line	<

start	initium

square	quadratum

trangle	triangulum

circle	circulus

black	nigrum

red	rufus

blue	caeruleum

green	viridis


Utilisation
========
gradus :{Integer} , représente la variable d’avancement de la boucle for, lors de cette boucle {Integer} prendra la valeur de la profondeur de l’imbrication. 
quia.{valeur de départ}.{pas}.{valeur de fin}
ire.{x}.{y}
Les motifs de bases s’utilisent de la manière suivante :
	{Motif}.{taille}.{couleur}
Les instructions ce finissent par 
	{Instruction}<




Exemples
========
Création d’un cercle de rayon 10 et de couleur bleu :
circulus.10.caeruleum<
Création d’un carré de rayon 10 et de couleur bleu :
	quadratum.10.caeruleum<
Création d’un triangle de rayon 10 et de couleur bleu :
triangulum.10.caeruleum<
Création de plusieurs cercles de rayon différents avec le même centre :
	quia.10.1.0<
	circulus.gradus:0.caeruleum<
	finis<

Création d’un carré, se place à une nouvelle position et dessine un carré.
quadratum.10.caeruleum<
	ire.12.3<
	quadratum.10.caeruleum<

Exemple de boucles imbriquées.

quia.10.1.0<
	quia.10.1.0<
	quadratum.gradus:0.caeruleum<
	finis<
	quadratum.gradus:1.caeruleum<
	finis<
