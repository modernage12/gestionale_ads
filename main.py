from classi import Cliente, Campagna, MetricaGiornaliera
from pathlib import Path
import importazione, persistenza, report, alert


def seleziona_cliente(lista_clienti):
    """Permette la selezione del cliente interessato tra quelli presenti se presenti e lo ritorna come oggetto"""
    cliente_selezionato = None

    print("\nSeleziona il cliente:")
    for numero, cliente in enumerate(lista_clienti, start=1):
        print(f"{numero}. {cliente}")

    if lista_clienti:
        while True:
            try:
                input_utente = int(input("\nNumero cliente: "))
                if 1 <= input_utente <= len(lista_clienti):
                    cliente_selezionato = lista_clienti[input_utente - 1]
                    break
                else:
                    print("Input fuori dal range, riprovare.")
                    continue
            except ValueError:
                print("Input non valido, riprovare.")
                continue

        return cliente_selezionato

    else:
        return None


def seleziona_campagna_cliente(cliente_selezionato):
    """Permette la selezione della campagna interessata del cliente selezionato e la ritorna come oggetto"""
    campagna_selezionata = None

    print("\nSelezione la campagna: ")

    for numero, campagna in enumerate(cliente_selezionato.campagne, start=1):
        print(f"{numero}. {campagna.nome}")

    if cliente_selezionato.campagne:
        while True:
            try:
                input_utente = int(input("\nNumero campagna: "))
                if 1 <= input_utente <= len(cliente_selezionato.campagne):
                    campagna_selezionata = cliente_selezionato.campagne[input_utente - 1]
                    break
                else:
                    print("Input fuori dal range, riprovare.")
                    continue
            except ValueError:
                print("Input non valido, riprovare.")
                continue

        return campagna_selezionata

    else:
        return None


def aggiungi_campagna(lista_clienti):
    """Aggiunge una campagna al cliente selezionato dell'utente"""
    cliente = seleziona_cliente(lista_clienti)
    nome_campagna = ""
    tipo_campagna = ""
    budget_campagna = 0

    if cliente:
        while True:
            nome_campagna = input("Nome campagna: ").strip()
            if nome_campagna:
                break
            else:
                print("Il nome non può essere vuoto, riprova.")
                continue

        while True:
            tipo_campagna = input("Tipo campagna: ").strip()
            if tipo_campagna:
                break
            else:
                print("Il tipo non può essere vuoto, riprova.")
                continue

        while True:
            try:
                input_budget_str = input("Budget campagna: ").strip()

                if input_budget_str:
                    budget_campagna = float(input_budget_str)
                    if budget_campagna > 0:
                        break
                    else:
                        print("Il budget deve essere maggiore di 0.")
                        continue
                else:
                    print("Il budget non può essere vuoto, riprova.")
                    continue
            except ValueError:
                print("Input non valido, riprovare.")
                continue

        campagna = Campagna(nome_campagna, budget_campagna, tipo_campagna)
        cliente.aggiungi_campagna(campagna)
        print(f"\nCampagna aggiunta al cliente {cliente.nome}.")

        return True  # Bool per flag modifiche non salvate

    else:
        print("Nessun cliente trovato.")
        return False


def verifica_alert(lista_clienti):
    """Richiede soglie KPI delle campagne dei clienti selezionati e ritorna i messaggi di alert"""
    soglia_cpa = None
    soglia_cpl = None
    soglia_roas = None
    cliente_selezionato = seleziona_cliente(lista_clienti)

    if cliente_selezionato:
        campagna_selezionata = seleziona_campagna_cliente(cliente_selezionato)

        if campagna_selezionata:
            while True:
                input_soglia = input("Soglia CPA: (invio per ignorare): ").strip()

                if input_soglia == "":
                    break

                try:
                    if float(input_soglia) > 0:
                        soglia_cpa = float(input_soglia)
                        break
                    else:
                        print("Il valore deve essere maggiore di 0.")
                        continue

                except ValueError:
                    print("Valore non valido, riprovare.")
                    continue

            while True:
                input_soglia = input("Soglia CPL: (invio per ignorare): ").strip()

                if input_soglia == "":
                    break

                try:
                    if float(input_soglia) > 0:
                        soglia_cpl = float(input_soglia)
                        break
                    else:
                        print("Il valore deve essere maggiore di 0.")
                        continue

                except ValueError:
                    print("Valore non valido, riprovare.")
                    continue

            while True:
                input_soglia = input("Soglia ROAS: (invio per ignorare): ").strip()

                if input_soglia == "":
                    break

                try:
                    if float(input_soglia) > 0:
                        soglia_roas = float(input_soglia)
                        break
                    else:
                        print("Il valore deve essere maggiore di 0.")
                        continue

                except ValueError:
                    print("Valore non valido, riprovare.")
                    continue

            alert_list = alert.verifica_alert(campagna_selezionata, soglia_cpa, soglia_cpl,
                                              soglia_roas)

            if alert_list:
                for singolo_alert in alert_list:
                    print(singolo_alert)
            else:
                print("Nessun alert.")

        else:
            print("Nessuna campagna disponibile.")
            return

    else:
        print("Nessun cliente disponibile.")
        return


def importa_metriche(lista_clienti):
    """Importa le metriche da un file .csv esterno all'interno della campagna del cliente"""
    cliente = seleziona_cliente(lista_clienti)

    if cliente is not None:
        campagna = seleziona_campagna_cliente(cliente)
        metriche_importate = []

        if campagna is not None:
            while True:
                percorso_input = input("Percorso file CSV: ")
                percorso_file_csv = Path(percorso_input)  # ottengo il percorso completo

                if percorso_input:
                    try:
                        metriche_importate = importazione.importa_metriche(percorso_file_csv)

                        for metrica in metriche_importate:
                            campagna.aggiungi_metrica(metrica)

                        break

                    except FileNotFoundError:
                        print("Percorso non valido, riprovare.")
                        continue
                    except ValueError as err:
                        print(err)  # Stampo l'eccezione prevista dall'oggetto metrica
                        continue

                else:
                    print("Il percorso non può essere vuoto, riprovare.")
                    continue

            print(
                f"Metriche importate correttamente nella campagna {campagna.nome} (+{len(metriche_importate)} metriche)")

            return True

        else:
            print("Nessuna campagna trovata.")
            return False

    else:
        print("Nessun cliente trovato.")
        return False


def genera_report(lista_clienti):
    """Genera il report della campagna del cliente selezionato con esportazione in file .txt se richiesto"""
    cliente = seleziona_cliente(lista_clienti)

    if cliente is not None:
        campagna = seleziona_campagna_cliente(cliente)

        if campagna is not None:
            report_finale = report.genera_report(campagna)
            print(report_finale)

            while True:
                scelta_utente = input("\nVuoi esportare il report? (s/n): ").strip()

                if scelta_utente:
                    if scelta_utente == "s":
                        with open("report.txt", "w", encoding="UTF-8") as file:
                            file.write(report_finale)
                    elif scelta_utente == "n":
                        break
                    else:
                        print("Input non valido, riprovare.")
                        continue
                else:
                    print("La scelta non può essere vuota.")
                    continue

                break

        else:
            print("Nessuna campagna trovata.")
            return None
    else:
        print("Nessun cliente trovato.")
        return None


def avvia_programma():
    cartella = Path(__file__).resolve().parent
    percorso_file = cartella / "dati_clienti.json"
    modifiche_non_salvate = False

    try:
        lista_clienti = persistenza.carica_clienti(percorso_file)
    except FileNotFoundError:
        lista_clienti = []

    lunghezza_titolo = len("Gestione Ads") * 2  # 2 per raddoppiare la grandezza

    print("=" * lunghezza_titolo)
    print(f"{'Gestione Ads':^{lunghezza_titolo}}")
    print("=" * lunghezza_titolo)

    print("1. Visualizza clienti")
    print("2. Aggiungi cliente")
    print("3. Aggiungi campagna a un cliente")
    print("4. Importa metriche da CSV")
    print("5. Genera report di una campagna")
    print("6. Verifica alert")
    print("7. Salva dati")
    print("8. Esci\n\n")

    while True:
        try:
            selezione = int(input("\nSeleziona un'opzione: "))
        except ValueError:
            print("Selezione non valida, riprova.")
            continue

        if selezione == 1:
            for clienti in lista_clienti:
                print(clienti)

        elif selezione == 2:
            while True:

                nome_cliente = input("Inserisci nome nuovo cliente: ").strip()

                if not nome_cliente:  # controlla se la stringa è vuota
                    print("Il nome non può essere vuoto, riprovare.")
                    continue

                nuovo_cliente = Cliente(nome_cliente)
                lista_clienti.append(nuovo_cliente)
                modifiche_non_salvate = True
                break

        elif selezione == 3:
            # Eseguo solo se avvengono modifiche per evitare sovrascrizioni modifiche_non_salvate
            if aggiungi_campagna(lista_clienti):
                modifiche_non_salvate = True

        elif selezione == 4:
            if importa_metriche(lista_clienti):
                modifiche_non_salvate = True

        elif selezione == 5:
            genera_report(lista_clienti)

        elif selezione == 6:
            verifica_alert(lista_clienti)

        elif selezione == 7:
            persistenza.salva_clienti(lista_clienti, percorso_file)
            modifiche_non_salvate = False
            print("Dati salvati.")

        elif selezione == 8:
            if modifiche_non_salvate:
                scelta_utente = input("Attenzione! Modifiche non salvate, vuoi salvarle prima? (s/n): ").lower()
                while True:
                    if scelta_utente == 's':
                        persistenza.salva_clienti(lista_clienti, percorso_file)
                        print("Dati salvati. Chiusura programma.")
                        break
                    elif scelta_utente == 'n':
                        print("Chiusura programma.")
                        break
                    else:
                        scelta_utente = input("Input non valido, riprovare: ").lower()
                        continue
            else:
                print("Chiusura programma.")
                break

            break


if __name__ == '__main__':
    avvia_programma()
