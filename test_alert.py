import alert
from classi import Campagna, MetricaGiornaliera


def test_alert():
    campagna1 = Campagna("Black Friday 2026", 5000, "Acquisti")
    metrica1 = MetricaGiornaliera("01-11-2026", 250, 23, 5600, 21)
    campagna1.aggiungi_metrica(metrica1)

    soglia_cpa = 5
    soglia_roas = 30
    soglia_cpl = 6
    lista_avvisi = alert.verifica_alert(campagna1, soglia_cpa, soglia_cpl, soglia_roas)

    assert any("$10.87 vs. $5" in avviso for avviso in lista_avvisi)
    assert any("x22.40 vs. x30" in avviso for avviso in lista_avvisi)
    assert any("$11.90 vs. $6" in avviso for avviso in lista_avvisi)
    assert isinstance(lista_avvisi, list)

    campagna2 = Campagna("Black Friday 2026", 5000, "Acquisti")
    metrica2 = MetricaGiornaliera("02-11-2026", 250, 23, 5600, 21)
    campagna2.aggiungi_metrica(metrica2)

    soglia_cpa = 30
    soglia_roas = 2

    lista_avvisi = alert.verifica_alert(campagna2, soglia_cpa, None, soglia_roas)

    assert lista_avvisi == []
