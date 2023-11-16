import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

root = tk.Tk()

frame_width = 200
frame_height = 100

frame = tk.Frame(root, width=frame_width, height=frame_height, bg="lightblue")
center_window(root, frame_width, frame_height)
frame.place(relx=0.5, rely=0.5)  # Use anchor to center the frame

root.mainloop()