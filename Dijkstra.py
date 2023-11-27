"""
Fonction Dijkstra(s, v)
    distance <- {sommet: infini pour sommet dans graphe}
    distance[s] <- 0
    predesseur <- {} (un dictionnaire vide)

    sommets_non_traites <- Liste des sommets du graphe

    Tant que sommets_non_traites n'est pas vide
        u <- Sommet avec la distance minimale dans sommets_non_traites

        Retirer u de sommets_non_traites

        Pour chaque voisin dans les voisins de u
            poids_uv <- Poids de l'arête entre u et voisin
            dist <- distance[u] + poids_uv

            Si dist < distance[voisin]
                distance[voisin] <- dist
                predesseur[voisin] <- u
    Fin Tant que
    
"""
class GrapheHelfest:
    def __init__(self, graphe={}, NO=True):
        self.graphe = graphe
        self.NO = NO
#Ajoute un sommet au graphe s'il n'existe pas déjà.
    def sommet(self, sommet1):
        if sommet1 not in self.graphe.keys():
            self.graphe[sommet1] = {}
    
#Ajoute une arête entre deux sommets avec un poids spécifié.

    def arete(self, sommet1, sommet2, poids=1):
        # Si le sommet1 n'existe pas, il faut le créer
        if sommet1 not in self.graphe.keys():
            self.graphe[sommet1] = {}
        # Si le sommet2 n'existe pas, il faut le créer
        if sommet2 not in self.graphe.keys():
            self.graphe[sommet2] = {}
        self.graphe[sommet1][sommet2] = poids
        if self.NO:
            self.graphe[sommet2][sommet1] = poids
    
#Affiche la liste des sommets avec leurs voisins et les poids des arêtes.
    def liste(self):
        for sommet in self.graphe:
            print(sommet, '->', self.graphe[sommet])
#Retourne une matrice d'adjacence du graphe.
    def get_matrice(self):
        rang = {}
        i = 0
        # Affecte un rang à chaque sommet pour construire la matrice
        for sommet in self.graphe:
            rang[sommet] = i
            i += 1
        # Initialise la matrice avec des 0
        matrice = [[0] * len(self.graphe) for i in range(len(self.graphe))]

        for sommet1 in self.graphe:
            for sommet2 in self.graphe[sommet1]:
                matrice[rang[sommet1]][rang[sommet2]] = self.graphe[sommet1][sommet2]
        return matrice
    
#Affiche la matrice d'adjacence du graphe.
    def matrice(self):
        matrice = self.get_matrice()
        for ligne in matrice:
            print(ligne)
            
#Applique l'algorithme de Dijkstra pour trouver le chemin le plus court entre les sommets s et v. Retourne la distance et le chemin.
    def dijkstra(self, s, v):
        """
        Applique l'algorithme de Dijkstra pour trouver le chemin le plus court entre les sommets s et v.
        Retourne la distance et le chemin.

        Args:
            s: Le sommet de départ.
            v: Le sommet d'arrivée.

        Returns:
        tuple: La distance minimale et le chemin.
        """
        # Initialisation des distances à l'infini pour tous les sommets sauf le sommet de départ s.
        distance = {sommet: float('inf') for sommet in self.graphe}
        distance[s] = 0

        # Initialisation du dictionnaire des prédécesseurs.
        predesseur = {}

        # Liste des sommets non encore traités.
        sommets_non_traites = list(self.graphe.keys())

        # Boucle principale de l'algorithme de Dijkstra.
        while sommets_non_traites:
            # Sélectionne le sommet u avec la plus petite distance parmi les sommets non traités.
            u = min(sommets_non_traites, key=lambda sommet: distance[sommet])
            # Retire u de la liste des sommets non traités.
            sommets_non_traites.remove(u)

            # Parcourt tous les voisins de u.
            for voisin in self.graphe[u]:
                # Calcule la distance jusqu'à ce voisin en passant par u.
                poids_uv = self.graphe[u][voisin]
                dist = distance[u] + poids_uv

                # Met à jour la distance si une distance plus courte est trouvée.
                if dist < distance[voisin]:
                    distance[voisin] = dist
                    predesseur[voisin] = u

        # Reconstruction du chemin le plus court à partir des prédécesseurs.
        chemin = []
        p = v
        while p != s:
            chemin.insert(0, p)
            p = predesseur[p]
        chemin.insert(0, s)

        # Retourne la distance minimale et le chemin.
        return distance[v], chemin


# Exemple d'utilisation des villes
graphe = GrapheHelfest()

graphe.sommet('A')
graphe.sommet('B')
graphe.sommet('C')
graphe.sommet('D')
graphe.sommet('E')
graphe.sommet('F')
## Ajout d'arêtes avec des poids représentant les distances entre les villes
graphe.arete('A', 'B', 200)
graphe.arete('A', 'C', 680)
graphe.arete('B', 'C', 860)
graphe.arete('B', 'F', 1120)
graphe.arete('A', 'F', 1040)
graphe.arete('C', 'F', 1320)
graphe.arete('C', 'D', 200)
graphe.arete('D', 'F', 1400)
graphe.arete('D', 'E', 360)
graphe.arete('E', 'F', 1380)

print(graphe.matrice())