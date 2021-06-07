"""
1. Sin utilizar funciones de minimización, maximización, sin condicionales, sin ciclos,
sin vectores y todo en un solo bloque."""

codigo = "est0001"
est1_nota1 = 40
est1_nota2 = 50
est1_nota3 = 39
est1_nota4 = 76
est1_nota5 = 16

"""Primera"""
a = est1_nota1
b = est1_nota2
medioRango = (b - a) / 2    #Mitad del camino entre el dato de menor valor y el dato de mayor.
valorAbsolutoMedioRango = (medioRango ** 2) ** (1 / 2)
#print(valorAbsolutoMedioRango)
media = ((a + b) / 2)
#print(media)
menorAyB = media - valorAbsolutoMedioRango
#print(menorAyB)
n1 = media + valorAbsolutoMedioRango

"""Segunda"""
a = menorAyB    #Menor de la nota1 y nota2 comparada con la nota3
b = est1_nota3
medioRango = (b - a) / 2
valorAbsolutoMedioRango = (medioRango ** 2) ** (1 / 2)
media = ((a + b) / 2)
menorAyB = media - valorAbsolutoMedioRango
#print(menorAyB)
n2 = media + valorAbsolutoMedioRango

"""Tercera"""
a = menorAyB
b = est1_nota4
medioRango = (b - a) / 2
valorAbsolutoMedioRango = (medioRango ** 2) ** (1 / 2)
media = ((a + b) / 2)
menorAyB = media - valorAbsolutoMedioRango
#print(menorAyB)
n3 = media + valorAbsolutoMedioRango

"""Cuarta"""
a = menorAyB
b = est1_nota5
medioRango = (b - a) / 2
valorAbsolutoMedioRango = (medioRango ** 2) ** (1 / 2)
media = ((a + b) / 2)
menorAyB = media - valorAbsolutoMedioRango
print("El menor de todos es: ",menorAyB)
n4 = media + valorAbsolutoMedioRango
print(n1)
print(n2)
print(n3)
print(n4)
promedioSinEscala = ((n1 + n2 + n3 + n4) / 4)
promedio = (promedioSinEscala / 100) * 5
print("El promedio ajustado del estudiante", codigo, "es:","{0:.2f}".format(promedio))