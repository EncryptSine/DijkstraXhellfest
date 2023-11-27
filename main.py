"""
Script principal pour exécuter l'interface graphique de calcul du chemin le plus court.

Ce script crée une fenêtre Tkinter et initialise la classe GUI pour fournir
une interface utilisateur permettant de calculer le chemin le plus court entre deux scenes.
"""

from interface import GUI  # Importation de la classe GUI
import tkinter as tk  # Importation de la bibliothèque tkinter pour l'interface graphique

if __name__ == '__main__':

    # Création de la fenêtre principale Tkinter
    root = tk.Tk()

    # Initialisation de GUI avec la fenêtre Tkinter en tant que maître
    app = GUI(root)

    # Exécution de la boucle d'événements Tkinter
    root.mainloop()
