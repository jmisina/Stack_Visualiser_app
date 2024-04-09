from tkinter import CENTER, font, scrolledtext, ttk
from turtle import color, width
from tkinter.scrolledtext import ScrolledText
import stackmain
import tkinter as tk
from tkinter import *; ttk
  
def buildStack():                                                           #Funkcja buildStack() służy do wyświetlania     
    for x in range(0, 26):                                                  #stosu na ekranie
        label = tk.Label(stackShow, text=x)                                      
        cell = Canvas(stackShow, height=20, width=60,bg="white")    
        cell.create_rectangle(2,2,60,20,outline="black", fill="white")
        label.grid(column=0, row=25-x)
        cell.grid(column=1, row=25-x)
        if (x)<=len(stackmain.mainStack)-1:
            stackValue = complex(stackmain.mainStack[x])
            cell.create_text(30, 10, text=stackValue, fill="black")
    stackShow.pack(side=LEFT, anchor=N)

def showInfo(message):                                                     #Funkcja showInfo(wiadomość)
    infoWindow['state']='normal'                                           #służy do wyświetlania wiadomości w oknie 
    infoWindow.insert(END, str(message)+"\n")                              
    infoWindow['state']='disabled'

def delete():                                                              #Funkcja delete()
    entryWindow.config(validate="none")                                    #usuwa zawartość pola wprowadzania
    entryWindow.delete(0, END)
    entryWindow.config(validate="key")
    
def insert():
    entryWindow.config(validate="none")                                     #Funkcja insert()
    entryWindow.insert(0, stackmain.stackPop())                             #wprowadza wartość zdjętą ze stosu
    entryWindow.config(validate="key")                                      #do pola wprowadzania


    
window = tk.Tk()                                                            #window jest głównym oknem programu
window.geometry("600x650+500+50")
window.resizable(False,False)
window.title("Wizualizacja stosu - liczby zespolone")


stackShow = ttk.Frame(window, padding=10, relief="solid")                   #stackShow jest ramką, w której umieszczony jest stos
stackShow.pack(side=LEFT, anchor=N, fill="y")

userMenu = ttk.Frame(window,padding=(110,10), relief="solid")               #userMenu jest ramką, w której umieszczone
userMenu.pack(side=TOP, anchor=CENTER)                                      #są opcje użytkownika

infoFrame = ttk.Frame(window, padding=10, relief="sunken")                  #infoFrame jest ramką, w której znajduje się
infoFrame.pack(side=TOP, anchor=W, fill="y")                                #infoWindow, pole z informacją zwrotną dla użytkownika 
infoWindow = ScrolledText(infoFrame, width=500, state='disabled')
infoWindow.pack()

stackShow.pack(side=LEFT, anchor=N)                                         #wstępne wczytanie stosu
buildStack()

check_num_wrapper = (window.register(stackmain.checkInput), '%S')           #metoda .register z pomocą funkcji stackmain.checkInput
                                                                            #zwraca napis pozwalający na walidację wprowadzanych wartości 
entryWindow = Entry(userMenu, width=10, justify=CENTER, bd=3,\
    font='Arial 18', takefocus=1, validate='all', validatecommand=check_num_wrapper)#entryWindow jest polem do wprowadzania danych na stos
entryWindow.grid(column=0, row=0, columnspan=3,pady=(20,0))
entryWindow.focus_set()
infoLabel = tk.Label(userMenu, text="Poprawny format: (a±bj)", pady=10)     
infoLabel.grid(column=0, row=1, columnspan=3)


#przycisk appendButton dodaje wartość z pola wprowadzania na stos
appendButton = ttk.Button(userMenu, text="Dodaj na stos",\
    command=lambda:[showInfo(stackmain.stackAppend(entryWindow.get())),buildStack(), delete()])
#przycisk popButton zdejmuje wartość ze stosu i zwraca ją do pola wprowadzania
popButton = ttk.Button(userMenu,text="Zdejmij ze stosu", \
    command=lambda:[delete(), insert(), showInfo('Zdjęto '+entryWindow.get()+' ze stosu'), buildStack()])
#przycisk clearButton usuwa wszystkie wartości stosu i wyświetla go 
clearButton = ttk.Button(userMenu,text="Wyczyść stos", \
    command=lambda:[stackmain.stackClear(),showInfo("Usunięto wszystkie wartości na stosie"), buildStack(), delete()])
#przycisk sumButton sumuje wartości na stosie i wyprowadza komunikat z otrzymaną wartością
sumButton = ttk.Button(userMenu,text="Sumuj wartości stosu", \
    command=lambda:[showInfo("Suma wszystkich wartości stosu: "+str(stackmain.stackSum()))])
#przycisk multiplyButton mnoży wartości na stosie i wyprowadza komunikat z otrzymaną wartością
multiplyButton = ttk.Button(userMenu,text="Pomnóż wartości stosu", \
    command=lambda:[showInfo("Iloczyn wszystkich wartości stosu: "+str(stackmain.stackMultiply()))])
#przycisk searchButton wyszukuje wprowadzoną przez użytkownika wartość i wyświetla indeksy na których się znajduje
searchButton = ttk.Button(userMenu,text="Odszukaj wartość na stosie", \
    command=lambda:[showInfo(stackmain.searchFilter(entryWindow.get()))])

#rozmieszczenie przycisków w menu użytkownika
appendButton.grid(column=1, row=3,ipady=10, ipadx=35)
sumButton.grid(column=1, row=4,ipady=10, ipadx=15)
popButton.grid(column=2,row=3,ipady=10, ipadx=31)
multiplyButton.grid(column=2, row=4,ipady=10, ipadx= 12)
searchButton.grid(column=1, row=5,ipady=10)
clearButton.grid(column=2, row=5,ipady=10, ipadx = 39)

window.mainloop()
