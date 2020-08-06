while True:
	print("\nPara sumar escribe \"sumar\"\n")
	print("\nPara restar escribe \"restar\"\n")
	print("\nPara multiplicar escribe \"multiplicar\"\n")
	print("\nPara dividir escribe \"dividir\"\n")
	print("\nPara salir escribe \"salir\"\n")
	Palabra = input (" :")
	if Palabra=='sumar':
		a= float(input("\n Ingresa el primer valor: "))
		b= float(input("\n Ingresa el segundo valor: "))
		print("\nEl resultado de sumar " + str(a) + " + " + str(b) +" es: " +str(a+b))
	elif Palabra=="restar":
		a= float(input("\n Ingresa el primer valor: "))
		b= float(input("\n Ingresa el segundo valor: "))
		print("\nEl resultado de restar ",a," - ",b,"es: ",a-b)
	elif Palabra=="multiplicar":
		a= float(input("\n Ingresa el primer valor: "))
		b= float(input("\n Ingresa el segundo valor: "))
		print("\nEl resultado de multiplicar ",a," x ",b,"es: ",a*b)
	elif Palabra=="dividir":
		a= float(input("\n Ingresa el primer valor: "))
		b= float(input("\n Ingresa el segundo valor: "))
		print("\nEl resultado de dividir ",a," / ",b,"es: ",a/b)
	elif Palabra=="salir":
		break;
	else:
		print("\nEscribiste: \""+Palabra+"\" y eso no esta en las opciones\n")
