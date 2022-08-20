#Input del usuario
pesoscol = input("¿Cuantos pesos colombianos tienes? ")
pesoscol = float(pesoscol)

#Declaracion de valores
valor_dolar = 3850      # usd to cop
valor_euro = 4099.63    # google: euro to cop
valor_cake = 11370.07   # [Crypto] PancakeSwap to Colombian Peso / https://www.coinbase.com/converter/cake/cop
valor_btc = 75968332.82 # [Crypto] BTC to COP / https://cuex.com/en/btc-cop

#Calculo valor dolar
dolares = pesoscol / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

#Calculo Valor Euro
euros = pesoscol / valor_euro
euros = round(euros, 2)
euros = str(euros)

#Calculo Cantidad de CAKE
cakes = pesoscol / valor_cake
cakes = round(cakes, 4)
cakes = str(cakes)

#Calculo Bitcoin
btcs = pesoscol / valor_btc
btcs = round(btcs, 9)
btcs = str(btcs)

#Prints
print("Tienes US$ " + dolares + " dólares")
print("Tienes € " + euros + " Euros")
print("Tienes: " + cakes + " CAKE")
print("Tienes: " + btcs + " Bitcoins")
