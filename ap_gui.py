import tkinter as tk
from tkinter.filedialog import askopenfilename
import webbrowser
import os
"""
https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
http://www.python-gui-builder.com/

Connor
June 2022

"""

class MenuBar(tk.Menu): # menu bar across top of MyApp
    # some examples from the template
    # ***** from template
        # menu_operations = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu4", menu=menu_operations)
        # menu_operations.add_command(label="Page Two", command=lambda: parent.show_frame(PageTwo))
        # menu_positions = tk.Menu(menu_operations, tearoff=0)
        # menu_operations.add_cascade(label="Menu5", menu=menu_positions)
        # menu_positions.add_command(label="Page Three", command=lambda: parent.show_frame(PageThree))
        # menu_positions.add_command(label="Page Four", command=lambda: parent.show_frame(PageFour))

        # menu_help = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu6", menu=menu_help)
        # menu_help.add_command(label="Open New Window", command=lambda: parent.OpenNewWindow())

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        
        # file menu
        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=menu_file)
        
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application", command=lambda: parent.Quit_application())
        
        # actions menu
        menu_actions = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Actions", menu=menu_actions)
        menu_actions.add_command(label="act1", command=lambda: print("not implemented"))
        #menu_actions.add_command(label="Open Spec", command=lambda:print("not implemented"))
        #menu_actions.add_command(label="Create Sepc", command=lambda:print("not implemented"))
        
        # views menu
        menu_views = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Views", menu=menu_views)
        menu_views.add_command(label="Home Page", command=lambda: parent.show_frame(PageHome))
        menu_views.add_command(label="Page One", command=lambda: parent.show_frame(PageOne))
        #menu_views.add_command(label="Page Two", command=lambda: parent.show_frame(PageTwo))
        #menu_views.add_command(label="PDF Merger", command=lambda: parent.show_frame(PageThree))
        
        # help menu
        menu_help = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=menu_help)
        menu_help.add_command(label="Read me", command=lambda: parent.show_frame(READ_ME))
        menu_help.add_command(label="Git repo", command=lambda: webbrowser.open("https://github.com/deJilz/work-gui"))

class GUI(tk.Frame): # very abstracted frame class
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, height=600, width=900)#bg="#EFF6F5", 
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # maybe add hidden progress bar
        
        self.main_frame.grid_columnconfigure(0, weight=1)

class MyApp(tk.Tk): # tk window app
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, height=600, width=500) #bg="#84CEEB", 
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.resizable(0, 0) #prevents the app from being resized
        # self.geometry("1024x600") fixes the applications size
        self.frames = {}
        pages = (PageHome, PageOne, PageTwo, READ_ME)#(Some_Widgets, PageOne, PageTwo, PageThree, PageFour)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(PageHome)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def OpenNewWindow(self):
        OpenNewWindow()

    def Quit_application(self):
        self.destroy()

class PageHome(GUI): # home page to link out to apps
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        # title
        tk.Label(self.main_frame, font=("Verdana", 22,"bold"), text="Home Page").place(x=33,y=50)
        
        # text
        tk.Label(self.main_frame, font=("Verdana", 12), text=" > Press a button to use that tool.",justify="left").place(x=33,y=90)

        # pdf merger
        tk.Button(self.main_frame, text='merge PDFs', bg='#F0F8FF', font=('Verdana', 12, 'normal'), command=lambda: controller.frames[PageOne].tkraise()).place(x=33, y=150)
  
class PageOne(GUI): # merge pdfs based on excel table
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        
        # declaring string variable
        excel_var=tk.StringVar()
        row_var=tk.StringVar()
        doc_fold_var=tk.StringVar()
        place_fold_var=tk.StringVar()
        
        # defaults
        doc_fold_var = os.getcwdb()
        place_fold_var = os.getcwdb()
        
        # title
        tk.Label(self.main_frame, font=("Verdana", 22,"bold"), text="Merge PDFs").place(x=33,y=50)
        
        
        # select what excel doc
        tk.Label(self.main_frame, font=("Verdana", 12,"normal"), text="Select the excel mapping doc: ").place(x=33,y=100)
        tk.Entry(self.main_frame,textvariable = excel_var).place(x=60,y=100) # entry
        tk.Button(self.main_frame, text='start splitting', bg='#F0F8FF', font=('Verdana', 12, 'normal'), command=lambda: print("nothing")).place(x=90, y=100) # button
        
        
        # what row to start on
        tk.Label(self.main_frame, font=("Verdana", 12,"normal"), text="What row do filenames start: ").place(x=33,y=130)
        tk.Entry(self.main_frame,textvariable = row_var).place(x=60,y=130) # entry
        
        
        # select where docs are - folder select
        tk.Label(self.main_frame, font=("Verdana", 12,"normal"), text="Where are the PDFs: ").place(x=33,y=160)
        tk.Label(self.main_frame, font=("Verdana", 6,"normal"), text=doc_fold_var).place(x=33,y=130)# label - default current
        tk.Button(self.main_frame, text='change folder', bg='#F0F8FF', font=('Verdana', 12, 'normal'), command=lambda: self.select_file()).place(x=90, y=100) # button
        
        
        # select where to put them or use where docs are
        tk.Label(self.main_frame, font=("Verdana", 12,"normal"), text="where to put the merges: ").place(x=33,y=190)
        tk.Label(self.main_frame, font=("Verdana", 12,"normal"), text=place_fold_var).place(x=33,y=130)# label - default current
        tk.Button(self.main_frame, text='change folder', bg='#F0F8FF', font=('Verdana', 12, 'normal'), command=lambda: self.select_file()).place(x=90, y=100) # button
        
        
        # button to start - this is where the import can come in
        tk.Button(self.main_frame, text='start splitting', bg='#F0F8FF', font=('Verdana', 12, 'normal'), command=lambda: print("nothing")).place(x=33, y=200)
        
        # progress bar
        
        pass # extend collapse
        
    def getInputBoxValue(self,box):
        userInput = box.get()
        return userInput
        
    def select_file(self):
        print("nope")
        pass
        
    def select_folder(self):
        print("nope")
        pass
  
class PageTwo(GUI): # split selected pdf based on excel table
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        
        # title
        tk.Label(self.main_frame, font=("Verdana", 22,"bold"), text="Split PDFs").place(x=33,y=100)
        
        # what pdf to split
        # mapping excel doc or suffix to start at ex PG0 or pg1 or PG01
        # button to go
        tk.Button(self.main_frame, text='start splitting', bg='#F0F8FF', font=('Verdana', 12, 'normal'), command=lambda: print("nothing")).place(x=33, y=150)
        # progress bar
        
        pass # extend collapse
    
class READ_ME(GUI): # little descriptor of project
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        
        # title
        label1 = tk.Label(self.main_frame, font=("Verdana", 22,"bold"), text="READ ME PAGE").place(x=33,y=100)
        
        # text
        label2 = tk.Label(self.main_frame, font=("Verdana", 12), text="This tool is a way to use some useful scripts.\nIt can also serve as a nice template for future use.\n\nCheck the >help>git repo for the code",justify="left").place(x=33,y=200)
   
if __name__ == "__main__": # startup script
    root = MyApp()
    root.title("AP GUI")
    root.geometry("600x500")#("400x300+10+10")#height=600, width=1024
    root.iconphoto(False,tk.PhotoImage(file = "images\\ap_logo.png"))
    root.mainloop()