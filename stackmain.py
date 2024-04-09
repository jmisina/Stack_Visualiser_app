def stackAppend(value):
    if (len(mainStack)<=25):                                        #Funkcja stackAppend(dodawana wartość)
        try:                                                        #służy do sprawdzenia zapełnienia stosu, poprawności zapisu
            mainStack.append(complex(value))                        #wartości, zamienieniu wartości na liczbę zespoloną, i ,po spełnieniu
            return "Dodano "+str(complex(value))+" do stosu"        #warunków, dodaniu liczby na górę stosu
        except ValueError:
            return "Niepoprawna wartość"
    return "Stos jest pełny"
            
        
def stackPop():                                                     #Funkcja stackPop()
    return mainStack.pop()                                          #zwraca ostatnią wartość dodaną na stos i usuwa ją ze stosu
    
def stackClear():                                                   #Funkcja stackClear()
    mainStack.clear()                                               #usuwa wszystkie wartości ze stosu

def stackSum():                                                     #Funkcja stackSum()
    return sum(mainStack)                                           #zwraca sumę wszystkich wartości stosu

def stackMultiply():                                                #Funkcja stackMultiply()
    prod = 1                                                        #zwraca iloczyn wszystkich wartości stosu
    for x in mainStack:
        prod*=x
    return prod

def stackSearch(value):                                                             #Funkcja stackSearch(szukana wartość)
    indexResult =[i for i, x in enumerate(mainStack) if x == complex(value)]        #służy do odszukania i zlokalizowania wartości na stosie
    return indexResult                                                              #zwraca tablicę indeksów, na których znajduje się szukana
                                                                                    #wartość
def searchFilter(value):                                                            #Funkcja searchFilter(szukana wartość)
    if len(stackSearch(value)) == 0:                                                #za pomocą funkcji stackSearch() sprawdza, czy szukana wartość
        return "Nie odnaleziono wartości na stosie"                                 #znajduje się na stosie, oraz zwraca stosowny komunikat
    else:
        return ("Wartość odnaleziona w polach o indeksach: "+str(stackSearch(value)))

def checkInput(value):                                                              #Funkcja checkInput(wprowadzona wartość)
    if value in ['(',')','j','+','-','', '\b','.'] or str.isdigit(value):           #służy do walidacji wartości wprowadzanej  
        return True                                                                 #przez użytkownika - ograniczeniu wprowadzania
    else:                                                                           #jedynie do dozwolonych symboli
        return False

mainStack = []                                                                      #zmienna mainStack przechowująca stos


