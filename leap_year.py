def leap_year():
    year = int(input("Ingrese un año: "))
    
    result = (not year % 400) or (not year % 4 and year % 100)
    
    print( f" El año {year}{""if result else "no "}es bisiesto")
