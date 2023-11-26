"""
Module contenant une classe GUI pour créer une interface graphique de calcul du chemin le plus court.
"""
# Importation des bibliothèques nécessaires
import tkinter as tk 
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Dijkstra import GrapheHelfest
from matplotlib_graph import tracer_point
import matplotlib.pyplot as plt
from valeurs import noms_points

class GUI:
    def __init__(self, master):
        """
        Initialise l'interface graphique avec les éléments nécessaires.

        :param master: Le widget maître (fenêtre principale) de Tkinter.
        """
        self.master = master
        self.master.title("Calcul du chemin le plus court entre les scènes du Hellfest !")

        # Initialisation du graphe
        self.graphe = GrapheHelfest()

        # Création des widgets
        self.create_widgets()

        # Affiche le graphique des points dès le lancement de l'application
        self.afficher_points()

    def create_widgets(self):
        """
        Crée et place les widgets nécessaires dans l'interface graphique.
        """
        
        # Ajout d'un Label pour le point de départ ainsi qu'un menu déroulant
        tk.Label(self.master, text="Point de départ:").grid(row=0, column=0, padx=10, pady=10)
        self.depart_entry = ttk.Combobox(self.master, values=list(noms_points.values()))
        self.depart_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Ajout d'un Label pour le point d'arrivée ainsi qu'un menu déroulant
        tk.Label(self.master, text="Point d'arrivée:").grid(row=1, column=0, padx=10, pady=10)
        self.arrivee_entry = ttk.Combobox(self.master, values=list(noms_points.values()))
        self.arrivee_entry.grid(row=1, column=1, padx=10, pady=10)

        # Ajout d'un bouton qui calcule le chemin le plus court grâce à la fonction calculer_et_afficher
        self.calculer_button = tk.Button(self.master, text="Calculer", command=self.calculer_et_afficher)
        self.calculer_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Ajout d'un Label pour afficher les résultats
        self.resultats_label = tk.Label(self.master, text="")
        self.resultats_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Configuration du graphique Matplotlib qui affiche le chemin le plus court
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)
        self.canvas.draw()

    def calculer_et_afficher(self):
        """
        Effectue le calcul du chemin le plus court et affiche les résultats dans l'interface graphique.
        """
        
        # Récupération des points de départ et d'arrivée à partir d'un menu déroulant
        depart = [key for key, value in noms_points.items() if value == self.depart_entry.get()][0]
        arrivee = [key for key, value in noms_points.items() if value == self.arrivee_entry.get()][0]
        
        # Calcul du chemin le plus court et récupération des résultats
        distance, chemin = self.graphe.dijkstra(depart, arrivee)
        
        nom_depart = noms_points[depart]
        nom_arrivee = noms_points[arrivee]

        resultat_texte = f"Distance minimale entre '{nom_depart}' et '{nom_arrivee}': {distance}\n"
        resultat_texte += f"Chemin le plus court : {' -> '.join([noms_points[point] for point in chemin])}"

        # Affichage des résultats dans l'interface graphique
        self.resultats_label.config(text=resultat_texte)

        # Appel de la fonction tracer_point et récupération de la figure
        figure = tracer_point(self.graphe, depart, arrivee)

        # Utilisation de FigureCanvasTkAgg pour afficher la figure dans la fenêtre Tkinter
        canvas = FigureCanvasTkAgg(figure, master=self.master)
        canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)
        canvas.draw()

    def afficher_points(self):
        """
        Affiche le graphique les points dans l'interface graphique dès le lancement de l'application.
        """
        # Appel de la fonction tracer_point et récupération de la figure
        figure = tracer_point(self.graphe, "A", "A")

        # Utilisation de FigureCanvasTkAgg pour afficher la figure dans la fenêtre Tkinter
        canvas = FigureCanvasTkAgg(figure, master=self.master)
        canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)
        canvas.draw()
