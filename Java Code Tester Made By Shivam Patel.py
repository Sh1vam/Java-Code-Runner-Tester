import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Root(Tk):
    
    def __init__(Shivam):
        
        super(Root, Shivam).__init__()
        
        Shivam.title("Java Code Runner Made By Shivam Patel")
        Shivam.minsize(5, 5)
 
        Shivam.labelFrame = ttk.LabelFrame(Shivam, text = "Open Java Files")
        Shivam.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        Shivam.labelFrame2=ttk.LabelFrame(Shivam, text = "OK")
        Shivam.labelFrame2.grid(column = 2, row = 1, padx = 20, pady = 20)
        
        Shivam.button()
 
    def button(Shivam):
        
        Shivam.button = ttk.Button(Shivam.labelFrame, text = "Browse A Java Code File",command = Shivam.codefileDialog)
        Shivam.button.grid(column = 1, row = 1)

        Shivam.button = ttk.Button(Shivam.labelFrame, text = "Browse A Java Class File\n [Must contain main()]",command = Shivam.classfileDialog)
        Shivam.button.grid(column = 1, row = 2)
        
        Shivam.button2 = ttk.Button(Shivam.labelFrame2, text = "Done",command = Shivam.destroy)
        Shivam.button2.grid(column = 3, row = 1)

    def codefileDialog(Shivam):
        
        Shivam.filename = filedialog.askopenfilename( title = "Select A File", filetype =[("Java code files","*.java")])
        Shivam.label = ttk.Label(Shivam.labelFrame, text = "")

        Shivam.label.grid(column = 1, row = 3)
        Shivam.label.configure(text = Shivam.filename)

        os.system(f'javac "{Shivam.filename}"')

    def classfileDialog(Shivam):
         
         Shivam.filename = filedialog.askopenfilename( title = "Select A File", filetype =[("Java class files","*.class")])
         Shivam.label = ttk.Label(Shivam.labelFrame, text = "")

         Shivam.label.grid(column = 1, row = 3)
         Shivam.label.configure(text = Shivam.filename)
         
         filepath = Shivam.filename[:-6]
         filename = filepath.split('/')[-1]
         os.system(f'java "{filename}"')
 
root = Root()
root.mainloop()
