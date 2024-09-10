print ("has sobrado funciones")
#aqui se escriben las funciones 

#suma
def suma_ab(a,b):
    s=a+b
    return s

#resta
def resta_cd(c,d):
    r=c-d
    return r

#multiplicacion 
def multiplicacion_ef(e,f):
    m=e*f
    return m

#divicion
def divicion_gh(g,h):
    d=g/h
    return d

#llamadas funciones 

print("calculando suma")
n1=int(input("ingresa el primer nuevo"))
n2=int(input("ingresa el segundo numero"))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es: {suma}")

print("calculando resta")
n3=int(input("ingresa el primer nuevo"))
n4=int(input("ingresa el segundo numero"))
resta=resta_cd(n3,n4)
print(f"la resta de {n3} - {n4} es: {resta}")

print("calculando multiplicacion")
n5=int(input("ingresa el primer nuevo"))
n6=int(input("ingresa el segundo numero"))
multiplicacion=multiplicacion_ef(n5,n6)
print(f"la multiplicacion de {n5} * {n6} es: {multiplicacion}")

print("calculando divicion")
n7=int(input("ingresa el primer nuevo"))
n8=int(input("ingresa el segundo numero"))
divicion=divicion_gh(n7,n8)
print(f"la divicion de {n7} / {n8} es: {divicion}")