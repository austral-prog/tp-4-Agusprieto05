import math
def line():
    print("TO DO")
    coef1 = float(input("Ingrese el coeficiente A: "))
    coef2 = float(input("Ingrese el coeficiente B: "))
    coefX1 = float(input("Ingrese el coeficiente X1: "))
    coefX2 = float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {coef1}")
    print(f"El coeficiente B de su ecuación de la recta es: {coef2}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coefX1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coefX2}")

    print("Para la siguiente ecuación: ")
    print(f"\t{coef1}X + {coef2}")
    print("")
    coefY1 = coef1 * coefX1 + coef2
    coefY2 = coef1 * coefX2 + coef2
    
    print("Dados los siguientes puntos:")
    print(f"\t P1({coefX1}, {coefY1})")
    print(f"\t P2({coef1}, {coefY2})")

 
 
    line1_0 = math.pow(coefY1,2) + math.pow(coefX1,2)
    line1_1 = math.sqrt(line1_0)

    line2_0 = math.pow(coefY2,2) + math.pow(coefX2,2)
    line2_1 = math.sqrt(line2_0)
    
    distance = line1_1 + line2_1
    
    print(f"La distancia entre ellos : {distance}")
