# Données des élections législatives françaises 2024

*par AstroAure*

Ce dépôt met à disposition de toustes chercheurs/chercheuses, journalistes ou amateurs/amatrices, les résultats complets par circonscription du premier tour des élections législatives françaises 2024.

Les données ont été récupérées directement sur le site du [Ministère de l'Intérieur et des Outre Mer](https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/index.html). Les tableaux publiés ici ont été réalisés le 01/07/2024 à 21:00 à partir de données qui peuvent encore évoluer en fonction de recours et de potentielles ré-élections.

Vous trouverez deux tableaux :
* [Résultats](results_legislatives_2024_T1.csv) : Résultats par circonscription, chaque ligne correspond à un candidat ;
* [Statistiques de vote](stats_legislatives_2024_T1.csv) : Statisitiques par circonscription (nombre d'inscrit.e.s, de votant.e.s, de votes blancs, de votes nuls).

Vous trouverez également deux notebooks Jupyter :
* [Collecte de données](DataScraping.ipynb) : Notebook servant à générer les tableaux de données. Il récupère les données directement sur le site du gouvernement et formate les données à partir de la page HTML ;
* [Analyse](Analyse.ipynb) : Notebook avec quelques analyses très basiques (calcul de participation nationale pour valider la collecte de données, nombre de député.e.s élu.e.s au premier tour, duels/triangulaires/quadrangulaires).

Les codes et tableaux sur ce dépôt sont sous license MIT (utilisation et partage libre pour tout usage, citation de l'auteur obligatoire, aucune garantie).