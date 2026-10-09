class Cliente:

    def __init__(self, nome, campagne=None):
        self.nome = nome
        if campagne is None:
            self.campagne = [] # vogliamo passare una lista vuota in caso di nessuna campagna
        else:
            self.campagne = campagne

    def __str__(self):
        """Serve per formattare il valore ritornato quando viene richiamato l'oggetto come stringa"""
        return f"Cliente: {self.nome} ({len(self.campagne)} campagne)"
