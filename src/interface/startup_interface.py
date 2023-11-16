import tkinter as tk
from tkinter import ttk, messagebox

class SudokuSolverInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        # Center the window on the screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = 400  # Adjust the window width as needed
        window_height = 300  # Adjust the window height as needed

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Set white background color
        self.master.configure(bg="white")

        self.create_widgets()

    def create_widgets(self):
        # Number of Cells Label and Entry
        self.cells_label = tk.Label(self.master, text="Number of Cells:",fg="black" ,  font=("Arial", 14), bg="white")
        self.cells_entry = tk.Entry(self.master, width=10, font=("Arial", 14))
        self.cells_label.grid(row=0, column=0, padx=10, pady=10)
        self.cells_entry.grid(row=0, column=1, padx=10, pady=10)

        # Algorithm Label and Dropdown
        self.algorithm_label = tk.Label(self.master, text="Algorithm:",fg="black",  font=("Arial", 14  ), bg="white" )
        self.algorithm_var = tk.StringVar()
        self.algorithm_dropdown = ttk.Combobox(self.master, textvariable=self.algorithm_var, values=["Algorithm 1", "Algorithm 2"], font=("Arial", 14))
        self.algorithm_label.grid(row=1, column=0, padx=10, pady=10)
        self.algorithm_dropdown.grid(row=1, column=1, padx=10, pady=10)

        # Solve Button
        self.solve_button = tk.Button(self.master, text="Solve Sudoku", command=self.solve_sudoku, font=("Arial", 14), width=20, height=2)
        self.solve_button.grid(row=2, column=0, columnspan=2, pady=20)

    def solve_sudoku(self):
        # Get user inputs
        num_cells = self.cells_entry.get()
        algorithm = self.algorithm_var.get()

        # Validate inputs
        if not num_cells.isdigit() or int(num_cells) <= 1:
            messagebox.showerror("Erreur", "Veuillez saisir un nombre de cellules valide.")
            return
        
        if int(num_cells) > 4 :
            messagebox.showerror("Erreur", "Veuillez saisir un nombre entre 2 et 4")
            return
        
        if not algorithm:
            messagebox.showerror("Error", "Veuillez selectionner un algorithme.")
            return

        # appel la fonction main de l'interface principale :
        # les parametre sont:
        # algorithme et int(num_cells)


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverInterface(root)
    root.mainloop()
