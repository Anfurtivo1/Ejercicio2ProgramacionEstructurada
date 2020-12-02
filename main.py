
def anadirTriangulo():
    nombreTriangulo="Triangulo ",contadorTriangulos
    coordenadaX=1
    coordenadaY=1
    longitud=1
    area=1
    coordenadaX=int(input("Indica la primera coordenada"))
    coordenadaY = int(input("Indica la segunda coordenada"))
    area=calcularArea(coordenadaX,coordenadaY)
    longitud=calcularLongitud(coordenadaX,coordenadaY)

    diccionarioTriangulos[nombreTriangulo]=coordenadaX,coordenadaY,area,longitud
    print(diccionarioTriangulos)


def calcularArea(X,Y):
    area=(X*Y)/2
    return area

def calcularLongitud(X,Y):
    longitud=1

    return longitud

if __name__ == '__main__':
    contadorTriangulos = 1
    diccionarioTriangulos={}
    mensaje="s"
    while(mensaje=="s"):
        anadirTriangulo()
        contadorTriangulos = contadorTriangulos + 1
        mensaje=input("¿Quieres añadir mas triangulos?")