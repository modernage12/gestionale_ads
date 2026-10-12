from classi import MetricaGiornaliera
from pathlib import Path
import importazione
import pytest

cartella_csv = Path(__file__).resolve().parent  # Ottengo la cartella in cui è contenuto questo file
#  il file di test e file .csv devono stare nella stessa cartella
percorso_file_csv = cartella_csv / "metriche_esempio.csv"
percorso_metriche_non_valide = cartella_csv / "metriche_non_valide.csv"


def test_importa_metriche():
    """Test di verifica per corretta importazione e lettura file .csv e metriche"""
    lista_metriche_importate = importazione.importa_metriche(percorso_file_csv)

    assert len(lista_metriche_importate) == 3  # tre righe nel file csv, quindi 3 oggetti metriche

    for metrica in lista_metriche_importate:
        assert isinstance(metrica, MetricaGiornaliera)

    assert lista_metriche_importate[0].spesa == 150.5  # Spesa prima giornata/metrica è 150.5
    assert lista_metriche_importate[1].ricavi is None  # Ricavi seconda giornata sono None
    assert lista_metriche_importate[2].lead is None  # Lead terza giornata sono None


def test_importazione_non_valida():
    """Test di verifica per errore ValueError in caso di input da file CSV non numerico"""
    # Funzionalità per testare gli errori, match per verificare il raised error
    with pytest.raises(ValueError, match="Errore alla riga 3: valore numerico non valido"):
        # Passando una stringa a float() in importa_metriche avremo ValueError
        importazione.importa_metriche(percorso_metriche_non_valide)  # Partirà un ValueError


