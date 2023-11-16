import tkinter as tk
from itertools import product
from tkinter import messagebox

import sys
import os

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(SCRIPT_DIR))

from logic.graph_classes.Graphe import Graphe


#################################################################
#####  INTERFACE FUNCTION FOR THE SUDOKU TABLE ##################

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


def create_3x3_box(parent , n_cells):
    box_frame = tk.Frame(
        parent, width=90, height=90, borderwidth=1, relief=tk.GROOVE, bg="white"
    )
    box_frame.pack_propagate(False)

    data = []

    for i in range(n_cells):
        row_data = []
        for j in range(n_cells):
            cell = tk.Frame(
                box_frame,
                width=30,
                height=30,
                borderwidth=1,
                relief=tk.GROOVE,
                bg="white",
            )
            cell.grid(row=i, column=j)

            # Entry widget to allow writing on the boxes
            entry = tk.Entry(cell, width=3,  font=("Arial", 20))
            entry.grid(row=i, column=j)
            row_data.append(entry)

        data.append(row_data)

    return box_frame, data


def create_NxN_boxes(root, N):
    main_frame = tk.Frame(root)
    

    box_data = []

    for i in range(N):
        row_data = []
        for j in range(N):
            sub_box, sub_box_data = create_3x3_box(main_frame , N)
            sub_box.grid(row=i, column=j)
            row_data.append(sub_box_data)

        box_data.append(row_data)

    return main_frame, box_data


def read_sudoku(box_data, n_cells):
    G = Graphe(n_cells)

    for i in range(n_cells):
        for j in range(n_cells):
            for i_cell in range(3):
                for j_cell in range(3):
                    result = G.add_to_dictionnary(
                        i, j, i_cell, j_cell, box_data[i][j][i_cell][j_cell].get()
                    )
                    if result == 1:
                        # print messege box erreur : 0 >= intval >= 10
                        messagebox.showerror(
                            "Erreur de valeur",
                            "les valeurs doivent être comprises entre 1 et 9. ",
                        )
                        return None

                    if result == 2:
                        # print messege box erreur : pas de str allowed
                        messagebox.showerror(
                            "Erreur de valeur", "les valeurs doivent être entière"
                        )
                        return None
    # the graph before claculation
    return G


def main(algo , num_cells):
    root = tk.Tk()
    root.title("Sudoku Solver")

    frame_width = 1800
    frame_height = 900

    # Create a Canvas widget
    canvas = tk.Canvas(root, width=frame_width, height=frame_height)
    canvas.pack()

    # Draw a horizontal line in the middle of the canvas
    vertical_line = canvas.create_line(frame_width // 2, 0, frame_width // 2, frame_height, fill="black", width=2)


    # pour centrer l'interface
    center_window(root, frame_width, frame_height)



    # result_table = tk.Label(root, text="", justify="left")
    # result_table.place(x= 10 , y=30)

    main_frame, box_data = create_NxN_boxes(root, num_cells)
    # main_frame.pack(padx= 10 , pady= 10)
    main_frame.place(x= 10 , y=80)

    # Button to solve Sudoku
    solve_button = tk.Button(
        root, width= 9 , text="Solve", command=lambda: read_sudoku(box_data, num_cells) ,font=("Arial", 20)
    )
    solve_button.place(x= 10 , y=30)






    root.mainloop()




if __name__ == "__main__":
    main( "hello" , 4)
