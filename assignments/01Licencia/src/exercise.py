
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad > 0:
        if edad >= 18:
            oficial = str(input("¿Tienes identificación oficial? (s/n): "))
            if oficial == "s":
                print("Trámite de licencia concedido")
            elif oficial == "n":
               print("No cumples requisitos")
            else:    
                print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")
    
if __name__ == '__main__':
    main()