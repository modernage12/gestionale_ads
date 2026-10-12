class Cliente:

    def __init__(self, nome, campagne=None):
        self.nome = nome
        if campagne is None:
            self.campagne = []  # vogliamo passare una lista vuota in caso di nessuna campagna
        else:
            self.campagne = campagne

    def __str__(self):
        """Serve per formattare il valore ritornato quando viene richiamato l'oggetto come stringa"""
        return f"Cliente: {self.nome} ({len(self.campagne)} campagne)"

    def aggiungi_campagna(self, campagna):
        self.campagne.append(campagna)


class Campagna:

    def __init__(self, nome, budget, tipo, metriche=None):
        self.nome = nome
        self.budget = budget
        self.tipo = tipo
        if metriche is None:
            self.metriche = []
        else:
            self.metriche = metriche

    def aggiungi_metrica(self, metrica):
        """Aggiunge una nuova metrica allE liste di metriche della campagna"""
        self.metriche.append(metrica)

    def calcola_spesa_totale(self):
        """Calcola la spesa totale dalle metriche della campagna e ne ritorna quindi la somma"""
        spesa_totale = 0

        for metrica in self.metriche:
            spesa_totale += metrica.spesa

        return spesa_totale

    def calcola_cpa_totale(self):
        """Calcola il cpa totale dalle metriche della campagna e ne ritorna il valore"""
        conversioni_totali = 0

        for metrica in self.metriche:
            conversioni_totali += metrica.conversioni

        if conversioni_totali > 0:
            return self.calcola_spesa_totale() / conversioni_totali
        else:
            return None  # Deciso che con 0 conversioni/metriche ritorna None

    def calcola_roas_totale(self):
        """Calcola il ROAS totale dalle metriche della campagna e ne ritorna il valore"""
        ricavi_totali = 0

        for metrica in self.metriche:
            if metrica.ricavi is not None:
                ricavi_totali += metrica.ricavi
            else:
                ricavi_totali = None  # Voglio che se anche solo un giorno ha ricavi = None, il resto non sia valido
                break

        if ricavi_totali is not None and self.calcola_spesa_totale() > 0:
            return ricavi_totali / self.calcola_spesa_totale()
        else:
            return None

    def calcola_cpl_totale(self):
        """Calcola il CPL totale dalle metriche della campagna e ne ritorna il valore"""
        lead_totali = 0
        spesa_totale = self.calcola_spesa_totale()

        for metrica in self.metriche:
            if metrica.lead is not None:
                lead_totali += metrica.lead
            else:
                lead_totali = None
                break

        if lead_totali is not None and lead_totali > 0:
            if spesa_totale > 0:
                return spesa_totale / lead_totali
            else:
                return spesa_totale  # Se spesa = 0 ma ci sono lead, il CPL sarà considerato 0 quindi come costo
        else:
            return None


class MetricaGiornaliera:

    def __init__(self, data, spesa, conversioni, ricavi=None, lead=None):
        self.data = data
        self.spesa = spesa
        self.conversioni = conversioni
        self.ricavi = ricavi  # se la campagna è di lead generation i ricavi non vengono li otteniamo
        self.lead = lead  # lead=None in caso di campagne non di lead generation

    def calcola_cpa(self):
        """Calcolca il costo per acquisizione e lo ritorna. In caso di zero conversioni, ritorna none"""
        try:
            return self.spesa / self.conversioni
        except ZeroDivisionError:
            return None  # Ritornando None, possiamo gestirlo meglio successivamente

    def calcola_roas(self):
        """Calcola il ROAS e lo ritorna. In caso di zero spesa, ritorna None"""
        if self.ricavi is not None:
            try:
                return self.ricavi / self.spesa
            except ZeroDivisionError:
                return None
        else:
            return None

    def calcola_cpl(self):
        """Calcola il costo per lead e lo ritorna. In caso di zero lead, ritorna None"""
        if self.lead is not None:  # Se la campagna non è lead generation, lead è None
            try:
                return self.spesa / self.lead
            except ZeroDivisionError:
                return None
        else:
            return None
