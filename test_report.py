from classi import Campagna, MetricaGiornaliera
import report


def test_creazione_report(tmp_path):
    """Test di verifica della corretta creazione del report e esportazione nel file .txt"""
    # Creo campagne e metriche per test
    campagna1 = Campagna("Black Friday 2026", 50000, "Acquisti")
    metrica1 = MetricaGiornaliera("01-11-2026", 500, 12, 1000)
    campagna1.aggiungi_metrica(metrica1)
    report_campagna = report.genera_report(campagna1)  # ritorna report come stringa
    percorso_file = tmp_path / "report_campagne.txt"

    with open(percorso_file, "w", encoding="UTF-8") as file:
        file.write(report_campagna)

    assert isinstance(report_campagna, str)
    assert "Black Friday 2026" in report_campagna
    assert "N/D" in report_campagna
    assert percorso_file.read_text(encoding="UTF-8") == report_campagna  # controllo report e file coincidano
