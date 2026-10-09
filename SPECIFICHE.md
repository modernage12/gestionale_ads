<h1>Specifiche Programma</h1>

<h2>Obiettivo</h2>

Programma che gestisce clienti e campagne. Import da file CSV delle metriche giornaliere con salvataggio di file
con report con le metriche come CPL, CPA, ROAS e alert quando una metrica supera una soglia

<h2>Classi</h2>
<b>Cliente</b>: Nome, Campagne

<b>Campagna</b>: Nome, Budget, Tipo, Piattaforma, Metriche

<b>Metrica Giornaliera</b>: Data, Spesa, Conversioni, Ricavi, Lead

## Funzionalità

Il programma permette di:

1. Aggiungere, elencare e cercare clienti.
2. Creare campagne pubblicitarie associate a un cliente.
3. Gestire campagne sulle piattaforme Meta e Google.
4. Importare metriche giornaliere da file CSV.
5. Visualizzare il riepilogo delle metriche di una campagna.
6. Visualizzare una tabella delle metriche suddivise per giorno.
7. Calcolare CPA, ROAS e CPL.
8. Mostrare un alert quando il CPA supera una soglia prestabilita.
9. Salvare e caricare i dati da un file JSON.

## Relazioni tra le classi

* Un cliente può avere più campagne.
* Ogni campagna appartiene a un cliente.
* Una campagna può avere più metriche giornaliere.
* Ogni metrica giornaliera contiene i dati relativi a una giornata di attività della campagna.

## Calcolo degli indicatori

* **CPA** = spesa totale / conversioni totali.
* **ROAS** = ricavi totali / spesa totale.
* **CPL** = spesa totale / lead totali.

Il programma deve gestire i casi in cui il denominatore è zero, evitando errori durante i calcoli.

## Importazione CSV

Il programma importa le metriche giornaliere da un file CSV.

Il formato iniziale previsto è:

`nome_campagna,data,spesa,conversioni,ricavi,lead`

La data deve essere nel formato `AAAA-MM-GG`.

Il programma deve controllare i dati importati e gestire file mancanti o righe non valide.

## Salvataggio dei dati

I dati di clienti, campagne e metriche devono essere salvati in un file JSON e poter essere ricaricati all'avvio del programma.

## Alert

Il programma deve segnalare quando il CPA di una campagna supera una soglia definita dall'utente o dalla configurazione del programma.
