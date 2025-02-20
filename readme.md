#Plan Comptable Général eic 2025 (PCG) - Format Lisible par Machine

##Introduction
Le PCG est un ensemble de règles et de normes comptables qui régissent la tenue des comptes en France.
Ce dépôt contient une version du PCG français, révisée pour être plus lisible par les machines.
La version est celle des entreprises industrielles et commerciales (eic) du 1er janvier 2025.
La source officielle de ce document est l'Autorité des Normes Comptables (ANC).

##Objectif
L'objectif de ce dépôt est de proposer un nouveau format du PCG qui soit plus facilement exploitable par des systèmes informatiques.
Ce format vise à faciliter l'automatisation des processus comptables et à améliorer l'interopérabilité entre différents systèmes de gestion comptable.

##Structure du Dépôt
data/ : Contient les fichiers de données au format lisible par machine.
scripts/ : Contient les scripts utilisés pour transformer le document PDF officiel en formats lisibles par machine.
docs/ : Contient la documentation supplémentaire et les guides d'utilisation.

##Ordre des scripts

- 01_complet.py  extrait tout le PDF vers un nouvau fichier au format TXT
- 02_comptes.py  extrait uniquement le plan de compte du PDF vers un nouveau fichier au format TXT

#Sources
1-Source Officielle du Plan Comptable Général
Le document officiel du PCG peut être consulté sur le site de l'ANC :
Recueil des Normes Comptables Françaises - Janvier 2025
https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_Janvier2025/Recueil-NF-Janvier-2025.pdf
2-PyMuPDF librairie python (fitz)
https://github.com/pymupdf/PyMuPDF


3Contributions
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce format ou ajouter de nouvelles fonctionnalités, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.