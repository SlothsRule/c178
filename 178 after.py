from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()

root.geometry("800x500")
root.title("Encapsulation")

class Color:
    def __init__(self, fruit_name, quantity):
        self.color = color_name
        self.quantity = int(quantity)
        
    def __calculateColor(self):
        random_color = self.quantity * self.__color
        print("You have to pay :"+str(total_cost)+" GBS")
        if(self.color == "Pink"):
        elif(self.color == "Red"):
        elif(self.color == "Blue"):
        print("x"+str(self.quantity)+" = "+str(calorie)+" calories")
        
    def getColor(self):
        self.__calculateCost()
def chooseColor():
    fruit = "Pink"
    quantity= 2000
    obj1 = Juice(fruit,quantity)
    obj1.getCost()

btn_it = Button(root, text="TOTAL", command=orderJuice)
btn_it.place(relx=0.95, rely=0.5,anchor=E)

            
root.mainloop()