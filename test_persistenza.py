from classi import MetricaGiornaliera, Campagna, Cliente
import persistenza as ps


def test_persistenza(tmp_path):
    percorso_file = tmp_path / "test_persistenza_json.json"

    metrica1 = MetricaGiornaliera("01-01-2027", 5000, 100, 50000)
    campagna1 = Campagna("New Year", 500000, "Acquisti", [metrica1])
    cliente1 = Cliente("Prova 1", [campagna1])
    cliente2 = Cliente("Prova 2")

    ps.salva_clienti([cliente1, cliente2], "test_persistenza_json.json")
    clienti = ps.carica_clienti("test_persistenza_json.json")

    """Test di verifica del corretto salvataggio e successiva lettura file json (serializzazione/deserializzazione)"""
    assert clienti[0].nome == "Prova 1"
    assert clienti[1].nome == "Prova 2"
    assert len(clienti[0].campagne) == 1
    assert len(clienti[1].campagne) == 0
    assert clienti[0].campagne[0].metriche[0].spesa == 5000
    assert type(clienti[0]) is Cliente
    assert type(clienti[0].campagne[0]) is Campagna
