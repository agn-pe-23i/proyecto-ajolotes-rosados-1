import catalogo_utils

def seleccion_opciones(opciones):
    """
    Solicita al usuario que seleccione una opción numérica y valida la entrada.
    """
    # Variable de control para el bucle while
    option = False
    while not option:
        # Solicitar al usuario que seleccione una opción numérica
        selection = input('Seleccione una opción (num): ')
        # Verificar si la selección es un dígito y está dentro del rango de opciones
        if selection.isdigit() and int(selection) > 0 and int(selection) <= len(opciones):
            # Si la selección es válida, se marca la opción como verdadera y se sale del bucle
            option = True
        else:
            # Si la selección es inválida, se muestra un mensaje de error y se solicita nuevamente
            print('Opción inválida, intente de nuevo: ')
    # Convertir la selección a entero y devolver la opción seleccionada junto con su valor
    selected_option = int(selection)
    return selected_option, opciones[selected_option]


def imprimir_menu(menu):
    """
    Imprime el menú
    """
    # Iterar por cada clave y valor
    for key, value in menu.items():
        # Imprimir en un formato legible
        print(key, value)


def plantilla_menu(titulo, opciones=None):
    """
    Imprime una plantilla de menú con un título y las opciones disponibles.
    """
    # Titulo del menu
    print(f'~{titulo}~')
    # Si hay opciones, se imprimen
    if opciones is not None:
        imprimir_menu(opciones)
    return


def opciones_menu(opcion):
    """
    Almacena y devuelve una lista de opciones correspondiente a la opción seleccionada
    """
    lista = [
        {1 : '~  Agregar un producto.', 
        2 : '~  Buscar un produto.', 
        3 : '~  Eliminar un producto.', 
        4 : '~  Mostrar catalogo.', 
        5 : '~  Cargar catalogo.', 
        6 : '~  Guardar catalogo.', 
        7 : '~  Salir.'}, 
        {1 : '~  Pelicula', 
        2 : '~  Serie', 
        3 : '~  Documental', 
        4 : '~  Evento deportivo en vivo',
        5 : '~  Regresar'}, 
        {1 : '~  Pelicula', 
        2 : '~  Serie', 
        3 : '~  Documental', 
        4 : '~  Evento deportivo en vivo',
        5 : '~  Todo',
        6 : '~  Regresar'}]
    return lista[opcion] # Regreso de diccionario correspondiente a la opcion solicitada


def verificar_catalogo_cargado(catalogo):
    """
    Verifica si el catálogo ha sido cargado previamente.
    Si el catalogo no ha sido cargado, lanza un aviso (exepcion)
    """
    # Si no hay catalogo, avisar de ello y terminar la ejecucucion con raise Exception
    if catalogo is None:
        raise Exception("¡El catálogo no ha sido cargado! Por favor, carga el catálogo antes de acceder a esta opción.")


def agregar_producto(catalogo):
    """
    Agrega un producto al catálogo.

    Verifica si el catálogo ha sido cargado. 
    Despliega un menú y utiliza la opción seleccionada como argumento para la función correspondiente en el módulo de utilidades.
    """
    try:
        # Verifica si el catálogo ha sido cargado antes de agregar un producto
        verificar_catalogo_cargado(catalogo)
        # Obtiene las opciones del menú
        opciones = opciones_menu(1)
        # Muestra el título del menú y las opciones disponibles
        plantilla_menu('Menu Agregar Producto', opciones)
        # Solicita al usuario que seleccione una opción y obtiene la opción seleccionada junto con su valor
        seleccion, opcion_seleccionada = seleccion_opciones(opciones)
        if seleccion != 5:
            valor_opcion = opcion_seleccionada.strip('~ ')
            # Crea un nuevo producto utilizando la función diccionario_agregar_producto del módulo catalogo_utils
            producto = catalogo_utils.diccionario_agregar_producto(valor_opcion)
            # Agrega el producto al catálogo utilizando la función agregar_producto_catalogo del módulo catalogo_utils
            catalogo = catalogo_utils.agregar_producto_catalogo(catalogo, valor_opcion, producto)
        else:
            # Si se selecciona la opción 5, vuelve al menú principal
            principal()
    except Exception as e:
        # Captura y muestra cualquier excepción generada durante la ejecución
        print(str(e))


def eliminar_producto(catalogo):
    """
    Elimina un producto del catálogo.

    Verifica si el catálogo ha sido cargado. 
    Despliega un menú y utiliza la opción seleccionada como argumento para la función correspondiente en el módulo de utilidades.
    """
    try:
        # Verifica si el catálogo ha sido cargado antes de eliminar un producto
        verificar_catalogo_cargado(catalogo)
        # Muestra el título del menú para eliminar un producto
        plantilla_menu('Eliminar un producto')
        # Solicita al usuario que ingrese palabras clave separadas por espacios
        palabras_clave = input('Ingrese palabras clave separadas por espacios: ').split()
        # Obtiene una lista de todos los productos del catálogo utilizando la función obtener_lista_productos del módulo catalogo_utils
        lista_productos = catalogo_utils.obtener_lista_productos(catalogo)
        # Busca y elimina productos utilizando la función buscar_serie_recursivo del módulo catalogo_utils
        catalogo_utils.buscar_y_eliminar_producto(lista_productos, palabras_clave, catalogo)
    except Exception as e:
        # Captura y muestra cualquier excepción generada durante la ejecución
        print(str(e))


def buscar_producto(catalogo):
    """
    Realiza una búsqueda de productos en el catálogo.

    Verifica si el catálogo ha sido cargado. Despliega un menú y llama a la función correspondiente en el módulo de utilidades.
    """
    try:
        # Verifica si el catálogo ha sido cargado antes de realizar una búsqueda de productos
        verificar_catalogo_cargado(catalogo)
        # Muestra el título del menú para buscar un producto
        plantilla_menu('Buscar un producto')
        # Llama a la función de búsqueda de productos en el catálogo del módulo catalogo_utils
        catalogo_utils.busqueda_producto_titulo(catalogo)
    except Exception as e:
        # Captura y muestra cualquier excepción generada durante la ejecución
        print(str(e))


def mostrar_catalogo(catalogo):
    """
    Muestra el catálogo de productos.

    Verifica si el catálogo ha sido cargado. Despliega un menú y utiliza la opción seleccionada como argumento para la función correspondiente en el módulo de utilidades.
    """
    try:
        # Verifica si el catálogo ha sido cargado antes de mostrar el catálogo
        verificar_catalogo_cargado(catalogo)
        # Obtiene las opciones del menú para mostrar el catálogo
        opciones = opciones_menu(2)
        # Muestra el título del menú para mostrar el catálogo
        plantilla_menu('Menu Mostrar Catálogo', opciones)
        # Obtiene la opción seleccionada y su descripción utilizando la función seleccion_opciones()
        seleccion, _ = seleccion_opciones(opciones)
        if seleccion == 6:
            # Si la opción seleccionada es 6, regresa al menú principal
            principal()
        elif seleccion == 5:
            # Si la opción seleccionada es 5, muestra todos los productos del catálogo utilizando la función mostrar_productos() del módulo catalogo_utils
            catalogo_utils.mostrar_productos(catalogo)
        else:
            # Si la opción seleccionada no es 5 ni 6, obtiene la categoría correspondiente a la opción y muestra los productos de esa categoría utilizando la
            # función mostrar_productos() del módulo catalogo_utils
            categoria = opciones[seleccion].strip('~ ')
            catalogo_utils.mostrar_productos(catalogo, categoria)
    except Exception as e:
        # Captura y muestra cualquier excepción generada durante la ejecución
        print(str(e))


def cargar_catalogo():
    """
    Carga el catálogo almacenado en un archivo.

    Verifica si es catalogo esta cargado y llama a la funcoin correspondiente en el modulo de utilidades
    """
    # Muestra el título del menú "Cargar catálogo"
    plantilla_menu('Cargar catálogo')
    # Llama a la función del módulo catalogo_utils para cargar el catálogo desde un archivo
    catalogo = catalogo_utils.cargar_catalogo_archivo()
    # Devuelve el catálogo cargado
    return catalogo


def guardar_catalogo(catalogo):
    """
    Guarda el catálogo en un archivo.

    Verifica si es catalogo esta cargado y llama a la funcoin correspondiente en el modulo de utilidades
    """
    # Verifica si el catálogo ha sido cargado antes de guardar el catálogo
    verificar_catalogo_cargado(catalogo)
    # Muestra el título del menú "Guardar catálogo"
    plantilla_menu('Guardar catálogo')
    # Llama a la función del módulo catalogo_utils para guardar el catálogo en un archivo
    catalogo_utils.guardar_catalogo_archivo(catalogo)


def principal(catalogo):
    """
        Menu principal el cual despliega las opciones de manipulacion de catalogo
    """
    while True:
        # Obtiene las opciones del menú
        opciones = opciones_menu(0)
        # Muestra el título del menú "Menú Principal" y las opciones disponibles
        plantilla_menu('Menú Principal', opciones)
        # Permite al usuario seleccionar una opción
        seleccion, _ = seleccion_opciones(opciones)
        if seleccion == 1:
            # Llama a la función agregar_producto(catalogo) si la opción seleccionada es 1
            agregar_producto(catalogo)
        elif seleccion == 2:
            # Llama a la función buscar_producto(catalogo) si la opción seleccionada es 2
            buscar_producto(catalogo)
        elif seleccion == 4:
            # Llama a la función mostrar_catalogo(catalogo) si la opción seleccionada es 4
            mostrar_catalogo(catalogo)
        elif seleccion == 3:
            # Llama a la función eliminar_producto(catalogo) si la opción seleccionada es 3
            eliminar_producto(catalogo)
        elif seleccion == 5:
            # Verifica si el catálogo ha sido cargado y llama a la función cargar_catalogo() si no ha sido cargado antes
            if catalogo is None:
                print('En caso de no contar con un archivo, por favor solo ponga el nombre deseado para crear uno.')
                catalogo = cargar_catalogo()
            else:
                print('El catálogo ya ha sido cargado.')
        elif seleccion == 6:
            # Llama a la función guardar_catalogo(catalogo) para guardar el catálogo en un archivo
            # Luego, imprime "Hasta luego" y finaliza el bucle
            guardar_catalogo(catalogo)
            print('Hasta luego')
            break
        elif seleccion == 7:
            # Finaliza el bucle y termina la ejecución del programa si la opción seleccionada es 7
            break
