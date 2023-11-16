class Graphe:
    def __init__(self):
        self.graph = {}

    def __init__(self, sudoku_taille: int):
        self.graph = {}
        self.sudoku_taille = sudoku_taille
        self.sudoku_matrice = []
        for i in range(sudoku_taille * sudoku_taille):
            sub_list = []
            for j in range(sudoku_taille * sudoku_taille):
                # cette commande retourne [NONE , id de la case (sommet prochainement) format "box ligne-box _ num de la case" ]
                # 1 2 3
                # 4 5 6
                # 7 8 9
                numDeLaCase = (j % sudoku_taille) + 1 + sudoku_taille * (i % sudoku_taille)
                box_ligne = i // sudoku_taille
                box_colomn = j // sudoku_taille

                id_case = f"{box_ligne}_{box_colomn}_{numDeLaCase}"
                
                
                sub_list.append([None, id_case])
                self.graph[id_case] = None
            self.sudoku_matrice.append(sub_list)

    def add_to_dictionnary(self, i: int, j: int, case_i: int, case_j: int, value: str):
        if value == "" or value.isspace():
            return 0
        


        # >???????????????????????????????????????????????????????
        # check this .,.should intval return according to sudoku 
        # taille example 4*4 should check for hexadecimal one digit 



        try:
            intval = int(value)
            
            if  intval <= 0 or  intval >= (self.sudoku_taille * self.sudoku_taille) + 1:
                return 1
                # after returning 0 i should print message box "0 >= intval >= 10"
        except ValueError:
            return 2

        # to revisit this expression
        numDeLaCase_calculated = (case_j) + 1 + self.sudoku_taille * (case_i)

        # ajout de la valeur trouver dans le dict pour le calcule ulterieur+
        self.graph[f"{i}_{j}_{numDeLaCase_calculated}"] = intval

        # success
        return 0

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # If the graph is undirected

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []

    def __str__(self):
        return str(self.graph)


# # Example usage:
# g = Graphe(4)


# for i in g.sudoku_matrice:
#     print(i)
# print("\n\n")
# print(g.graph)
