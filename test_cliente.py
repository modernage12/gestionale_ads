from classi import Cliente


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

