# Calculo de imc 
# IMC=PESO/(Alturaxaltura)
# entre 20 y 25: normal 
# entre 26 y 30: sobrepeso
# > de 30 : obesidad 

# FUNCIONES
# def calcularIMC (peso,alturaEnMetros):
#    imc =peso/(altura*alturaEnMetros)
#    return imc 

# peso=float(input("ingrese su peso en kg"))
# alturaEnMetros=float(input("ingrese su altura en m"))
# imc =calcularIMC(peso,alturaEnMetros)
# print("Tu imc es " + str(imc))
# if imc<20:
#     print("Estado de delgadez")
# if imc>=20 and imc<=25:
#     print("Estado normal")
# if imc>25 and imc<=30:
#     print("Estado de sobrepeso")
# if imc>30:
#     print("Estado de Obesidad")

# BUCLE WHILE
# contador=0
# while contador <=5:
#     contador=contador+1
#     if contador == 3:
#         continue 
#     print("el valor de contador es: " +str(contador))

# CHAT CON EMOJIS
# seguirChateando= True 
# while seguirChateando:
#     texto=input(">")
#     if texto=="salir":
#         seguirChateando= False
          
#     texto=texto.replace(":)","😀")
#     texto=texto.replace(":(","😭")
#     texto=texto.replace(">:/","😠")
#     print(texto)

# ARREGLO

# arreglo=["platano","manzana","pera","uva"]
# for fruta in arreglo:
#     if fruta.endswith("a"):
#      print("La fruta es: " + fruta)

# arreglo.reverse()
# arreglo.remove("manzana")
# arreglo.append()
# arreglo.insert(3,"guanabana")
# arreglo.pop(3)

# texto="hola mundo"
# for letra in texto:
#     print (letra)
   
# for numero in range (10):
#     if numero >3:
#      print (numero)7

#DICCIONARIOS 

# diccionario= {
#     "Programar":"generar un codigo util",
#     "POD":"Programacion orientada a objetos",
#     "MVC":"Modelo vista controlador"
# }
# print(diccionario["MVC"])

# numeros= {
#     "0":"cero",
#     "1":"uno",
#     "2":"dos",
#     "3":"tres",
#     "4":"cuatro",
#     "5":"cinco",
#     "6":"seis",
#     "7":"siete",
#     "8":"ocho",
#     "9":"nueve"
# }
# texto=input("ingrese un numero")
# textofinal=""
# for num in texto:
#     textofinal += numeros[num] + " " 
# print(textofinal)

#ARCHIVOS DE TEXTO
archivo=open("texto.txt","w")
archivo.write("prueba de guardado en el archivo")
archivo.write("hola")
archivo.close()

archivo= open("texto.txt", "r")
print(archivo.read())





