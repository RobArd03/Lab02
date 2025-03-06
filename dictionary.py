class Dictionary:

    def __init__(self):
        self.dizionario = {}

    def addWord(self, traduzioni: list):
        if self.dizionario.get(traduzioni[0]) is None:
            self.dizionario[traduzioni[0]] = traduzioni[1:]
        else:
            unione_senza_doppioni = list(set( self.dizionario.get(traduzioni[0]) + traduzioni[1:]))
            self.dizionario[traduzioni[0]] = unione_senza_doppioni

    def translate(self, query):
        return self.dizionario.get(query)

    def translateWordWildCard(self, query: str):
        i = query.find("?")
        s = ""
        for key in self.dizionario.keys():
            if key[:i] == query.split("?")[0] and key[i+1:] == query.split("?")[1]:
                s+="\n"
                for mystr in self.dizionario[key]:
                    s += " " + mystr
        return s





if __name__ == "__main__":
    d = Dictionary()
    with open("dictionary.txt", 'r') as f:
        lines = f.readlines()
    for line in lines:
        result = line.strip().split(" ")
        d.addWord(result)
    d.translateWordWildCard("kis?a")