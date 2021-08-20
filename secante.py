import math

expr = input("Ingrese la expresion a evaluar: ")

xi=float(input("Ingrese xi: "))
xi_menos_uno = float(input("Ingrese xi-1: "))
tol=1.e-5
maxit=100
it=0
print("it              xi              xi-1              f(xi)             f(xi-1)               x2                Error")


while abs(xi_menos_uno-xi)>tol and it <= maxit:
	it=it +1
	libres = dict(x=xi)  # evalia xi
	funcs = vars(math)	
	fxi = eval(expr, funcs,libres)

	libres = dict(x=xi_menos_uno) #evalua xi-1
	funcs = vars(math)	
	fxi_menos_uno = eval(expr, funcs,libres)


	xi_mas_uno = xi -((fxi*(xi_menos_uno-xi))/(fxi_menos_uno - fxi)) #xi+1

	error=((xi_mas_uno-xi)/xi_mas_uno)*100 #error
	

	print (it,end=" |")
	print (xi,end=" |")
	print (xi_menos_uno,end=" |")
	print (fxi,end=" |")
	print (fxi_menos_uno,end="  |")
	print (xi_mas_uno, end="|")
	print (error,"%	")

	xi_menos_uno = xi
	xi = xi_mas_uno

print ("raiz aproximada= ",xi_mas_uno)