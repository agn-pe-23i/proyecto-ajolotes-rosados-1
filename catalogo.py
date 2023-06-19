import menu
catalogo = None

def main():
    # Se define catalogo como variable global para poder manejar el catalogo a lo largo de la ejecucion del programa
    global catalogo 
    # Se llama a la función principal del módulo "menu"
    menu.principal(catalogo)

# Llama a la función main para iniciar el programa
main()