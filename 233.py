import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("NikonKikkeli")
window.geometry("300x300")


img = ImageTk.PhotoImage(Image.open("next.png"))
panel = tk.Label(window, image = img)

panel.pack(side = "bottom", fill = "both", expand = "yes")
window.mainloop()

