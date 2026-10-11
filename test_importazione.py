from classi import MetricaGiornaliera
from pathlib import Path
import importazione

cartella_csv = Path(__file__).resolve().parent  # Ottengo la cartella in cui è contenuto questo file
#  il file di test e file .csv devono stare nella stessa cartella
percorso_file_csv = cartella_csv / "metriche_esempio.csv"


def test_importa_metriche():
    """Test di verifica per corretta importazione e lettura file .csv e metriche"""
    lista_metriche_importate = importazione.importa_metriche(percorso_file_csv)

    assert len(lista_metriche_importate) == 3  # tre righe nel file csv, quindi 3 oggetti metriche

    for metrica in lista_metriche_importate:
        assert isinstance(metrica, MetricaGiornaliera)

    assert lista_metriche_importate[0].spesa == 150.5  # Spesa prima giornata/metrica è 150.5
    assert lista_metriche_importate[1].ricavi is None  # Ricavi seconda giornata sono None
    assert lista_metriche_importate[2].lead is None  # Lead terza giornata sono None
