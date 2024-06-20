import Funciones as fn
compras=[]
while True:
    try:
        print("     Menu principal")
        print("")
        print("1. Registrar pedido")
        print("2. Listar los todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        opc=int(input("Ingrese su opción: "))
        if opc == 1:
            fn.registrar_pedidos(compras)
        elif opc == 2:
            fn.listar_pedidos(compras)
        elif opc == 3:
            fn.imprimir_planilla(compras)
        else:
            print("Saliendo del programa")
            break
    except:
        print("Ingrese dato válido")