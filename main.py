import tkinter as tk
from ui import ChatUI

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatUI(root)
    root.mainloop()