import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Ramanujan Machine")

# Create a label to display a brief description of the Ramanujan Machine
description_label = tk.Label(window, text="The Ramanujan Machine is a powerful computational tool used to solve mathematical problems and perform complex calculations. It is named after the famous Indian mathematician Srinivasa Ramanujan, who made significant contributions to the field of mathematics.")
description_label.pack()

# Create a label to display the technical specifications of the Ramanujan Machine
specs_label = tk.Label(window, text="Technical specifications: \n - Processor: Quad-Core \n - Memory: 16GB \n - Storage: 1TB \n - Operating System: Linux")
specs_label.pack()

# Run the main loop to display the GUI
window.mainloop()