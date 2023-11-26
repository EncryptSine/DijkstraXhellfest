"""
Graphe_DijkstraVilles_eleve

@author:
    
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
            
#Retourne le degré du sommet donné.
    def degre(self, sommet):
        return len(self.graphe[sommet])
    
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

#Retourne l'ordre du graphe (le nombre de sommets).
    def ordre(self):
        return len(self.graphe)
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
        distance = {sommet: float('inf') for sommet in self.graphe}
        distance[s] = 0
        predesseur = {}

        sommerts_non_traites = list(self.graphe.keys())

        while sommerts_non_traites:
            u = min(sommerts_non_traites, key=lambda sommet: distance[sommet])
            sommerts_non_traites.remove(u)

            for voisin in self.graphe[u]:
                poids_uv = self.graphe[u][voisin]
                dist = distance[u] + poids_uv

                if dist < distance[voisin]:
                    distance[voisin] = dist
                    predesseur[voisin] = u
        
        chemin = []
        p = v
        while p != s:
            chemin.insert(0, p)
            p = predesseur[p]
        chemin.insert(0, s)

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
