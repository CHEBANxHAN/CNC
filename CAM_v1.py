from tkinter import Tk, Label, Button, Entry, Canvas
import tkinter as tk
from PIL import Image

class MainRoot():
    def __init__(self, master):
        self.master = master

        self.entry = Entry(master)
        self.bt_sev = Button(master, text="Convect", padx="5", pady="3", command=self.draw)
        self.bt_sev1 = Button(master, text="Delete", padx="5", pady="3", command=self.delete)
        self.canvas = Canvas(master, bg="white", width=500, height=500)
        self.textn = Label(master, text="", font=("Microsoft Yahei", 14))

        self.entry.pack(side=tk.LEFT)
        self.bt_sev.pack(side=tk.LEFT)
        self.bt_sev1.pack(side=tk.LEFT)
        self.textn.pack(side=tk.LEFT)
        self.canvas.pack(anchor="e", expand=1)

    def draw(self):
        self.canvas.delete("all")
        try:
            name = self.entry.get()
            nameX = 500
            nameY = 500
            img = Image.open(name).convert('1')
            img = img.resize((nameX, nameY))
            mass = list(img.getdata())

            count = 0
            a = []
            data = []

            for h in mass:
                count += 1
                a.append(h)
                if count >= nameX:
                    data.append(a)
                    a = []
                    count = 0
        
            count_x = 0
            count_y = 0

            mass_coord = []
            coord = []
            for_file = []

            for i in data:
                for j in i:
                    if j == 0:
                        coord.append(count_x)
                        coord.append(count_y)
                        mass_coord.append(coord)
                    coord = []
                    count_x += 1
                count_x = 0
                count_y += 1 #Ставим + если ось ординат направленна вверх, - если вниз

            for i in data:
                for j in i:
                    if j == 0:
                        coord.append(count_x)
                        coord.append(count_y)
                        coord.append("b")
                        for_file.append(coord)
                    if j == 255:
                        coord.append(count_x)
                        coord.append(count_y)
                        coord.append("w")
                        for_file.append(coord)
                    coord = []
                    count_x += 1
                count_x = 0
                count_y -= 1 #Ставим + если ось ординат направленна вверх, - если вниз

            f = open(f"data_{name}.txt", "w")
            f.write(str(for_file))

            for h in mass_coord:
                self.canvas.create_rectangle(h[0], h[1], h[0]+1, h[1]+1, fill="black", outline="black")
            self.textn["text"] = "Complate!!!"
            self.textn.update()
        except FileNotFoundError:
            self.textn["text"] = "File not found"
            self.textn.update()

    def delete(self):
        self.canvas.delete("all")
        self.textn["text"] = ""
        self.textn.update()

root = Tk()
root.geometry("1000x500")
root.resizable(False, False)
MainRoot(root)
root.mainloop()
