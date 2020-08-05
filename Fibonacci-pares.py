fibo = []
fibopar = []
fibo.append (1)   #Necesito eliminar estos dos append, son una mala prática... 
fibo.append (1)
suma=0
i=1
j=0
while True:
    i = i +1
    fibo.append(fibo[i-1]+fibo[i-2])
    if fibo[i]%2==0:
        fibopar.append(fibo[i]);
        suma=suma+fibopar[j]
        j+=1
    if i == 10:
        break
    

print("\n La lista de los fibonacci es:\n",fibo)

print("\n La lista de los fibonacci par es:\n",fibopar)

print("\n La suma de todos los numeros de fibonacci par es :",suma)


