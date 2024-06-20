sectores=["centro","norte","sur"]
def registrar_pedidos(compras):
    try:
        nombre=input("Ingrese nombre y apellido del comprador: ")
        direccion=input("Ingrese dirección del comprador: ")
        sector=input("Ingrese sector del comprador: ").lower()
        while sector not in sectores:
            print("Sector no válido")
            sector=input("Ingrese sector del comprador: ").lower()  
        pequeno=int(input("Ingrese cuantos paquetes pequeños desea comprar: "))
        mediano=int(input("Ingrese cuantos paquetes medianos desea comprar: "))
        grande=int(input("Ingrese cuantos paquetes grandes: "))
                
    except:
        print("Ingrese solo números")
        return

    compras.append({
            "nombre":nombre,
            "direccion":direccion,
            "sector":sector,
            "pequeno":pequeno,
            "mediano":mediano,
            "grande":grande
        })
    print("El registro se ha realizado exitosamente")

def listar_pedidos(compras):
    for i in compras:
        print(i)
        return

def imprimir_planilla(compras):
    sector_imprimir=input("Ingrese uno de los sectores para imprimir la planilla o bien presione ENTER para imprimirlas todas: ")
    if sector_imprimir=="":
        lista=compras
        nombre_archivo="Planilla_todos.txt"
    elif sector_imprimir in sectores:
        lista=[]
        for paquete in compras:
            if paquete["sector"]==sector_imprimir:
                lista.append(paquete)
        nombre_archivo=f"Planilla_{sector_imprimir}.txt"
    else:
        print("Ingrese un sector válido")
    
    with open(f"{nombre_archivo}","w") as archivo:
        for pedido in lista:
            archivo.write(f"Nombre y apellido: {pedido["nombre"]}\n"),
            archivo.write(f"Dirección: {pedido["direccion"]}\n"),
            archivo.write(f"Sector: {pedido["sector"]}\n"),
            archivo.write(f"Pequeños: {pedido["pequeno"]}\n"),
            archivo.write(f"Medianos: {pedido["mediano"]}\n"),
            archivo.write(f"Grandes: {pedido["grande"]}\n\n")
    

        
