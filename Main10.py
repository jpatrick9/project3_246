from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Background(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="gray")
        
        self.parent = parent
        self.parent.title("Soundboard - CST205 Project 3")
        self.pack(fill=BOTH, expand=1)
        
        self.centerWindow()
        self.pictureBG()
        self.categories()
        #self.lines()
        self.buttonOne()

    def buttonOne(self):
        quitButton = Button(self, text="Quit",
            command=self.quit_pressed, bg="white", fg="red")
        quitButton.place(x=1500, y=750)

    def quit_pressed(self):
        self.master.destroy()        
        
    def centerWindow(self):
        w = 1600
        h = 900

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def pictureBG(self):
        # May need to use file path -> C:\\Users\\redle\\AppData\\Local\\Programs\\Python\\Python36-32\\
        bgImage = Image.open("Untitled-2.gif")
        bgImage = bgImage.resize((1600, 800), Image.ANTIALIAS)
        bgImage.save("bgGray.gif", "gif")
        self.photo = PhotoImage(file="bgGray.gif")
        self.Artwork = Label(self, image=self.photo)
        self.Artwork.photo = self.photo
        self.Artwork.grid(row=0, column=1)

    def categories(self):
        empty = Label(self, bg="black", font=('', 12), width=88)
        empty.place(x=3, y=3)
        stallForTime = Label(self, text="Stall for time", bg="black", fg="white", font=('', 12))
        stallForTime.place(x=3, y=3)
        pronouns = Label(self, text="Pronouns", bg="black", fg="white", font=('', 12))
        pronouns.place(x=150, y=3)
        verbs = Label(self, text="Verbs", bg="black", fg="white", font=('', 12))
        verbs.place(x=260, y=3)
        adjectives = Label(self, text="Adjectives", bg="black", fg="white", font=('', 12))
        adjectives.place(x=370, y=3)

    def lines(self):
        s = ttk.Separator(self, orient=VERTICAL).grid(sticky="ew")
        
def main():
    # Always start the program with root = Tk()
    root = Tk()

    # This is the class call for the window's properties
    ex = Background(root)
    
    ourNames = Label(root, text="Soundboard - by Jay, Joshua, and Bret", bg="black", fg="white")
    ourNames.pack(fill=BOTH)
    
    # Always end with root.mainloop()
    root.mainloop()

if __name__ == '__main__':
    main()
