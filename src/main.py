"""
Fase4SantiagoVilla — Entry point.

Bootstraps the Tkinter root, the Controlador, and the LoginWindow.
The MainWindow is opened by LoginWindow upon successful authentication.
"""

import sys
import os

# Allow imports from src/ regardless of where the script is run from
sys.path.insert(0, os.path.dirname(__file__))

import tkinter as tk
from controllers.controlador import Controlador
from views.login_window import LoginWindow
from views.main_window import MainWindow


def main() -> None:
    """Application entry point."""
    root = tk.Tk()
    root.withdraw()          # hide root; LoginWindow is the first visible window
    root.title("Fase4SantiagoVilla")

    ctrl = Controlador()

    def abrir_principal() -> None:
        """Callback passed to LoginWindow; opens MainWindow after login."""
        MainWindow(root, ctrl)

    LoginWindow(root, ctrl, on_success=abrir_principal)
    root.mainloop()


if __name__ == "__main__":
    main()
