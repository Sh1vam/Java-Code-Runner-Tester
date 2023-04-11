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

        Shivam.text_area = Text(Shivam, height=5, width=20, font=("",15))
        Shivam.text_area.grid()
        
        Shivam.button2 = ttk.Button(Shivam.labelFrame2, text = "Enter Cmd Args (if any)\n   [Before Running]",command = Shivam.Input)
        Shivam.button2.grid(column = 3, row = 4)

        Shivam.button2 = ttk.Button(Shivam.labelFrame2, text = "Compile",command = Shivam.compile)
        Shivam.button2.grid(column = 3, row = 2)

        Shivam.button2 = ttk.Button(Shivam.labelFrame2, text = "Run",command = Shivam.run)
        Shivam.button2.grid(column = 3, row = 3)

    def codefileDialog(Shivam):
        
        Shivam.filename = filedialog.askopenfilename( title = "Select A File", filetype =[("Java code files","*.java")])
        Shivam.label = ttk.Label(Shivam.labelFrame, text = "")

        Shivam.label.grid(column = 1, row = 3)
        Shivam.label.configure(text = Shivam.filename)

        global file
        file=Shivam.filename
        
    def compile(Shivam):
        
         try :
             print("\n")
             os.system(f'javac "{file}"')
             print("\n")
         except :
             print("\n")
         else :
             print("\n")
         finally:
             print("\n")
             
    def classfileDialog(Shivam):
         
         Shivam.filename = filedialog.askopenfilename( title = "Select A File", filetype =[("Java class files","*.class")])
         Shivam.label = ttk.Label(Shivam.labelFrame, text = "")

         Shivam.label.grid(column = 1, row = 3)
         Shivam.label.configure(text = Shivam.filename)
         
         filepath = Shivam.filename[:-6]
         
         global filename
         filename = filepath.split('/')[-1]

         global path
         path=filepath[:-(len(filename.split('/')[-1]))]

         
    def run(Shivam):
        
         #print(f'java -cp "{path}" {filename}')
         try :
             print("\n")
             os.system(f'java -cp "{path}" {filename} {Input}')
             print("\n")
         except :
             print("\n")
             os.system(f'java -cp "{path}" {filename}')
             print("\n")
         else :
             print("\n")
             
             print("\n")
         finally:
             print("\n")
         
    def Input(Shivam):
         global Input
         Input = Shivam.text_area.get("1.0", "end-1c")
 
root = Root()
root.mainloop()
