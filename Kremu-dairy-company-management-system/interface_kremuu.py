# This is the kremuu interface made with Tkinter.
import tkinter as tk

# This are the most used colors.
BACKGROUND = "#111827"
SIDEBAR = "#0B1720"


class KremuuDesktopApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Sistema de Gestion Empresarial Kremuú")
        self.window.state('zoomed') # I specify that the window will occupy the entire screen. 
        self.window.minsize(1000, 800)

        # This is the main frame to show information and make processes.
        self.main_frame = tk.Frame(bg=BACKGROUND)
        self.main_frame.pack(side="right", fill="both", expand=True)

        # This is the left-hand bar.
        self.sidebar = tk.Frame(bg=SIDEBAR, width=30)
        self.sidebar.pack(side="left", fill="y")

        # Menu frame is child of sidebar
        self.menu = tk.Frame(self.sidebar, bg=SIDEBAR)
        self.menu.pack(side="top", fill="both", expand=True)

        # This frame define the location of the logo.
        self.logo_frame = tk.Frame(self.sidebar, bg=SIDEBAR)
        self.logo_frame.pack(side="bottom", fill="x")





    def initialize_window(self):
        """This method inicialize the kremuu app"""
        self.window.mainloop()





