import json
from classi import Cliente, Campagna, MetricaGiornaliera


def salva_clienti(clienti, percorso_file):
    """Riceve lista oggetti Cliente e percorso file json, estrae info dagli oggetti e li esporta in file json"""
    lista_clienti = []

    for cliente in clienti:
        lista_campagne = []

        for campagna in cliente.campagne:
            lista_metriche = []

            for metrica in campagna.metriche:
                lista_metriche.append({
                    "data": metrica.data,
                    "spesa": metrica.spesa,
                    "conversioni": metrica.conversioni,
                    "ricavi": metrica.ricavi,
                    "lead": metrica.lead
                })

            lista_campagne.append({
                "nome": campagna.nome,
                "budget": campagna.budget,
                "tipo": campagna.tipo,
                "metriche": lista_metriche
            })

        # json non sa gestire oggetti, richiede dictionaries - Serializzazione
        lista_clienti.append({
            "nome": cliente.nome,
            "campagne": lista_campagne
        })

    with open(percorso_file, "w", encoding="UTF-8") as file_json:
        # indent=4 ed ensure_ascii=False per miglior formattazione
        json.dump(lista_clienti, file_json, indent=4, ensure_ascii=False)


def carica_clienti(percorso_file):
    """Riceve percorso file json con dati clienti e deserializza in oggetti e ritorna la lista dei Clienti"""
    with open(percorso_file, "r", encoding="UTF-8") as file_json:
        lista_json = json.load(file_json)

    lista_clienti = []

    for cliente in lista_json:
        lista_campagne = []

        for campagna in cliente["campagne"]:
            lista_metriche = []

            for metrica in campagna["metriche"]:
                metrica_campagna = MetricaGiornaliera(metrica["data"], metrica["spesa"], metrica["conversioni"],
                                                      metrica["ricavi"], metrica["lead"])
                lista_metriche.append(metrica_campagna)

            campagna_cliente = Campagna(campagna["nome"], campagna["budget"], campagna["tipo"], lista_metriche)
            lista_campagne.append(campagna_cliente)

        nuovo_cliente = Cliente(cliente["nome"], lista_campagne)
        lista_clienti.append(nuovo_cliente)

    return lista_clienti
