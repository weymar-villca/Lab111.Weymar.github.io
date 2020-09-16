"""EJERCICIO3 WEYMAR VILLCA ORUÑO"""
hora=int(input("intro hora: "))
min=int(input("intro min: "))
seg=int(input("intro seg: "))
sumseg=int(input("cantidad de seg de suma: "))
hora1=hora*60*60
hora2=hora1+sumseg
min1=min*60
min2=min1+sumseg
seg1=seg+sumseg
resultado=hora1+min1+sumseg
print("la suma de hora mas el seg: ",min2,"seg")
print("la suma de min mas el seg: ",min2,"seg")
print("la suma de seg mas sumseg: ",seg1,"seg")
print("resultado total en segundos: ",resultado,"seg")