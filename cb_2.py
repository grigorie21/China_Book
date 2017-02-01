import shelve
from tkinter import *
import collections
import random

class Application(Frame):
    '''GUI application ере displays menu for the programm'''
    def __init__(self, master):
        '''Initialize Frame'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        ''' Create widgets to get story information and to display story. '''

        self.score=[]
        
        # 1 number button
        Button(self,
               text = "number #1",
               command = self.record
               ).grid(row = 1, column = 1, sticky = W)
        
        # 1 number button
        Button(self,
               text = "number #2",
               command = self.record
               ).grid(row = 2, column = 1, sticky = W)
        
        # 1 number button
        Button(self,
               text = "number #3",
               command = self.record
               ).grid(row = 3, column = 1, sticky = W)
        
        # 1 number button
        Button(self,
               text = "number #4",
               command = self.record
               ).grid(row = 4, column = 1, sticky = W)
        
        # 1 number button
        Button(self,
               text = "number #5",
               command = self.record
               ).grid(row = 5, column = 1, sticky = W)
        
        # 1 number button
        Button(self,
               text = "number #6",
               command = self.record
               ).grid(row = 6, column = 1, sticky = W)
        
        # show training button
        Button(self,
               text = "show result",
               command = self.tngDisplay
               ).grid(row = 8, column = 2, sticky = W)

        self.tngField = Text(self, width = 30, height = 3, wrap = WORD)
        self.tngField.grid(row = 11, column = 0, columnspan = 4)

    def rand(self):
        i=random.randint(0,1)
        return i
    
    def record(self):
        self.score.append(self.rand())
        
    def tngDisplay (self):
                
        self.tngField.delete(0.0, END)
        self.tngField.insert('end', self.score)
        


root = Tk()
root.title('ChinaBook')
app = Application(root)
root.mainloop()
