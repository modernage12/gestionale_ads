from classi import Campagna, MetricaGiornaliera


def genera_report(campagna):
    """Genera il report della campagna passata come parametro e lo ritorna come testo"""
    # variabili per formattazione report
    lunghezza_titolo = len(f"REPORT:  {campagna.nome}")
    lunghezza_nome_campagna = len(campagna.nome)

    cpa_totale = campagna.calcola_cpa_totale()
    cpl_totale = campagna.calcola_cpl_totale()
    roas_totale = campagna.calcola_roas_totale()
    spesa_totale = campagna.calcola_spesa_totale()

    righe = []  # lista per raccogliere ogni stringa

    righe.append("=" * lunghezza_titolo)
    righe.append(f"REPORT: {campagna.nome}")
    righe.append("=" * lunghezza_titolo)
    righe.append(f"{'Budget: ':<{lunghezza_nome_campagna}}{campagna.budget:,.2f}")
    righe.append(f"{'Tipo: ':<{lunghezza_nome_campagna}}{campagna.tipo}")

    if cpa_totale is not None:
        righe.append(f"{'CPA: ':<{lunghezza_nome_campagna}}{cpa_totale:,.2f}")
    else:
        righe.append(f"{'CPA: ':<{lunghezza_nome_campagna}}N/D")

    if cpl_totale is not None:
        righe.append(f"{'CPL: ':<{lunghezza_nome_campagna}}{cpl_totale:,.2f}")
    else:
        righe.append(f"{'CPL: ':<{lunghezza_nome_campagna}}N/D")

    if roas_totale is not None:
        righe.append(f"{'ROAS: ':<{lunghezza_nome_campagna}}{roas_totale:,.2f}")
    else:
        righe.append(f"{'ROAS: ':<{lunghezza_nome_campagna}}N/D")

    righe.append(f"{'Spesa Totale: ':<{lunghezza_nome_campagna}}{spesa_totale:,.2f}")

    return "\n".join(righe)  # ritorno la lista come un'unica stringa, ogni elemento preso come singola riga e a capo
