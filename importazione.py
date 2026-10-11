import csv
from classi import MetricaGiornaliera


def importa_metriche(percorso_file_csv):
    """Importa file .csv da percorso, estrae le metriche e le ritorna in una lista come oggetti"""
    with open(percorso_file_csv, "r", encoding="UTF-8", newline="") as file_csv:
        metriche_csv = csv.DictReader(file_csv)  # Passo il file .csv come oggetto contenete dizionari

        lista_metriche = []

        for metrica in metriche_csv:
            if metrica["ricavi"] != "":
                ricavi = float(metrica["ricavi"])
            else:
                ricavi = None

            if metrica["lead"] != "":
                lead = int(metrica["lead"])
            else:
                lead = None

            # passo un oggetto MetricaGiornaliera invece che una lista per facilitare l'accesso
            lista_metriche.append(
                MetricaGiornaliera(metrica["data"], float(metrica["spesa"]), int(metrica["conversioni"]),
                                   ricavi, lead))

    return lista_metriche
