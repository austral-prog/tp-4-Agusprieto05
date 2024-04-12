def leap_year():
    año = int(input("Ingrese un año: "))
    
    result = (not año % 400) or (not año % 4 and año % 100)
    
    print( f" El año {año}{""if result else "no "}es bisiesto")
