class Dictionary:

    def __init__(self):
        self.dizionario = {}

    def addWord(self, traduzioni):
        if self.dizionario.get(traduzioni[0]) == None:
            self.dizionario = {traduzioni[0]: traduzioni[1:]}
        else:
            unione_senza_doppioni = list(set( self.dizionario.get(traduzioni[0]) + traduzioni[1:]))
            self.dizionario[traduzioni[0]] = unione_senza_doppioni

    def translate(self, query):
        return self.dizionario.get(query)

    def translateWordWildCard(self):
        pass