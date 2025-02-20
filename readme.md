# Plan Comptable Général eic 2025 (PCG) - Format Lisible par Machine

## Objectif
L'objectif de ce dépôt est de proposer un nouveau format du PCG qui soit plus facilement exploitable par des systèmes informatiques.
Ce format de PCG révisé facilite l'automatisation des processus comptables et à améliorer l'interopérabilité entre différents systèmes de gestion comptable.

## Introduction
Le PCG est un ensemble de règles et de normes comptables qui régissent la tenue des comptes en France.
Ce dépôt contient une version du PCG français, révisée pour être plus lisible par les machines.
La version est celle des entreprises industrielles et commerciales (eic) du 1er janvier 2025.
La source officielle de ce document est l'Autorité des Normes Comptables (ANC).

## Structure du Dépôt
data/ : Contient les fichiers de données au format lisible par machine.
scripts/ : Contient les scripts utilisés pour transformer le document PDF officiel en formats lisibles par machine.
docs/ : Contient la documentation supplémentaire et les guides d'utilisation.

## Ordre des scripts

- 01_complet.py  extrait tout le PDF vers un nouvau fichier au format TXT
- 02_comptes.py  extrait uniquement le plan de compte du PDF vers un nouveau fichier au format TXT

## Sources
- [x] Source Officielle du Plan Comptable Général
Le document officiel du PCG peut être consulté sur le site de l'ANC :
Recueil des Normes Comptables Françaises - Janvier 2025
https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_Janvier2025/Recueil-NF-Janvier-2025.pdf
- [x] PyMuPDF librairie python (fitz)
https://github.com/pymupdf/PyMuPDF

## Améliorations to-do-list
- [ ] Indiquer les actions effectuées par chaque script dans docs
- [ ] doc 01_complet.py
- [ ] doc 02_comptes.py
- [ ] supprimer les références implicites dans le PCG comme "2813 Constructions (même ventilation que celle du compte 213)"
- [ ] inclure une version 3 qui comporte le complet et les comptes
- [ ] faire en sorte que le script version 3 appelle en réalité le script version 2 de façon modifiée, avec un critère d'entrée différent
- [ ] les actions listées dans la doc doivent être classées avec une numérotation commune
- [ ] un script global doit pouvoir vérifire que les règles énnoncées comme appliquées dans la doc sont effectivement appliquées dans le code et dans les sorties
- [ ] voir une orchestration d'IA : un agent appelant un autre agent pour mener une tâche
- [ ] comment permettre à un LLM en local d'avoir accès à la lecture des fichiers locaux
- [ ] comment gérer des permissions pour donner l'accès à certains répertoires uniquement

## Contributions
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce format ou ajouter de nouvelles fonctionnalités, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.