from opciones import stock_marca, busqueda_precio, actualizar_precio
while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

    try:
        opt = int(input("Ingrese opción: "))
    except ValueError:
        print("Debe seleccionar una opción válida!!")
        continue

    if opt == 1:
        marca = input("Ingrese la marca: ")
        stock_marca(marca)

    elif opt == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros!!")
        busqueda_precio(p_min, p_max)

    elif opt == 3:
        while True:
            modelo = input("Ingrese modelo a actualizar: ")
            try:
                p = int(input("Ingrese precio nuevo: "))
                nuevoprecio = actualizar_precio(modelo, p)
                if nuevoprecio == True:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
            except ValueError:
                print("Precio no valido!!")
            continuar = input("Desea actualizar otro precio (s/n)?: ")
            if continuar == "si":
                break
            elif continuar == "no":
                continue

    elif opt == 4:
        print("Programa finalizado.")
        break
    
    else:
        print("Debe seleccionar una opción válida!!")

