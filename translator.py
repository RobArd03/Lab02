from dictionary import Dictionary as di

class Translator:

    def __init__(self):
        self.d = di()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print(f"{"-"*35}\n{"Translator Alien-Italian"}\n{"-"*35}\n"
              f"1. Aggiungi nuova parola\n"
              f"2. Cerca una traduzione\n"
              f"3. Cerca con wildcard\n"
              f"4. Exit\n"
              f"{"-"*35}")

    def loadDictionary(self, dict: str):
        # dict is a string with the filename of the dictionary
        with open(dict, 'r') as f:
            lines = f.readlines()
        for line in lines:
            result = line.strip().split(" ")
            self.d.addWord(result)


    def handleAdd(self, entry: str):
        # entry is a tuple <parola_aliena>
        mystr = entry.strip().split(" ")
        if len(mystr) <= 1:
            print("Inserisci le parole nel formato corretto")
        for i in mystr:
            b = True
            if i.isalpha() is False:
                b = False
                print("Inserire solo parole")
        if len(mystr) > 1 and b:
            self.d.addWord(mystr)

    def handleTranslate(self, query: str):
        # query is a string <parola_aliena>
        value = self.d.translate(query)
        if value is None:
            print("Parola non trovata")
        else:
            mystr = ""
            for i in value:
                mystr += i + " "
            print(f"La traduzione è: {mystr}")

    def handleWildCard(self,query: str):
        # query is a string with a ? --> <par?la_aliena>
        i = 0
        for carattere in query.strip():
            if carattere == "?":
                i += 1
        if i==1:
            return self.d.translateWordWildCard(query)
        else:
            print("Inserire solo un carattere '?'")

