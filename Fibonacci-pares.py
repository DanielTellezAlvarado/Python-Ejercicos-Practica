fibo = [1,1]
fibopar = []
suma=0
i=1
j=0
a=int(input("hasta que numero de fibonacci quieres ???\n"))
while True:
    i = i +1
    fibo.append(fibo[i-1]+fibo[i-2])
    if fibo[i]%2==0:
        fibopar.append(fibo[i]);
        suma=suma+fibopar[j]
        j+=1
    if i == a:
        break
    

print("\n La lista de los fibonacci es:\n",fibo)

print("\n La lista de los fibonacci par es:\n",fibopar)

print("\n La suma de todos los numeros de fibonacci par es :",suma)
