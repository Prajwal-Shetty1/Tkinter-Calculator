from tkinter import Tk,Entry,Button,StringVar

class calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry('370x480+0+0')
        master.config(bg='Black')
        master.resizable(False,False)

        self.equation=StringVar()
        self.entry_value=''
        Entry(master, width=25, bg='white', font=('Arial Bold', 20), textvariable=self.equation).grid(row=0, column=0, columnspan=4, pady=5)




        Button(width=11, height=4, text='(', bg='white', command=lambda: self.show('(')).grid(row=1 ,column=0)
        Button(width=11, height=4, text=')', bg='white', command=lambda: self.show(')')).grid(row=1, column=1)  
        Button(width=11, height=4, text='%', bg='white', command=lambda: self.show('%')).grid(row=1 ,column=2)  
        Button(width=11, height=4, text='1', bg='white', command=lambda: self.show('1')).grid(row=4, column=0)  
        Button(width=11, height=4, text='2', bg='white', command=lambda: self.show('2')).grid(row=4 , column=1)  
        Button(width=11, height=4, text='3', bg='white', command=lambda: self.show('3')).grid(row=4 , column=2)  
        Button(width=11, height=4, text='4', bg='white', command=lambda: self.show('4')).grid(row=3 , column=0)  
        Button(width=11, height=4, text='5', bg='white', command=lambda: self.show('5')).grid(row=3 , column=1)  
        Button(width=11, height=4, text='6', bg='white', command=lambda: self.show('6')).grid(row=3 , column=2)  
        Button(width=11, height=4, text='7', bg='white', command=lambda: self.show('7')).grid(row=2 , column=0)  
        Button(width=11, height=4, text='8', bg='white', command=lambda: self.show('8')).grid(row=2 , column=1)  
        Button(width=11, height=4, text='9', bg='white', command=lambda: self.show('9')).grid(row=2, column=2)  
        Button(width=11, height=4, text='0', bg='white', command=lambda: self.show('0')).grid(row=5 , column=1)  
        Button(width=11, height=4, text='.', bg='white', command=lambda: self.show('.')).grid(row=5 , column=2)  
        Button(width=11, height=4, text='+', bg='white', command=lambda: self.show('+')).grid(row=4 , column=3)  
        Button(width=11, height=4, text='-', bg='white', command=lambda: self.show('-')).grid(row=3 , column=3)  
        Button(width=11, height=4, text='/', bg='white', command=lambda: self.show('/')).grid(row=1, column=3)  
        Button(width=11, height=4, text='x', bg='white', command=lambda: self.show('*')).grid(row=2, column=3)  
        Button(width=11, height=4, text='=', bg='white', command=self.solve).grid(row=5, column=3)
        Button(width=11, height=4, text='C', bg='white', command=self.clear).grid(row=5 , column=0)  


 
        
    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)
        

    
        
        
        

root=Tk()

calculator=calculator(root)
root.mainloop()
