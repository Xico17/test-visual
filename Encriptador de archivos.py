
def encriptar(texto):
    print("el texto a encriptar es " + texto)
    textoFinal=""
    for letra in texto:
        textoFinal += letra + "x"
    return textoFinal   


def desencriptar(texto):
    print("el taxto encriptado es " + texto)
    textoFinal=""
    contador=0
    for letra in texto:
        if contador % 2 == 0:
         textoFinal += letra 
        contador += 1

     
    print("El texto desencriptado es " + textoFinal)    


# encriptar("prueba de texto")
# desencriptar("pxrxuxexbxax xdxex xtxexxxtxox")

def encriptarArchivo():
    archivo=open("texto.txt","r")
    texto=archivo.read()
    archivo.close()
    textoEncriptado=encriptar(texto)

    archivo= open("texto.txt", "w")
    archivo.write(textoEncriptado)
    archivo.close()
    
encriptarArchivo()



