from classi import Cliente, MetricaGiornaliera, Campagna


def test_cliente():
    """Test per verificare che la classe generi correttamente l'oggetto Cliente"""
    cliente1 = Cliente("Lorenzo")  # oggetti creati in singoli test per evitare modifiche di altri test
    cliente2 = Cliente("Gloria")

    assert cliente1.nome == "Lorenzo"
    assert cliente1.campagne == []
    assert cliente2.nome == "Gloria"
    assert cliente2.campagne == []


def test_campagne():
    """Test per verificare che la classe crei oggetti indipendenti"""
    cliente1 = Cliente("Lorenzo")
    cliente2 = Cliente("Gloria")

    cliente1.campagne.append("Meta")

    assert cliente1.campagne == ["Meta"]
    assert cliente2.campagne == []


def test_str():
    cliente1 = Cliente("Lorenzo", ["Campagna 1", "Campagna 2"])

    assert str(cliente1) == "Cliente: Lorenzo (2 campagne)"


def test_metrica():
    """Test per verificare che la classe crei oggetti in modo corretto"""
    metrica1 = MetricaGiornaliera("2026-09-12", 200, 10)
    metrica2 = MetricaGiornaliera("2026-09-13", 200, 7)

    assert metrica1.data == "2026-09-12"
    assert metrica1.spesa == 200
    assert metrica1.conversioni == 10
    assert metrica2.data == "2026-09-13"
    assert metrica2.spesa == 200
    assert metrica2.conversioni == 7


def test_calcoli_metrica():
    """Test per verificare che i metodi delle classi funzionino correttamente"""
    metrica1 = MetricaGiornaliera("2026-09-12", 200, 10)
    metrica2 = MetricaGiornaliera("2026-09-13", 200, 7)

    assert metrica1.calcola_cpa() == 20
    assert metrica1.calcola_roas() is None
    assert metrica1.calcola_cpl() is None
    assert metrica2.calcola_cpa() == (200 / 7)
    assert metrica2.calcola_roas() is None
    assert metrica2.calcola_cpl() is None

    metrica3 = MetricaGiornaliera("2026-11-03", 300, 5, 2300)
    metrica4 = MetricaGiornaliera("2026-06-21", 150, 3, lead=3)

    assert metrica3.calcola_cpa() == 300 / 5
    assert metrica3.calcola_roas() == 2300 / 300
    assert metrica3.calcola_cpl() is None
    assert metrica4.calcola_cpa() == 150 / 3
    assert metrica4.calcola_roas() is None
    assert metrica4.calcola_cpl() == 150 / 3


def test_metriche_zero():
    """Test per verificare che l'error catching dei metodi funzioni correttamente"""
    metrica1 = MetricaGiornaliera("2026-09-12", 0, 0, 0, 0)

    # In caso di divisione per 0 l'error catching dovrebbe restituire None
    assert metrica1.calcola_cpl() is None
    assert metrica1.calcola_roas() is None
    assert metrica1.calcola_cpa() is None


def test_campagna():
    """Test per verificare la corretta creazione degli oggetti Campagna"""
    campagna1 = Campagna("Black Friday 2026", 50000, "Acquisti E-commerce")
    campagna2 = Campagna("Natale 2026", 70000, "Lead Generation")

    assert campagna1.nome == "Black Friday 2026"
    assert campagna1.budget == 50000
    assert campagna1.tipo == "Acquisti E-commerce"
    assert campagna2.nome == "Natale 2026"
    assert campagna2.budget == 70000
    assert campagna2.tipo == "Lead Generation"

    metrica1 = MetricaGiornaliera("2026-11-01", 500, 10)
    campagna2.aggiungi_metrica(metrica1)

    assert len(campagna1.metriche) == 0  # Controllo che venga creata la lista vuota per metriche
    assert len(campagna2.metriche) == 1


def test_aggiunta_metrica():
    campagna1 = Campagna("Black Friday 2026", 50000, "Acquisti E-commerce")

    metrica1 = MetricaGiornaliera("2026-11-01", 500, 10)
    metrica2 = MetricaGiornaliera("2026-11-02", 500, 7)

    campagna1.aggiungi_metrica(metrica1)
    campagna1.aggiungi_metrica(metrica2)

    assert metrica1 in campagna1.metriche
    assert campagna1.metriche[0] == metrica1
    assert metrica2 in campagna1.metriche
    assert campagna1.metriche[1] == metrica2


def test_calcolo_spesa_totale():
    campagna1 = Campagna("Black Friday 2026", 50000, "Acquisti E-commerce")
    campagna2 = Campagna("Natale 2026", 70000, "Lead Generation")

    metrica1 = MetricaGiornaliera("2026-11-01", 500, 10)
    metrica2 = MetricaGiornaliera("2026-11-02", 500, 7)
    metrica3 = MetricaGiornaliera("2026-11-03", 500, 8)

    campagna1.aggiungi_metrica(metrica1)
    campagna1.aggiungi_metrica(metrica2)
    campagna1.aggiungi_metrica(metrica3)

    assert campagna1.calcola_spesa_totale() == 1500
    assert campagna2.calcola_spesa_totale() == 0  # Senza metriche ritorna 0


def test_calcolo_cpa_totale():
    """Test per verificare che il metodo per il calcolo del cpa totale funzioni correttamente"""
    campagna1 = Campagna("Black Friday 2026", 50000, "Acquisti E-commerce")

    metrica1 = MetricaGiornaliera("2026-11-01", 500, 10)
    metrica2 = MetricaGiornaliera("2026-11-02", 500, 7)
    metrica3 = MetricaGiornaliera("2026-11-03", 500, 8)

    campagna1.aggiungi_metrica(metrica1)
    campagna1.aggiungi_metrica(metrica2)
    campagna1.aggiungi_metrica(metrica3)

    assert campagna1.calcola_cpa_totale() == 1500 / 25

    campagna2 = Campagna("Natale 2026", 50000, "Acquisti E-commerce")

    assert campagna2.calcola_cpa_totale() is None  # Nessuna metrica ritorna None

    campagna3 = Campagna("Natale 2026", 50000, "Acquisti E-commerce")

    metrica4 = MetricaGiornaliera("2026-11-08", 500, 0)

    campagna3.aggiungi_metrica(metrica4)

    assert campagna3.calcola_cpa_totale() is None  # Con 0 conversioni ritorna None
