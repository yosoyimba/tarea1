#-*- coding: utf-8 -*-

def Primos(n):
	lista = list()
	for a in range(1,n):
		es_primo = True
		for b in range(2,a):
			if ((a%b) == 0):
				es_primo = False
				break
		if es_primo:
			lista.append(a)
	return lista

if __name__ == "__main__":
	print "Imprime los números primos desde 1 a N"
	print "Se invoca como Primos(n), con n natural"
