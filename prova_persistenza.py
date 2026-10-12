from persistenza import carica_clienti
from classi import MetricaGiornaliera, Campagna, Cliente

clienti = carica_clienti("prova.json")

print(type(clienti))
print(clienti[0])
print(clienti[1])
print(clienti[1].campagne)
print(clienti[0].campagne[0].metriche)