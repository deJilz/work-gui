import tkinter as tk
from tkinter.filedialog import askopenfilename
import webbrowser
"""
https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
http://www.python-gui-builder.com/


Connor
June 2022
"""

class MenuBar(tk.Menu):
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
        self.main_frame = tk.Frame(self, height=600, width=500)#bg="#EFF6F5", 
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

class MyApp(tk.Tk):
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

class PageHome(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        # title
        tk.Label(self.main_frame, font=("Verdana", 22,"bold"), text="Home Page").place(x=33,y=50)
        
        # text
        tk.Label(self.main_frame, font=("Verdana", 12), text=" > Press a button to use that tool.",justify="left").place(x=33,y=90)

        # pdf merger
        tk.Button(self.main_frame, text='merge PDFs', bg='#F0F8FF', font=('Verdana', 12, 'normal'), command=lambda: controller.frames[PageOne].tkraise()).place(x=33, y=150)
        
class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page One")
        label1.pack(side="top")
    
class PageTwo(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Two")
        label1.pack(side="top")
    
# class PageThree(GUI):
    # ''' PDF merger from a excel table method '''
    # def __init__(self, parent, controller):
        # GUI.__init__(self, parent)

        # label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="PDF Merger file")
        
        
        # #tk.Button(self.main_frame, text='act', bg='#F0F8FF', font=('arial', 12, 'normal'), command=lambda: merge_table_with_mp.Merger(self.prompt_file())).place(x=40, y=0)
        
        # label1.pack(side="top")
    # def prompt_file(self):
        # c_filename = askopenfilename(title='select tag file', filetypes=[
                    # ("all excel formats", ".xls"),
                    # ("all excel formats", ".xlsx"),
                    # ("all excel formats", ".xlsm")]) # show an "Open" dialog box and return the path to the selected file
        # if c_filename == '':
            # quit() #user hit cancel
        
        
class READ_ME(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        
        # title
        label1 = tk.Label(self.main_frame, font=("Verdana", 22,"bold"), text="READ ME PAGE").place(x=33,y=100)
        
        # text
        label2 = tk.Label(self.main_frame, font=("Verdana", 12), text="This tool is a way to use some useful scripts.\nIt can also serve as a nice template for future use.\n\nCheck the >help>git repo for the code",justify="left").place(x=33,y=200)
        
if __name__ == "__main__":
    root = MyApp()
    root.title("Smart Plant Instrumentation GUI")
    root.geometry("600x500")#("400x300+10+10")#height=600, width=1024
    root.iconphoto(False,tk.PhotoImage(file = "images\\ap_logo.png"))
    root.mainloop()