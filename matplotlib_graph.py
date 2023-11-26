"""
Module contenant une fonction pour tracer des points avec des chemins en utilisant matplotlib.
"""

# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from valeurs import noms_points, points

def tracer_point(graphe, x, y, figure=None):
    """
    Trace les points, les chemins et l'image de fond sur une figure Matplotlib.

    :param graphe: Instance de la classe de graphe utilisée pour calculer le chemin le plus court.
    :param x: Point de départ pour le chemin le plus court.
    :param y: Point d'arrivée pour le chemin le plus court.
    :param figure: Figure Matplotlib existante à utiliser (facultatif).
    :return: La figure Matplotlib mise à jour.
    """
    if figure is None:
        # Si la figure n'est pas fournie, créez une nouvelle figure
        figure, ax = plt.subplots()
    else:
        # Si la figure est fournie, utilisez les axes existants
        ax = figure.gca()
        
    # Faire un absolute path pour l'image de fond
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construire le chemin complet de l'image de fond
    fond_img_path = os.path.join(script_directory, 'fond.jpeg')
    fond_img = mpimg.imread(fond_img_path)
    
    # Afficher l'image de fond avec pour axe x et y de 0 à 7.5
    ax.imshow(fond_img, extent=[0, 7.5, 0, 7.5])

    # Tracer les points avec leurs noms personnalisés
    for nom, coordonnees in points.items():
        ax.scatter(coordonnees[0], coordonnees[1], label=noms_points[nom])

    # Tracer le chemin le plus court avec Dijkstra
    distance, chemin = graphe.dijkstra(x, y)
    x_chemin = [points[nom][0] for nom in chemin]
    y_chemin = [points[nom][1] for nom in chemin]
    ax.plot(x_chemin, y_chemin, color='blue', linewidth=2, label='Chemin le plus court')

    ax.set_title('Chemin vers la scène le plus court')

    # Ajouter une légende
    ax.legend()

    return figure  # Retourne la figure pour pouvoir la mettre à jour dans le GUI
