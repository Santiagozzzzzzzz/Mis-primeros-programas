#Determinar el pago mensual M de un pr ́estamo simple con capital P ,tasa de inter ́es mensual r, y n ́umero de pagos n

p=float(input("Capital:  "))
r=float(input("tasa de interes:  "))
n=float(input("periodo:  "))

pagomensual=(p*r/1-(1+r)**-n)