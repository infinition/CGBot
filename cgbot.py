import os
import sys
from tkinter import *
from resources.CustomTkinter import customtkinter
import customtkinter
#or import customtkinter with pip rather than locally
from PIL import Image, ImageTk
#imports modules
from resources.zbrush import Zbrush
from resources.redirector import StdoutRedirector
from resources.createfolderstructure import CreateFolderStructure
from resources.blender import Blender
from resources.substancepainter import SubstancePainter
from resources.unreal import Unreal

PATH = os.path.dirname(os.path.realpath(__file__))

zbrush = Zbrush()
blender = Blender()
substancepainter = SubstancePainter()
unreal = Unreal()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(PATH + "\\resources\\assets\\themes\\dark-blue.json")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global txt
        self.geometry("800x750+400+100")
        self.resizable(False, False)
        self.title("CGbot")
        self.iconbitmap(PATH + "\\resources\\assets\\images\\cgbot.ico")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=200)

        self.frame_1 = customtkinter.CTkFrame(master=self, width=250, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)
        self.frame_2 = customtkinter.CTkFrame(master=self, width=150, height=240, corner_radius=15)
        self.frame_2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.frame_2.grid_columnconfigure(0, weight=1)
        self.frame_2.grid_columnconfigure(1, weight=1)

        self.add_app_logo_image = self.load_image( "\\resources\\assets\\images\\cgbot.png", 100)
        self.add_folder_image = self.load_image( "\\resources\\assets\\images\\add-folder.png", 20)
        self.eraser_image = self.load_image( "\\resources\\assets\\images\\eraser.png", 40)
        self.blender_image = self.load_image( "\\resources\\assets\\images\\blender.png", 100)
        self.zbrush_image = self.load_image( "\\resources\\assets\\images\\zbrush.png", 100)
        self.substancepainter_image = self.load_image( "\\resources\\assets\\images\\substancepainter.png", 100)
        self.unreal_image = self.load_image( "\\resources\\assets\\images\\unreal.png", 100)
 
        label = customtkinter.CTkLabel(master=self.frame_1,
                                    image=self.add_app_logo_image,
                                    width=140,
                                    height=25,
                                    fg_color=("white", "gray40"),
                                    corner_radius=8)
        label.grid(row=0, column=0, columnspan=3, padx=10, pady=(5,3), sticky="nsew")
        self.button_1 = customtkinter.CTkButton(master=self.frame_1, image=self.add_folder_image, text="Create Folders Structure in the current directory", height=32,
                                                compound="right", command=CreateFolderStructure, width=220)                                
        self.button_1.grid(row=1, column=0, columnspan=3,padx=10, pady=(30,0),  sticky="nsew")
        self.button_3 = customtkinter.CTkButton(master=self.frame_1, image=self.eraser_image, text="Clear terminal", width=40, height=40,
                                                corner_radius=10, fg_color="gray40", hover_color="gray25",
                                                command=self.clear_txt)
        self.button_3.grid(row=2, column=1, columnspan=1, padx=10, pady=10, sticky="w")
        self.button_6 = customtkinter.CTkButton(master=self.frame_2, image=self.zbrush_image, text="", width=130, height=30, border_width=2,
                                                corner_radius=10, border_color="gray25", fg_color=("gray84", "gray25"),
                                                hover_color="#f2c831", command=zbrush.main)
        self.button_6.grid(row=1, column=3, padx=20, pady=10, sticky="nsew")
        self.button_5 = customtkinter.CTkButton(master=self.frame_2, image=self.blender_image, text="", width=130, height=60, border_width=2,
                                                corner_radius=10, border_color="gray25", fg_color=("gray84", "gray25"),
                                                hover_color="#f2c831", command=blender.main)
        self.button_5.grid(row=2, column=3, padx=20, pady=10 , sticky="nsew")  
        self.button_7 = customtkinter.CTkButton(master=self.frame_2, image=self.substancepainter_image, text="", width=130, height=60, border_width=2,
                                                corner_radius=10, border_color="gray25", fg_color=("gray84", "gray25"),
                                                hover_color="#f2c831", command=substancepainter.main)
        self.button_7.grid(row=3, column=3, padx=20, pady=10 , sticky="nsew")
        self.button_8 = customtkinter.CTkButton(master=self.frame_2, image=self.unreal_image, text="", width=130, height=60, border_width=2,
                                                corner_radius=10, border_color="gray25", fg_color=("gray84", "gray25"),
                                                hover_color="#f2c831", command=unreal.main)
        self.button_8.grid(row=4, column=3, padx=20, pady=10 , sticky="nsew")  


        ##Terminal zone##
        txt = Text(master=self.frame_1, bg="grey25", fg="white", font="Roboto" , width=60, highlightbackground="grey25", highlightthickness=0, borderwidth=0, relief="ridge") 
        txt.grid(row=5, column=0, columnspan=3, padx=10, pady=10 , sticky="nsew") 
        
    def load_image(self, path, image_size):
        """ load rectangular image with path relative to PATH """
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
        
    def clear_txt(self):
        txt.delete(1.0, END)   
        

          
if __name__ == "__main__":
    app = App()
    sys.stdout = StdoutRedirector(txt) #redirect stdout to the text widget
    app.mainloop()







