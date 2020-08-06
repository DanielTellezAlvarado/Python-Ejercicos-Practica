
#esta función hará lo mismo que input pero verificará la entrada del usuario hasta que ingrese un numero

def verificador_de_entrada_numerica(r):     
	print(r)	
	while True:	
		try:
			a=float(input(""))
			if ((a/1)==a):
				return a;
		except (TypeError,ValueError):
			print("\nNo ingresaste un numero por favor intenta de nuevo\n")




#solo es para no hacer tan tediosa la anotación la funcion entrada hará lo mismo

entrada=verificador_de_entrada_numerica  



#programa muestra para verificar el uso de la función

print("Vamos a sumar dos numeros\n")
a=entrada("Ingresa el primer numero\n")
b=entrada("Ingresa el segundo numero\n")
print("La suma es: ",a+b)

