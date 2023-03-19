from tkinter import *
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
raiz.geometry("660x530")
raiz.configure(background="gray40")


ttk.Label(raiz, text="Product Management ", font=("verdana", 30, "bold"), foreground="white", background="gray40").grid(column=0, row=0, sticky=(W), padx=90)

MainFrame = ttk.Frame(raiz, background="gray2")
MainFrame.grid(column=0, row=1, sticky=(W))
SecondFrame = ttk.Frame(MainFrame, background="#482525")
SecondFrame.grid(column=0, row=0, padx=35, pady=10)
ThirdFrame = ttk.Frame(SecondFrame, background="#482525")
ThirdFrame.grid(column=0, row=0, padx=35)
FourthFrame = ttk.Frame(SecondFrame, background="#482525")
FourthFrame.grid(column=0, row=1, pady=10, padx=5)


IdDato = IntVar()
NameDato = StringVar()
DescripcionDato = StringVar()
QuantityDato = IntVar()
PriceDato = float()
imageCompras = PhotoImage(file="Compras.png")
imagenCarrito = ttk.Label(raiz, background="gray40")
imagenCarrito.grid(column=0, row=0, sticky=(W))
imagenCarrito['image'] = imageCompras
imageLupa = PhotoImage(file="Lupa.png")
imageEscoba = PhotoImage(file="Limpiar.png")


IdEntry = ttk.Entry(ThirdFrame, background="#482525", textvariable=IdDato, width=24).grid(column=1, row=1, padx=5, pady=2, sticky=(W))
IdEntry = ttk.Entry(ThirdFrame, background="#482525", textvariable=NameDato, width=24).grid(column=1, row=2, padx=5,  pady=2, sticky=(W))
IdEntry = ttk.Entry(ThirdFrame, background="#482525", textvariable=DescripcionDato, width=24).grid(column=1, row=3, padx=5,  pady=2, sticky=(W))
IdEntry = ttk.Entry(ThirdFrame, background="#482525", textvariable=QuantityDato, width=24).grid(column=1, row=4, padx=5,  pady=2, sticky=(W))
IdEntry = ttk.Entry(ThirdFrame, background="#482525", textvariable=PriceDato, width=24).grid(column=1, row=5, padx=5,  pady=2, sticky=(W))

BotonLupa = ttk.Button(ThirdFrame,  background="#482525", activebackground="#482525")
BotonLupa.grid(column=2, row=0, padx=20, pady=10, sticky=(N, W))
BotonLupa['image'] = imageLupa
BotonEscoba = ttk.Button(ThirdFrame,  background="#482525", activebackground="#482525")
BotonEscoba.grid(column=2, row=0, padx=60, pady=10 ,sticky=(N, W))
BotonEscoba['image'] = imageEscoba
BotonSave = ttk.Button(ThirdFrame, background="Green4", text="Save",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=10, activebackground="darkgreen").grid(column=2, row=2, sticky=(N, W), padx=10, pady=2)
BotonDelete = ttk.Button(ThirdFrame, background="red", text="Delete",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=10 ,activebackground="red4").grid(column=2, row=3, sticky=(N, W), padx=10, pady=2)
BotonUpdate = ttk.Button(ThirdFrame, background="darkOrange", text="Update",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=10, activebackground="orange3").grid(column=2, row=5, sticky=(N, W), padx=10, pady=2)
BotonBack = ttk.Button(ThirdFrame, background="#482525", text="Back", foreground="SlateBlue",font=("verdana", 12, "bold"), anchor="center",  activebackground="#482525", activeforeground="SlateBlue").grid(column=2, row=0, sticky=(N, E), padx=100, pady=5)

ttk.Label(ThirdFrame, background="#482525", text="Id product: ", foreground="white", font=("arial", 12, "bold" )).grid(column=0, row=1, sticky=(W), padx=10, pady=2)
ttk.Label(ThirdFrame, background="#482525", text="Name: ", foreground="white", font=("arial", 12,"bold")).grid(column=0, row=2, sticky=(N, W), padx=10, pady=10)
ttk.Label(ThirdFrame, background="#482525", text="Description: ", foreground="white", font=("arial", 12,"bold" )).grid(column=0, row=3, sticky=(N, W), padx=10, pady=10)
ttk.Label(ThirdFrame, background="#482525", text="Quantity: ", foreground="white", font=("arial", 12 ,"bold")).grid(column=0, row=4, sticky=(N, W), padx=10, pady=10)
ttk.Label(ThirdFrame, background="#482525", text="Price: ", foreground="white", font=("arial", 12,"bold")).grid(column=0, row=5, sticky=(N, W), padx=10, pady=10)
ttk.Label(FourthFrame, text="idproduit", width=10, fg="gray30", bg="gray70").grid(row=0, column=0)
ttk.Label(FourthFrame, text="namep", width=20, fg="gray30",  bg="gray70").grid(row=0, column=1)
ttk.Label(FourthFrame, text="description", width=30, fg="gray30",  bg="gray70").grid(row=0, column=2)
ttk.Label(FourthFrame, text="quantity", width=10, fg="gray30",  bg="gray70").grid(row=0, column=3)
ttk.Label(FourthFrame, text="unite_price", width=10, fg="gray30", bg="gray70").grid(row=0, column=4)

data = [
    ("1", "Condia", "lait", "24", "100.0"),
    ("2", "la vache quirit", "fromage", "200", "300.0"),
    ("3", "bamoud boualam", "boisson gaseuse", "98", "90.0"),
    ("4", "Mina", "Chocolat","80","50.0"),
    ("5", "Aroma", "cafe","60","80.0"),
    ("6", "Facto", "Facto","7000","600.0")
]
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(FourthFrame, text=item, font=("system", 8), width=8 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j, sticky=(W))

raiz.mainloop()