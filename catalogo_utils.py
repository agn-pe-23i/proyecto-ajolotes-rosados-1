"""
Modulo utilidades de catalogo, las funciones se enfocan en realizar mayormente las manipulaciones del catalogo
"""

def crear_archivo_vacio(nombre_archivo):
    """
    Crea un catalogo vacio con un formato que maneja el sistema
    """
    with open(nombre_archivo, 'w') as archivo: # Se crea el archivo en modo escritura y se le guarda la estructura del catalogo
        estructura_catalogo = "[{'Pelicula': []},{'Serie': []},{'Documental' : []},{'Evento deportivo en vivo': []}]"
        archivo.write(estructura_catalogo)


def cargar_catalogo_archivo():
    """
    Carga el catalogo desde un archivo existente.

    Se solicita el nombre de archivo sin extension .txt.
    Si el archivo existe, lo lee y evalua su contenido como catalogo. 
    Si no existe, intenta crear uno usando la funcion crear_archivo_vacio()
    Se muestran mensajes informativos y de error en caso de existir alguno.
    """
    while True:
        # Solicitar al usuario el nombre del archivo a cargar
        nombre_archivo = input('Ingrese el nombre del archivo a cargar (sin la extensión .txt): ')
        # Comprobar si el nombre del archivo está vacío
        if nombre_archivo.strip() == '':
            print('El nombre del archivo no puede estar vacío. Intente de nuevo.')
            continue
        # Comprobar si el nombre del archivo incluye la extensión .txt
        if nombre_archivo.endswith('.txt'):
            print('No incluya la extensión .txt en el nombre del archivo.')
            continue
        # Construir el nombre completo del archivo
        nombre_archivo_completo = nombre_archivo + '.txt'
        try:
            # Intentar abrir el archivo en modo de lectura
            with open(nombre_archivo_completo, 'r') as archivo:
                # Leer el contenido del archivo
                contenido = archivo.read()
                # Evaluar el contenido como una expresión de Python
                catalogo = eval(contenido)
                # Imprimir mensaje de éxito
                print(f"El archivo '{nombre_archivo_completo}' se ha cargado correctamente.")
                # Devolver el catálogo cargado
                return catalogo 
        # Capturar excepción si el archivo no se encuentra
        except FileNotFoundError:
            print(f"Archivo '{nombre_archivo_completo}' no encontrado. Intentando crearlo...")
            # Crear un archivo vacío con el nombre proporcionado
            crear_archivo_vacio(nombre_archivo_completo)
            # Imprimir mensaje de éxito
            print(f"Archivo '{nombre_archivo_completo}' se ha creado con éxito.")
            print("Por favor cargue el archivo recién creado...")
        # Capturar cualquier otra excepción
        except Exception as e:
            print(f"Ocurrió un error al cargar el catálogo: {str(e)}")


def guardar_catalogo_archivo(catalogo):
    """
    Guarda el archivo existente.

    Se solicita el nombre del archivo donde se guardara el catalogo.
    Si el archivo existe y existen permisos de escritura, se sobreescribe el contenido.
    Se muestran mensajes informativos y de error en caso de existir alguno.
    """
    from os.path import exists
    while True:
        # Solicitar al usuario el nombre del archivo donde se guardará el catálogo
        nombre_archivo = input('Ingrese el nombre del archivo donde se guarde el catálogo (sin la extensión .txt): ')
        # Comprobar si el nombre del archivo está vacío
        if nombre_archivo.strip() == '':
            print('El nombre del archivo no puede estar vacío. Intente de nuevo.')
            continue
        # Comprobar si el nombre del archivo incluye la extensión .txt
        if nombre_archivo.endswith('.txt'):
            print('No incluya la extensión .txt en el nombre del archivo.')
            continue
        # Construir el nombre completo del archivo
        nombre_archivo_completo = nombre_archivo + '.txt'
        # Comprobar si el archivo no existe
        if not exists(nombre_archivo_completo):
            print(f"Archivo '{nombre_archivo_completo}' no encontrado.")
            continue
        try:
            # Intentar abrir el archivo en modo escritura con codificación utf-8
            with open(nombre_archivo_completo, 'w', encoding='utf-8') as archivo:
                # Escribir el catálogo en el archivo como una representación de cadena
                archivo.write(repr(catalogo))
            # Imprimir mensaje de éxito
            return print(f'Catálogo guardado con éxito en: "{nombre_archivo_completo}"')
        # Capturar excepción si no se tienen permisos para escribir en el archivo
        except PermissionError:
            print(f"No tiene permisos para escribir en el archivo '{nombre_archivo_completo}'. Intente de nuevo.")
        # Capturar cualquier otra excepción
        except Exception as e:
            print(f"Ocurrió un error al guardar el catálogo: {str(e)}")


def obtener_claves_categoria(categoria):
    """
    Obtiene las claves de la categoria solicitada.

    Busca la categoria en una lista de diccionarios y retorna las claves correspondientes.
    """
    lista = [
        {
            'Pelicula': ['Titulo', 'Actor/a principal', 'Director/a', 'Año', 'Costo Venta', 'Costo Renta']
        },
        {
            'Serie': ['Titulo', 'Actor/a principal', 'Director/a', 'Temporadas', 'Costo Venta', 'Costo Renta']
        },
        {
            'Documental': ['Titulo', 'Director/a', 'Tema', 'Año', 'Costo Venta', 'Costo Renta']
        },
        {
            'Evento deportivo en vivo': ['Titulo', 'Deporte', 'Fecha', 'Hora', 'Lugar', 'Costo Venta']
        }
    ]
    # Iterar sobre cada diccionario en la lista
    for categoria_dict in lista:
        # Comprobar si la categoría buscada está en el diccionario
        if categoria in categoria_dict:
            # Devolver la lista de claves correspondiente a la categoría seleccionada
            return categoria_dict[categoria]


def diccionario_agregar_producto(categoria):
    """
    Crea un diccionario de producto para una categoría específica.
    
    Utiliza las claves de la categoría obtenidas con la función obtener_claves_categoria().
    Solicita al usuario ingresar valores para cada clave y construye el diccionario de producto.
    """
    # Obtener las claves de la categoría
    key_categoria = obtener_claves_categoria(categoria)
    if key_categoria is not None:
        # Crear un diccionario vacío para el producto
        producto = {}
        # Iterar sobre cada característica en las claves de la categoría
        for caracteristica in key_categoria:
            # Solicitar al usuario ingresar el valor para cada característica
            valor = input(f"Ingrese el valor para {caracteristica}: ")
            # Agregar la característica y su valor al diccionario del producto
            producto[caracteristica] = valor
        # Devolver el diccionario de producto creado
        return producto


def agregar_prodcuto_catalogo(catalogo, categoria, producto):
    """
    Agrega un diccionario de producto al catálogo en la categoría correspondiente.

    Busca la categoría en el catálogo y agrega el producto al diccionario de esa categoría.
    """
    # Iterar sobre cada elemento del catálogo
    for item in catalogo:
        # Verificar si la categoría está presente en el elemento del catálogo
        if categoria in item:
            # Agregar el producto al diccionario de la categoría correspondiente
            item[categoria].append(producto)
            # Detener la búsqueda una vez que se ha agregado el producto
            break
    return catalogo # Devolver el catálogo actualizado


def formato_impresion_producto(producto):
    """
    Imprime el diccionario de un producto en un formato.
    """
    print('~') # Separacion visual
    # Itera sobre cada clave y valor en el diccionario del producto
    for key, value in producto.items():
        # Imprime la clave y el valor en un formato legible
        print(f'{key}: {value}')


def mostrar_productos(catalogo, categoria=None):
    """
    Muestra los productos del catálogo.

    Si se especifica una categoría, muestra solo los productos de esa categoría.
    Si no se especifica una categoría, muestra todos los productos del catálogo.
    """
    # Itera sobre cada item en el catálogo
    for item in catalogo:
        # Itera sobre cada categoría y lista de productos en cada item
        for item_categoria, productos in item.items():
            # Comprueba si no se especificó ninguna categoría o si la categoría actual coincide
            if categoria is None or item_categoria == categoria:
                # Comprueba si la lista de productos no está vacía
                if len(productos) > 0:
                    # Imprime el título de la categoría
                    print(f"--- {item_categoria} ---")
                    # Itera sobre cada producto en la lista de productos
                    for producto in productos:
                        # Se imprime cada producto
                        formato_impresion_producto(producto)
                else:
                    # Imprime un mensaje de que no hay productos en la categoría actual
                    print(f"No hay productos de la categoría {item_categoria} en el catálogo.")


def obtener_lista_productos(catalogo):
    """
    Regresa una lista de todos los productos del catálogo.
    """
    # Lista vacía para almacenar los productos
    lista_productos = []
    # Iterar sobre cada categoría en el catálogo
    for categoria in catalogo:
        # Iterar sobre cada lista de productos en la categoría actual
        for productos in categoria.values():
            # Agregar los productos a la lista_productos
            lista_productos.extend(productos)
    # Devolver la lista de productos
    return lista_productos


def buscar_y_eliminar_producto(lista_productos, palabras_clave, catalogo):
    """
    Busca productos en la lista de productos utilizando palabras clave.

    Realiza una búsqueda recursiva con las palabras clave.
    Muestra los productos encontrados y ofrece la opción de eliminar un producto.
    """
    # Copia el catálogo en una variable local
    catalogo = catalogo
    # Lista vacía para almacenar los productos encontrados
    productos_encontrados = []
    # Itera sobre cada producto en la lista de productos
    for producto in lista_productos:
        # Inicializa una variable para indicar si el producto coincide con las palabras clave
        producto_coincidente = True
        # Itera sobre cada palabra clave en las palabras clave proporcionadas
        for palabra_clave in palabras_clave:
            # Inicializa una variable para indicar si se encontró la palabra clave en el producto
            encontrado = False
            # Itera sobre cada clave y valor en el diccionario de producto
            for clave, valor in producto.items():
                # Comprueba si la palabra clave (en minúsculas) está presente en el valor convertido a cadena (en minúsculas)
                if palabra_clave.lower() in str(valor).lower():
                    # Marca que se encontró la palabra clave en el producto
                    encontrado = True
                    break
            # Si no se encontró la palabra clave en el producto, marca que el producto no coincide
            if not encontrado:
                producto_coincidente = False
                break
        # Si el producto coincide con todas las palabras clave, se agrega a la lista de productos encontrados
        if producto_coincidente:
            productos_encontrados.append(producto)

    # Comprobar que no hay productos encontrados
    if len(productos_encontrados) == 0:
        print("No se encontró ningún producto con la palabra clave en el catálogo.")
        return False
    # Si se encontró un único producto
    elif len(productos_encontrados) == 1:
        # Obtener el producto encontrado
        producto = productos_encontrados[0]
        print("Producto encontrado:")
        formato_impresion_producto(producto)
        # Solicitar confirmación para eliminar el producto
        confirmar_eliminar = input("¿Desea eliminar este producto? (s/n): ")
        if confirmar_eliminar.lower() == "s":
            # Buscar y eliminar el producto del catálogo
            for categoria in catalogo:
                for productos in categoria.values():
                    if producto in productos:
                        productos.remove(producto)
            print("Producto eliminado del catálogo.")
            return producto
        else:
            return False
    # Si se encontraron múltiples productos
    else:
        print("Productos encontrados:")
        # Imprimir todos los productos encontrados
        for producto in productos_encontrados:
            formato_impresion_producto(producto)
        # Solicitar nuevas palabras clave para una búsqueda recursiva
        nuevas_palabras_clave = input('Ingrese otra/s palabra/s clave (separe por espacios): ').split()
        # Realizar una búsqueda recursiva con las nuevas palabras clave
        return buscar_y_eliminar_producto(lista_productos, nuevas_palabras_clave, catalogo)


def busqueda_producto_titulo(catalogo):
    """
    Elimina un producto del catálogo.

    Solicita al usuario seleccionar un producto de la lista y lo elimina del catálogo.
    """
    # Solicitar al usuario que ingrese palabras clave para buscar en el título del producto
    palabras_clave = input("Ingrese palabras clave del título del producto a buscar: ").lower()
    # Lista vacía para almacenar los productos coincidentes
    productos_coincidentes = []
    # Iterar sobre cada categoría en el catálogo
    for categoria in catalogo:
        # Iterar sobre cada tipo de producto y lista de productos en cada categoría
        for tipo_producto, productos in categoria.items():
            # Iterar sobre cada producto en la lista de productos
            for producto in productos:
                # Obtener el título del producto y convertirlo a minúsculas
                titulo = producto.get('Titulo', '').lower()
                # Comprobar si las palabras clave están presentes en el título
                if palabras_clave in titulo:
                    # Agregar el tipo de producto y el producto coincidente a la lista de productos coincidentes
                    productos_coincidentes.append((tipo_producto, producto))
    # Comprobar si se encontraron productos coincidentes
    if not productos_coincidentes:
        print("No se encontraron productos que coincidan con las palabras clave ingresadas.")
        return
    # Mostrar los productos encontrados
    print("Productos encontrados:")
    for tipo_producto, producto in productos_coincidentes:
        print(f"Tipo de producto: {tipo_producto}")
        formato_impresion_producto(producto)