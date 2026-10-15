# Gestionale Ads

Gestionale da terminale (CLI) sviluppato in Python per organizzare clienti, campagne pubblicitarie e relative metriche giornaliere.

Il programma permette di importare dati da file CSV, calcolare indicatori di performance come CPA, CPL e ROAS, generare report, configurare alert personalizzati e salvare i dati localmente in formato JSON.

Il progetto è stato realizzato come esercizio pratico di sviluppo software, applicando programmazione orientata agli oggetti, gestione dei file, modularizzazione del codice e test automatizzati a un caso d'uso legato al digital advertising.

## Funzionalità

- **Gestione clienti:** visualizzazione e aggiunta di clienti.
- **Gestione campagne:** creazione di campagne associate a un cliente, con nome, tipologia e budget.
- **Importazione CSV:** caricamento delle metriche giornaliere all'interno di una campagna, con gestione degli errori di lettura e conversione numerica.
- **Calcolo KPI:** elaborazione della spesa totale, del costo per acquisizione (CPA), del costo per lead (CPL) e del ritorno sulla spesa pubblicitaria (ROAS).
- **Report:** generazione di riepiloghi delle campagne, visualizzabili nel terminale ed esportabili in formato TXT.
- **Alert:** verifica di soglie personalizzabili per CPA, CPL e ROAS.
- **Persistenza JSON:** salvataggio e caricamento di clienti, campagne e metriche tra diverse esecuzioni.
- **Menu interattivo:** accesso alle funzionalità attraverso un'interfaccia testuale.

I dati vengono inseriti manualmente o importati da file CSV. Il programma non prevede integrazioni dirette con le API delle piattaforme pubblicitarie.

## Requisiti e installazione

È necessario avere installato **Python 3**.

Per eseguire il gestionale sono sufficienti i moduli della libreria standard di Python. L'unica dipendenza esterna necessaria per i test è `pytest`.

### 1. Clonare la repository

```bash
git clone https://github.com/modernage12/gestionale_ads.git
cd gestionale_ads
```

### 2. Avviare il programma

```bash
python main.py
```

All'avvio, il gestionale carica automaticamente i dati salvati, se disponibili, e mostra il menu principale.

## Utilizzo

Il programma mette a disposizione otto opzioni:

```text
1. Visualizza clienti
2. Aggiungi cliente
3. Aggiungi campagna a un cliente
4. Importa metriche da CSV
5. Genera report di una campagna
6. Verifica alert
7. Salva dati
8. Esci
```

### Esempio di utilizzo

1. Selezionare **2** per creare un nuovo cliente.
2. Selezionare **3** per aggiungere una campagna al cliente, specificando nome, tipologia e budget.
3. Selezionare **4** per importare le metriche giornaliere da un file CSV.
4. Selezionare **5** per visualizzare il report della campagna ed eventualmente esportarlo in TXT.
5. Selezionare **6** per verificare le performance rispetto alle soglie desiderate.
6. Selezionare **7** per salvare i dati oppure **8** per uscire.

Se sono presenti modifiche non salvate, il programma chiede se salvarle prima della chiusura.

## Importazione delle metriche CSV

Per importare metriche è necessario che esistano un cliente e almeno una campagna associata.

Il programma richiede di selezionare la campagna e specificare il percorso del file CSV.

### Formato richiesto

Il file deve utilizzare:

- Codifica UTF-8 senza BOM.
- Virgola come separatore delle colonne.
- Punto come separatore decimale.
- Intestazioni indicate nell'esempio seguente.

```csv
data,spesa,conversioni,ricavi,lead
2026-10-01,150.50,10,600,20
2026-10-02,200,8,,15
2026-10-03,100,5,300,
```

| Colonna | Descrizione |
|---|---|
| `data` | Data della rilevazione, nel formato previsto `AAAA-MM-GG` |
| `spesa` | Spesa pubblicitaria giornaliera |
| `conversioni` | Numero intero di conversioni |
| `ricavi` | Ricavi giornalieri, facoltativi |
| `lead` | Numero intero di lead, facoltativo |

Le colonne `ricavi` e `lead` devono essere presenti anche quando i rispettivi valori non sono disponibili. Le celle vuote vengono convertite in `None`.

Il file CSV non deve specificare il cliente o la campagna: le metriche vengono associate alla campagna precedentemente selezionata dal menu.

Nella repository sono disponibili due file:

- `metriche_esempio.csv`: contiene dati validi per provare l'importazione.
- `metriche_non_valide.csv`: contiene valori numerici non validi, utilizzati per verificare la gestione degli errori.

## Calcolo degli indicatori

I KPI delle campagne vengono calcolati utilizzando i totali delle metriche giornaliere, non la media dei singoli indicatori giornalieri.

| Indicatore | Formula |
|---|---|
| **CPA** — Costo per acquisizione | Spesa totale / Conversioni totali |
| **CPL** — Costo per lead | Spesa totale / Lead totali |
| **ROAS** — Ritorno sulla spesa pubblicitaria | Ricavi totali / Spesa totale |

### Gestione dei valori mancanti

Un indicatore viene considerato non disponibile quando non esistono dati sufficienti per calcolarlo.

In particolare:

- Se il denominatore è zero, il relativo indicatore non è calcolabile.
- Se mancano i ricavi anche per una sola giornata, il ROAS complessivo non viene calcolato.
- Se mancano i lead anche per una sola giornata, il CPL complessivo non viene calcolato.
- Una campagna senza metriche presenta una spesa totale pari a zero e indicatori non disponibili.

Gli indicatori non calcolabili vengono rappresentati come `None` a livello applicativo e visualizzati come `N/D` nei report.

## Report e alert

### Generazione dei report

Il gestionale permette di generare un riepilogo contenente:

- Nome della campagna
- Budget
- Tipologia
- Spesa totale
- CPA
- CPL
- ROAS

Il report viene mostrato nel terminale e può essere esportato nel file `report.txt`.

L'esportazione crea il file nella directory di esecuzione del programma. Un'esportazione successiva sovrascrive il contenuto precedente.

### Sistema di alert

È possibile configurare tre soglie opzionali:

| Indicatore | Condizione di attivazione |
|---|---|
| CPA | Il valore supera la soglia massima impostata |
| CPL | Il valore supera la soglia massima impostata |
| ROAS | Il valore è inferiore alla soglia minima impostata |

Le soglie inserite devono essere maggiori di zero. Premendo **Invio** senza specificare un valore, il relativo controllo viene ignorato.

Il ROAS viene espresso come rapporto: ad esempio, `2` rappresenta ricavi pari a due volte la spesa pubblicitaria.

Gli alert vengono generati soltanto quando sono disponibili sia la soglia sia l'indicatore da confrontare.

Pertanto, il messaggio `Nessun alert` può indicare sia l'assenza di violazioni delle soglie sia l'impossibilità di effettuare alcuni confronti per mancanza di dati.

## Persistenza dei dati

Il gestionale utilizza un file JSON per conservare la struttura dei clienti, delle campagne e delle relative metriche giornaliere.

Il file `dati_clienti.json` viene:

- Caricato automaticamente all'avvio, quando esiste.
- Creato o aggiornato quando l'utente seleziona il salvataggio.
- Conservato nella stessa cartella di `main.py`.

Se il file non è presente, il programma viene avviato con una lista di clienti vuota.

Il salvataggio non avviene automaticamente dopo ogni modifica: il gestionale tiene traccia delle operazioni effettuate e, in presenza di modifiche non salvate, propone il salvataggio prima dell'uscita.

## Struttura del progetto

```text
gestionale_ads/
├── main.py                  # Menu CLI e coordinamento delle operazioni
├── classi.py                # Cliente, Campagna e MetricaGiornaliera
├── importazione.py          # Importazione e conversione dei dati CSV
├── persistenza.py           # Salvataggio e caricamento JSON
├── report.py                # Generazione dei report
├── alert.py                 # Verifica delle soglie KPI
├── test_cliente.py          # Test di classi, relazioni e calcoli
├── test_importazione.py     # Test di importazione CSV
├── test_persistenza.py      # Test della persistenza JSON
├── test_report.py           # Test dei report
├── test_alert.py            # Test del sistema di alert
├── metriche_esempio.csv     # Dataset CSV di esempio
├── metriche_non_valide.csv  # Dataset CSV con valori non validi
├── .gitignore
└── README.md
```

La logica applicativa è suddivisa in moduli con responsabilità specifiche.

Le classi gestiscono clienti, campagne, metriche e relativi calcoli. I moduli `importazione.py`, `persistenza.py`, `report.py` e `alert.py` gestiscono le rispettive operazioni, mentre `main.py` si occupa dell'interazione con l'utente e del coordinamento delle funzionalità.

## Test automatizzati

Il progetto include una suite di test realizzata con **pytest**.

Per installare pytest:

```bash
python -m pip install pytest
```

Per eseguire tutti i test dalla cartella del progetto:

```bash
python -m pytest -v
```

La suite verifica:

- Creazione e gestione degli oggetti.
- Associazione di campagne e metriche.
- Calcolo dei KPI e gestione dei denominatori nulli.
- Valori facoltativi delle metriche.
- Importazione dei CSV ed errori numerici.
- Salvataggio e caricamento JSON.
- Generazione dei report.
- Verifica degli alert.

I due CSV di esempio sono utilizzati nei test di importazione.

La suite automatizzata si concentra sui moduli applicativi e non include test dei flussi interattivi completi del menu CLI.

## Stato del progetto e limitazioni

Il progetto ha raggiunto gli obiettivi previsti per la sua prima versione: le funzionalità principali sono state implementate e integrate in un'interfaccia CLI.

Restano alcune limitazioni:

- Importare ripetutamente lo stesso CSV aggiunge nuovamente le metriche, senza un controllo sui duplicati.
- La validazione dei dati non comprende tutte le possibili anomalie, come date non valide o valori numerici incoerenti.
- La gestione degli errori non copre tutti i casi di file JSON danneggiati o problemi di scrittura.
- I test automatizzati non coprono l'interazione completa con il menu.

Questi aspetti non rientrano negli obiettivi della prima versione del progetto.

## Obiettivi formativi

Gestionale Ads è stato sviluppato nell'ambito di un percorso di apprendimento autonomo della programmazione in Python.

Il progetto ha permesso di approfondire e applicare:

- Programmazione orientata agli oggetti (OOP).
- Organizzazione del codice in funzioni e moduli.
- Gestione dei file CSV, JSON e TXT.
- Validazione degli input e gestione delle eccezioni.
- Persistenza dei dati.
- Test automatizzati con pytest.
- Refactoring e separazione delle responsabilità.
- Controllo di versione con Git.

L'approfondimento di SQL, SQLite e lo sviluppo di applicazioni backend con Django e API REST costituiscono tappe successive del percorso di studio, indipendenti da questo progetto.

## Autore

[modernage12](https://github.com/modernage12)