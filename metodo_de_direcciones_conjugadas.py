import sympy as sp
import platform
import os

def limpiar_pantalla():
    if platform.system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def solicitarDirecciones():
#Número de direcciones y sus valores
    n_direcciones = int(input("Introduce el número de direcciones: "))
    
    #Validación de parámetro ingresado
    while n_direcciones < 1:
        n_direcciones = int(input("Por favor ingresa un valor válido (mayor a cero): "))
    
    #Guardado de arreglo de direcciones especificados por el usuario
    S = []
    for i in range(n_direcciones):
        x1 = float(input("Ingrese el x1 de la dirección: "))
        x2 = float(input("Ingrese el x2 de la dirección: "))
        S.append(sp.Matrix([x1,x2]))
    return S



def solicitarPuntoInicial():
#Valores del punto inicial: 
    
    x = float(input("Ingresa x del punto inicial: "))
    y = float(input("Ingresa y del punto inicial: "))
    return [x,y]



def minimizar(S,p,i):
#Cálculos según los parámetros recibidos

    #Inicialización de las variables y lambda (t)
    t, x, y = sp.symbols("t x y")
    
    # Fórmula: (A,B) + TS
    vector_sust =  p[i]+ t*S[i]


    #Fórmula cuadrática: x1 - x2 + 2x1^2 + 2 (x1) * (x2) + x^2 
    f_cuadratica = (x - y + 2 * x**2  + 2 * x * y + y**2).subs({x: vector_sust[0], y: vector_sust[1]})

    #Cálculo de las derivadas
    derivada = f_cuadratica.diff(t)
    
    segundaDerivada = derivada.diff(t)
    
    #Si f'' < 0 no se puede resolver
    if segundaDerivada < 0:
        print("No se puede resolver. No se está minimizando.")
        exit()

    #Despeje de lambda (t)
    valor_t = sp.solve(derivada, t)
    p.append(sp.Matrix(vector_sust.subs(t, valor_t[0])))


def mostrarEnPantalla(p):
    limpiar_pantalla()
    print("_________________________________________________________________________")
    print(f"\nLos puntos conjugados han sido:\n")
    for i in range(1,len(p)):
        sp.pprint(p[i])
        print(" ")
    print(f"\nPor tanto, el punto mínimo es:\n") 
    sp.pprint(p[-1])
    
    
def metodoDeDireccionesConjugadas():
    
    #Lista de direcciones
    S = solicitarDirecciones()
    
    
    #Lista de matrices de los puntos
    p = []
    p.append(sp.Matrix(solicitarPuntoInicial()))
    for i in range(len(S)):
        minimizar(S, p,i)
    
    #Cálculo de la dirección final: x3 - x1
    Sfinal = p[-1] - p[1]

    S.append(Sfinal)
    minimizar(S, p, -1)
    mostrarEnPantalla(p)

def main():
    metodoDeDireccionesConjugadas()

if __name__ == "__main__":
    main()
