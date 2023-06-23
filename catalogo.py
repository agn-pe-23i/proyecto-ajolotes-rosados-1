import menu as UserInterface
catalogo = None


def main():
    """
        Menu principal el cual despliega las opciones del programa (agregar/eliminar/buscar un prodcuto y mostrar/cargar/guardar un catalogo)
    """
    global catalogo
    while True:
        # Obtiene las opciones del menu
        opciones = UserInterface.opciones_menu(0)
        # Muestra el titulo del menu "Menu Principal" y las opciones disponibles
        UserInterface.plantilla_menu('Menú Principal', opciones)
        # Permite al usuario seleccionar una opcion
        seleccion, _ = UserInterface.seleccion_opciones(opciones)
        if seleccion == 1:
            #Llama a la funcion agregar_producto(catalogo) si la opcion seleccionada es 1
            UserInterface.agregar_producto(catalogo)
        elif seleccion == 2:
            # Llama a la función buscar_producto(catalogo) si la opción seleccionada es 2
            UserInterface.buscar_producto(catalogo)
        elif seleccion == 3:
            # Llama a la función eliminar_producto(catalogo) si la opción seleccionada es 3
            UserInterface.eliminar_producto(catalogo)
        elif seleccion == 4:
            # Llama a la función mostrar_catalogo(catalogo) si la opción seleccionada es 4
            UserInterface.mostrar_catalogo(catalogo)
        elif seleccion == 5:
            # Verifica si el catálogo ha sido cargado y llama a la función cargar_catalogo() si no ha sido cargado antes
            if catalogo is None:
                print('En caso de no contar con un archivo, por favor solo ponga el nombre deseado para crear uno.')
                catalogo = UserInterface.cargar_catalogo()
            else:
                print('El catálogo ya ha sido cargado.')
        elif seleccion == 6:
            # Llama a la función guardar_catalogo(catalogo) para guardar el catálogo en un archivo
            # Luego, imprime "Hasta luego" y finaliza el bucle
            UserInterface.guardar_catalogo(catalogo)
            print('Hasta luego')
            break
        elif seleccion == 7:
            # Finaliza el bucle y termina la ejecución del programa si la opción seleccionada es 7
            break


main()