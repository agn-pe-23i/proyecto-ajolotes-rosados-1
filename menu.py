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
            return
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
        # Busca y elimina productos utilizando la función buscar_y_eliminar_prodcuto del módulo catalogo_utils
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
            return
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

liiiist = [
    {'Pelicula': [
        {'Titulo': 'Spider Man: de regreso a casa', 'Actor/a principal': '  Tom Holland.', 'Director/a': 'Jon Watts', 'Año': '2017', 'Costo Venta': '233', 'Costo Renta': '50'}, 
        {'Titulo': 'Spider Man: Far From Home', 'Actor/a principal': 'Tom Holland.', 'Director/a': 'Jon Watts', 'Año': '2019', 'Costo Venta': '333', 'Costo Renta': '210'}, {'Titulo': 'Spider Man: No Way Home', 'Actor/a principal': 'Tom Holland', 'Director/a': 'Jon Watts', 'Año': '2020', 'Costo Venta': '661', 'Costo Renta': '211'}, 
        {'Titulo': 'spider man into the spider-verse 2', 'Actor/a principal': 'Peter Ramsey', 'Director/a': 'Bob Persichetti', 'Año': '2023', 'Costo Venta': '1000', 'Costo Renta': '500'}, 
        {'Titulo': 'guardianes de la galaxia', 'Actor/a principal': 'Peter Quill', 'Director/a': 'James Gunn', 'Año': '2023', 'Costo Venta': '700', 'Costo Renta': '455'}, 
        {'Titulo': 'Shrek', 'Actor/a principal': 'Shrek', 'Director/a': 'Andrew Adamson', 'Año': '200', 'Costo Venta': '666', 'Costo Renta': '212'}
        ]
     }, 
     {'Serie': [
         {'Titulo': 'como si fuera a la primera ves', 'Actor/a principal': 'Adam Sandler', 'Director/a': 'Peter Segal', 'Temporadas': '5', 'Costo Venta': '1000', 'Costo Renta': '500'}, 
         {'Titulo': 'Son como niños', 'Actor/a principal': 'Kevin James', 'Director/a': 'Dennis Dugan', 'Temporadas': '4', 'Costo Venta': '700', 'Costo Renta': '300'}, 
         {'Titulo': 'Yo los Declaro Marido y Larry', 'Actor/a principal': 'Adam Sandler', 'Director/a': 'Dennis Dugan', 'Temporadas': '1', 'Costo Venta': '566', 'Costo Renta': '210'}, 
         {'Titulo': 'Grimm', 'Actor/a principal': 'David Giuntoli', 'Director/a': 'Ever After High', 'Temporadas': '6', 'Costo Venta': '1000', 'Costo Renta': '500'}, 
         {'Titulo': 'Sexo/Vida', 'Actor/a principal': 'Sarah Shahi', 'Director/a': 'Rotten Tomatoes', 'Temporadas': '2', 'Costo Venta': '800', 'Costo Renta': '400'}, 
         {'Titulo': 'Chucky', 'Actor/a principal': 'Jennifer Tilly', 'Director/a': 'George Donald Mancini', 'Temporadas': '2', 'Costo Venta': '1000', 'Costo Renta': '500'}, 
         {'Titulo': 'Stranger Things', 'Actor/a principal': 'Millie Bobby Brown', 'Director/a': 'Matt Duffer Ross Duffer Shawn Levy', 'Temporadas': '4', 'Costo Venta': '1000', 'Costo Renta': '500'}
         ]
      }, 
      {'Documental': [
          {'Titulo': 'Nuestro padre', 'Director/a': 'donald cline', 'Tema': 'medicina', 'Año': '2022', 'Costo Venta': '1000', 'Costo Renta': '500'}, 
          {'Titulo': 'El estafador de Tinder', 'Director/a': 'Simon Leviev', 'Tema': 'casos de la vida real', 'Año': '2023', 'Costo Venta': '1000', 'Costo Renta': '500'}, 
          {'Titulo': 'Hongos fantasticos', 'Director/a': 'Paul Stamets', 'Tema': 'drogadiccion', 'Año': '2020', 'Costo Venta': '700', 'Costo Renta': '300'}, 
          {'Titulo': 'Misha y los lobos', 'Director/a': 'Misha Defonseca', 'Tema': 'informativo', 'Año': '2021', 'Costo Venta': '900', 'Costo Renta': '450'}, 
          {'Titulo': 'La vida en la escuela', 'Director/a': 'axel juarez', 'Tema': 'casos de la vida real', 'Año': '2023', 'Costo Venta': '1000', 'Costo Renta': '500'}
          ]
       }, 
       {'Evento deportivo en vivo': [
           {'Titulo': 'UEFA Champions League ', 'Deporte': 'Fútbol', 'Fecha': '10/06/2023', 'Hora': '13:00', 'Lugar': 'paris', 'Costo Venta': '1000'}, 
           {'Titulo': 'Super Bowl', 'Deporte': 'Fútbol Americano', 'Fecha': '10/09/2023', 'Hora': '14:00', 'Lugar': 'Estados unidos', 'Costo Venta': '1000'}, 
           {'Titulo': 'Finales de la NBA', 'Deporte': 'Basketball', 'Fecha': '10/02/2023', 'Hora': '12:00', 'Lugar': 'Estados Unidos', 'Costo Venta': '1000'}, 
           {'Titulo': 'Mundial de Fórmula 1', 'Deporte': 'Carreras', 'Fecha': '1/02/2023', 'Hora': '17:00', 'Lugar': 'italia', 'Costo Venta': '1000'}
           ]
        }
    ]