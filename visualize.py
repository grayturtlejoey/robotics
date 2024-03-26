import tkinter as tk
import random

class BlinkingEyes:
    def __init__(self, master, width=650, height=400):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(master, width=width, height=height)
        self.canvas.pack()

        self.eye1 = self.canvas.create_oval(50, 50, 300, 300, fill="white")
        self.eye2 = self.canvas.create_oval(350, 50, 600, 300, fill="white")
        self.pupil1 = self.canvas.create_oval(100, 100, 250, 250, fill="black")
        self.pupil2 = self.canvas.create_oval(400, 100, 550, 250, fill="black")
        self.master.update_idletasks()


    def neutralEyes(self):
        self.canvas.moveto(self.pupil1, 100,100)
        self.canvas.moveto(self.pupil2, 400,100)
        self.master.update_idletasks()
        
    def leftEyes(self):
        self.canvas.moveto(self.pupil1, 60,100)
        self.canvas.moveto(self.pupil2, 360,100)
        self.master.update_idletasks()
        
    def rightEyes(self):
        self.canvas.moveto(self.pupil1, 140,100)
        self.canvas.moveto(self.pupil2, 440,100)
        self.master.update_idletasks()
    
    def downEyes(self):
        self.canvas.moveto(self.pupil1, 100,140)
        self.canvas.moveto(self.pupil2, 400,140)
        self.master.update_idletasks()
        
    def upEyes(self):
        self.canvas.moveto(self.pupil1, 100,60)
        self.canvas.moveto(self.pupil2, 400,60)
        self.master.update_idletasks()
        

def main():
    root = tk.Tk()
    root.title("Visualize")

    app = BlinkingEyes(root)

    while True:
        root.update_idletasks()
        root.update()
        app.upEyes()

if __name__ == "__main__":
    main()