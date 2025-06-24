def menu():
    print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.- Mostrar stock de funciones.")
    print("4.- Salir.")

def mostrar_stock(stock):
    print("\n=== Stock de funciones ===")
    print(f"Función 1: Cats Día Viernes - Disponibles: {stock['viernes']['disponibles']} | Vendidas: {stock['viernes']['vendidas']}")
    print(f"Función 2: Cats Día Sábado - Disponibles: {stock['sabado']['disponibles']} | Vendidas: {stock['sabado']['vendidas']}")

def comprar_entrada(clientes, stock):
    nombre = input("Ingrese nombre de comprador: ").strip()
    if nombre in clientes:
        print("El nombre de comprador ya existe. No puede comprar otra entrada.")
        return

    print("Seleccione función:")
    print("1.- Cats Día Viernes")
    print("2.- Cats Día Sábado")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        funcion = "viernes"
    elif opcion == "2":
        funcion = "sabado"
    else:
        print("Opción inválida.")
        return

    if stock[funcion]["disponibles"] > 0:
        stock[funcion]["disponibles"] -= 1
        stock[funcion]["vendidas"] += 1
        clientes[nombre] = funcion
        print("Entrada registrada exitosamente.")
    else:
        print("No hay entradas disponibles para esa función.")

def cambiar_funcion(clientes, stock):
    nombre = input("Ingrese su nombre: ").strip()
    if nombre not in clientes:
        print("No se encuentra este comprador.")
        return

    actual = clientes[nombre]
    nueva = "sabado" if actual == "viernes" else "viernes"
    print(f"Actualmente tiene entrada para el día {'Viernes' if actual == 'viernes' else 'Sábado'}.")
    resp = input(f"¿Desea cambiar a {'Sábado' if nueva == 'sabado' else 'Viernes'}? (s/n): ").strip().lower()
    if resp != "s":
        print("No se realizó el cambio de función.")
        return

    if stock[nueva]["disponibles"] > 0:
        stock[actual]["vendidas"] -= 1
        stock[actual]["disponibles"] += 1
        stock[nueva]["disponibles"] -= 1
        stock[nueva]["vendidas"] += 1
        clientes[nombre] = nueva
        print(f"Función cambiada exitosamente a {'Sábado' if nueva == 'sabado' else 'Viernes'}.")
    else:
        print(f"No hay disponibilidad en la función {'Sábado' if nueva == 'sabado' else 'Viernes'}.")

def main():
    stock = {
        "viernes": {"disponibles": 150, "vendidas": 0},
        "sabado": {"disponibles": 180, "vendidas": 0}
    }
    clientes = {}

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            comprar_entrada(clientes, stock)
        elif opcion == "2":
            cambiar_funcion(clientes, stock)
        elif opcion == "3":
            mostrar_stock(stock)
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    main()