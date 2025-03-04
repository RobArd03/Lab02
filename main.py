import translator as tr
def main():
    t = tr.Translator()

    while True:

        # print Menu
        t.printMenu()

        # apertura e salvataggio del file e i suoi dati
        t.loadDictionary("dictionary.txt")

        # input del metodo selezionato
        txtIn = input("Inserisci un numero tra 1 e 4: ")
        if txtIn.isdigit():
            while int(txtIn) > 4 or int(txtIn) == 0:
                print("Il numero selezionato è errato.")
                txtIn = input("Inserisci un numero tra 1 e 4: ")

         # Add input control here!

        if int(txtIn) == 1:
            print(f"{"-"*35}")
            txtIn = input("Inserisci la parola da tradurre separate da uno spazio (Aliena Italiano): ")
            t.handleAdd(txtIn)



        elif int(txtIn) == 2:
            pass


        elif int(txtIn) == 3:
            pass

        # break
        elif int(txtIn) == 4:
            break
main()