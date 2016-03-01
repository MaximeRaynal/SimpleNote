Simple Open Note
=========

Simple Open Note (SON), est une application de gestion et de prise de note.

Elle se veut simple et ouverte mais à la fois complète et puissante et sécurisé (cryptage client side et/ou server side).

Elle a pour but de gérér un ensemble de fichier texte ainsi que plusieur fichier attachés.

La version présente ici se compose en 3 partie distincte est indépendante :

1. Le coeur, qui permet de manager une gestion documentaire
2. Un serveur web qui simplifie les chose comme l'indexation et la recherche
   et qui fourni une API Rest
3. Une application web pour utiliser tout cela dans un navigateur

Cette instance est fourni avec un conteneur Docker pour simplifier l'installation
et l'utilisation.


Une note
---------

Une note au sens de cette application est un dossier qui contient au moins un fichier texte
et un ensemble de fichier joint.
Est généré pour ce dossier un fichier meta.json qui contient des informations descriptives
concernant les autres fichiers texte comme l'auteur, la date de création.
Il contient des informations important mais en aucun cas du contenu et peut être
regénéré (avec perte).

Organisation
---------

La gestion de l'ensemble de note est à la charge du serveur web.
Il est conseillé d'utiliser un système basé les tags (relation bi-directionnelle 0..N),
plutot qu'un système de dossier.