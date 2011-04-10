#-*- coding: utf-8 -*-
def Fibonacci(n):
	lista = [1,1]
	for a in range(2,n):
		lista.append(lista[a-2] + lista[a-1])
	return lista

if __name__ == "__main__":
	print "Imprime los primeros n números de la sucesión de Fibonacci"
	print "Se invoca como Fibonacci(n), donde n es un entero"
