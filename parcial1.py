print("hola mundo")
#maquina de funciones 
def f(x):
  f_x= -2*x+34
  return f_x
  
y=f(10)

print (y)

def f(x):
  f_x= (x-2)**2
  return f_x
  
y=f(10)

print (y)


#código coding rush
#OPCIÓN A 
print("¿A qué temperatura estamos?")
print("A 30 grados celcius ")
fahrenheit=30*(9/5)+32
print("Eso en farenheit es",fahrenheit)
kelvin=30+273.15
print("Y en kelvin sería",kelvin)



#ejercicios de repaso
def descuento():
  print("Inserta costo de la comida:")
  costo = input()
  print("Porcentaje de propina %:")
  porcentaje = input() 
  resultado = int (costo) * int (porcentaje) / 100 
  print("La cantidad de propina es:",resultado)
  montototal = int(resultado) + int(costo)
  print("Por lo tanto el monto total a pagar es:",montototal)

descuento()

#2 
print ("Ingresar la cantidad en dólares:")
cantidad=input()
print("Cuanto vale cada dolar en peso:")
valor=input()
resultado= float(cantidad)*float(valor)
print("Este es el resultado:", resultado)



#código examen parcial 
#OLGA SOFIA ARANDA AGUILAR A00574093
print("Ingresa el número de adultos:")
adultos=input() #
print("Ingresa el número de niños:")
niños=input()  #
totalsA=float(adultos)*25 
totalsN=float(niños)*20

totalsA=float(adultos)*25 
totalsN=float(niños)*20
totals=float(totalsA)+float(totalsN)
print("Este es el total en pesos de sillas:",totals)
mesaA=float(adultos)*17
print("El total en pesos de mesa de adultos:",mesaA)
mesaN=float(niños)*17
print("El total en pesos de mesa de niño",mesaN)
cuantasmesasA=float(mesaA)/170
cuantasmesasN=float(mesaN)/170
totaldecarpas=float(cuantasmesasA)+float(cuantasmesasN)
pesocarpa=float(totaldecarpas)*630
print("El total de carpas en pesos son:",pesocarpa)
subtotal=float(pesocarpa)+float(mesaA)+float(mesaN)
print("El subtotal es",subtotal)
impuestos=float(subtotal)*0.16
print("Cantidad de impuestos",impuestos)
impuestostotal=float(subtotal)+float(impuestos) #
print("Total con impuestos",impuestostotal)
print("De cuanto es tu descuento:")
descuento=input()
descuentoenpesos=float(impuestostotal)*float(descuento)/100
print("Cantidad de descuento en pesos:",descuentoenpesos)
total=float(impuestostotal)-float(descuentoenpesos)
print("total con descuento",total)


