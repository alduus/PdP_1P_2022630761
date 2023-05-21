import math
import random
#ADAIR LOPEZ SANCHEZ
#ALDO ESCAMILLA RESENDIZ 
#LOBARDO YAÑEZ MARTINEZ
#DIEGO CASTILLO REYES
class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        dz = self.z - otro_punto.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

def encontrar_par_mas_cercano(puntos):
    par_mas_cercano = (None, None)
    distancia_minima = float('inf')

    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            distancia = puntos[i].distancia(puntos[j])
            if distancia < distancia_minima:
                distancia_minima = distancia
                par_mas_cercano = (puntos[i], puntos[j])

    return par_mas_cercano

# Ejemplos proporcionados
P1 = Punto3D(2, 3, 4)
P2 = Punto3D(-2, 3, 9)
P3 = Punto3D(0.5, 0.3, 0.9)

# Generar 17 puntos aleatorios adicionales
puntos = [P1, P2, P3]
for _ in range(17):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    z = random.uniform(-10, 10)
    punto = Punto3D(x, y, z)
    puntos.append(punto)

# Encontrar el par más cercano
par_cercano = encontrar_par_mas_cercano(puntos)

# Imprimir el resultado
if par_cercano[0] is not None and par_cercano[1] is not None:
    print("El par más cercano es:")
    print("P1 =", (par_cercano[0].x, par_cercano[0].y, par_cercano[0].z))
    print("P2 =", (par_cercano[1].x, par_cercano[1].y, par_cercano[1].z))
else:
    print("No se encontró un par de puntos.")
