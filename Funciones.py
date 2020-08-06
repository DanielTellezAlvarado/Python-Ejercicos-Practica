a=[] #esta lista es global
def mi_funcion(a):	
	b=[]	#esta lista no puede ser usada fuera de la función 
	for i in range(a):
		if not i%2==0:
			b.append(str(i+1))
	return b



a=mi_funcion(int(input("Dame un numero:")))  #se llama a la funcion y se guarda el retorno en la lista a


print(a) #imprime la lista tal cual regresa la función


for i in range(len(a)):
	print("\n",a[i])


