from classi import Campagna, MetricaGiornaliera


def verifica_alert(campagna, soglia_cpa = None, soglia_cpl = None, soglia_roas = None):
    """Controlla le metriche di una campagna, confronta con le soglie, e ritorna una lista di Alert se oltre soglia"""
    lista_alert = []  # Raccolgo gli alert come stringhe in una lista da ritornare a fine funzione
    cpa_totale = campagna.calcola_cpa_totale()
    cpl_totale = campagna.calcola_cpl_totale()
    roas_totale = campagna.calcola_roas_totale()

    if soglia_cpa is not None:
        if cpa_totale is not None and cpa_totale > soglia_cpa:
            lista_alert.append(f"ATTENZIONE! CPA oltre la soglia! (${cpa_totale:,.2f} vs. ${soglia_cpa})")

    if soglia_cpl is not None:
        if cpl_totale is not None and cpl_totale > soglia_cpl:
            lista_alert.append(f"ATTENZIONE! CPL oltre la soglia! (${cpl_totale:,.2f} vs. ${soglia_cpl})")

    if soglia_roas is not None:
        if roas_totale is not None and roas_totale < soglia_roas:
            lista_alert.append(f"ATTENZIONE! ROAS sotto la soglia! (x{roas_totale:,.2f} vs. x{soglia_roas})")

    return lista_alert