import numpy as np
from scipy.integrate import trapz

def concentracao_plasmatica (dose, k, t):
  return dose * np.exp(-k *t)

def auc(dose, k, t):
  t = np.linspace(0,t)
  concentracao = concentracao_plasmatica(dose, k, t)
  return trapz(concentracao, t)

def aumc (t, c,):
  t = np.linspace(0,t)
  aumc = trapz(np.multiply(c,t), t)
  return aumc


dose = float(input("insira a dosagem: "))
k = float(input("insira a constante de eliminacao do farmaco: "))
tempo = int (input("insira o tempo em horas: "))
print("AUC: {} mg/L.h".format(auc(dose,k,tempo)))
print("AUMC: {} mg/L.h^2".format(aumc(tempo,concentracao_plasmatica(dose,k,tempo))))
print("MRT: {} h".format(aumc(tempo,concentracao_plasmatica(dose,k,tempo))/auc(dose,k,tempo)))


