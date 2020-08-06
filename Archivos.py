"""with open("/home/daniel/Desktop/ArchivosPython/Archivo_de_texto.txt","a+") as miarchivo:
#print(miarchivo.read(10))  Diez es en numero de bytes que se leen y un caracter cabe en un byte
	print(miarchivo.read())
	T= input ("Please give me a text to write in the file\n");
	miarchivo.write("\n")	
	miarchivo.write(T)
#miarchivo.close()

with open("/home/daniel/Desktop/ArchivosPython/Archivo_de_texto.txt","r") as miarchivo:
	print(miarchivo.read())

"""
with open("texto.txt","a+") as miarchivo:
#print(miarchivo.read(10)) """ Diez es en numero de bytes que se leen y un caracter cabe en un byte"""
	b=miarchivo.read()
	print(b)
	b. replace ("phi","x")	
	b. replace ("teta","y")
	b. replace ("r","z")
	miarchivo.write(b)
	print(b)
