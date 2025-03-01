# Jeu Tetris

Ce projet est une implémentation du célèbre jeu Tetris, réalisé en binôme dans le cadre du cours *ALGO2 - Algorithmique et Programmation 2* du semestre 2 de la **Licence 1 Informatique** à l'Université d'Artois, Faculté des Sciences Jean Perrin.
---
## Description du Projet

Le jeu Tetris se déroule sur un terrain vertical composé de cases carrées. Des formes géométriques appelées tétriminos tombent une par une et se placent au bas du terrain. Lorsqu'une ligne est complètement remplie, elle disparaît, permettant de libérer de l'espace. Le jeu prend fin lorsque les tétriminos empilés atteignent le sommet du terrain.

## Présentation du Jeu

Tetris est un jeu de puzzle classique où le but est de remplir des lignes horizontales avec des tétriminos. Ces formes, composées de carrés, doivent être manipulées pour s'emboîter parfaitement dans l'espace disponible. Chaque fois qu'une ligne est remplie, elle disparaît, et le joueur marque des points. L'objectif est de durer le plus longtemps possible sans que les tétriminos n'atteignent le sommet du terrain.

## Fonctionnalités

- Affichage graphique du plateau de jeu et des tétriminos en mouvement.
- Déplacement des tétriminos vers la gauche, la droite et vers le bas.
- Rotation des tétriminos pour les adapter à l'espace disponible.
- Système de score pour suivre les performances du joueur.
- Gestion des niveaux de difficulté, avec l'augmentation de la vitesse de chute des tétriminos au fur et à mesure du temps.

## Prérequis
Avant de lancer le jeu, assurez-vous d'avoir installé la bibliothèque `tkinter`. Si ce n'est pas déjà fait, vous pouvez l'installer avec la commande suivante (si vous utilisez Python 3) :

```bash
pip install tkinter
```
## Lancer le jeu
Une fois tkinter installé, il vous suffit d'exécuter le fichier pytetris.py pour lancer le jeu.
```bash
python pytetris.py
```

## Auteurs

Ce projet a été réalisé en binome avec , **MACHTER Massinissa** [https://github.com/machterMassi06] dans le cadre de notre licence 1 **(2022/2023)** en cours de ALGO2 - Algorithmique et Programmation 2.