"""EJERCICION°2 WEYMAR VILLCA ORUÑO utilizando los coeficientes a,b,c se pide mostrar la naturaleza de sus numeros"""
import math
a=int(input("intro valor de a: "))
b=int(input("intro valor de b: "))
c=int(input("intro valor de c: "))
dis=b**2-4*a*c
if dis>0:
	resul1=(-b+(math.sqrt((b**2)-(4*a*c))))
	resul2=(-b-(math.sqrt((b**2)-(4*a*c))))
	p=2*a
	resultado=resul1/p
	resultado2=resul2/p
	print("la raiz de la ecuacion es: ",resultado)
	print("la raiz de la ecuacion es: ",resultado2)
	
else:
	print("no tiene soliciones reales")