from tkinter import *
from settings import Settings
from PIL import Image as PilImage
from PIL import ImageTk
import tkinter


class Interface:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.withdraw()
        self.window = Toplevel(self.root)
        self.window.title(Settings.TITLE)
        self.window.configure(bg=Settings.ICON_COLOUR)
        self.window.iconbitmap(Settings.ICON)
        self.window.resizable(False, False)
        self.window.geometry(f"{Settings.ICON_WIDTH}x{Settings.ICON_HEIGHT}")

        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth() * 2) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight() * 2) / 2
        self.window.wm_geometry("+%d+%d" % (x, y))

        img = PilImage.open(Settings.BUTTON_BG)
        img = img.resize((Settings.BUTTON_WIDTH, Settings.BUTTON_HEIGHT), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

    def create_button_img(self, function, text_button="button", height_gm=0):
        button = Button(self.window,
                        text=text_button,
                        font=("Courier", 13),
                        image=self.photo_image,
                        compound=CENTER,
                        bd=0,
                        pady=5,
                        command=function)

        button.pack()
        button.place(x=Settings.BUTTON_WIDTH_GM, y=Settings.BUTTON_HEIGHT_GM + height_gm)

    def create_button(self, function, text_button="button", height_gm=0):
        button = Button(self.window,
                        width=17,
                        height=1,
                        text=text_button,
                        font=("Courier", 13),
                        compound=CENTER,
                        bd=0,
                        pady=5,
                        command=function,
                        bg=Settings.BUTTON_COLOUR,
                        activebackground=Settings.BUTTON_COLOUR_ACTIVE)

        button.pack()
        button.place(x=Settings.BUTTON_WIDTH_GM, y=Settings.BUTTON_HEIGHT_GM + height_gm)

    def create_label(self, text_label="label", height_gm=0):
        label = Label(self.window,
                      text=text_label,
                      font=("Courier", 36, "bold"),
                      pady=50,
                      bg=Settings.ICON_COLOUR)
        label.pack()

    def destroy_window(self):
        self.window.destroy()

    def run(self):
        self.window.mainloop()
