from classi import Cliente, MetricaGiornaliera


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