def leap_year():
    año = int(input("Ingrese un año: "))
    
    if año%100==0:
        if año%400==0:
            print(f"{año} es un año bisiesto.")

    elif año%4==0:
        print(f"{año} es un año bisiesto.")
        
    else:
        print(f"{año} no es un año bisiesto.")
