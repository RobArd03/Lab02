import translator as tr
def main():
    t = tr.Translator()

    # apertura e salvataggio del file e i suoi dati
    t.loadDictionary("dictionary.txt")

    while True:

        # print Menu
        t.printMenu()

        # input del metodo selezionato
        txtIn = input("Inserisci un numero tra 1 e 4: ")
        if txtIn.isdigit():
            while int(txtIn) > 4 or int(txtIn) == 0:
                print("Il numero selezionato è errato.")
                txtIn = input("Inserisci un numero tra 1 e 4: ")

         # Add input control here!

        # aggiunta voce nel dizionario
        if int(txtIn) == 1:
            print(f"{"-"*35}")
            txtIn = input("Inserisci le parole da aggiungere nel dizionario separate da uno spazio (<parola_aliena> <traduzione1 traduzione2 ...>): ")
            t.handleAdd(txtIn)


        # aggiunta
        elif int(txtIn) == 2:
            print(f"{"-" * 35}")
            txtIn = input("Inserisci la parola aliena da tradurre: ")
            t.handleTranslate(txtIn)


        elif int(txtIn) == 3:
            pass

        # break
        elif int(txtIn) == 4:
            break

        else:
            print("Inserisci un numero tra 1 e 4.")
main()