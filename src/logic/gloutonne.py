def greedy_coloring(graph):
    colors = {}  # Dictionnaire pour stocker les couleurs attribuées à chaque sommet


    # Triez les sommets par degré décroissant
    sorted_vertices = sorted(graph, key=lambda x: len(graph[x]), reverse=True)


    for vertex in sorted_vertices:
        # Initialisez un ensemble des couleurs déjà utilisées par les voisins
        neighbor_colors = set(colors.get(neighbor, None) for neighbor in graph[vertex])

        # Trouvez la plus petite couleur non utilisée
        color = 1
        while color in neighbor_colors:
            color += 1

        # Attribuez la couleur au sommet
        colors[vertex] = color

    return colors

# Exemple d'utilisation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C'],
}

coloring = greedy_coloring(graph)
print(coloring)
