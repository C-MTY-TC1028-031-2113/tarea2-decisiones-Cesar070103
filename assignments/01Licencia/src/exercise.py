
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad == str:
        print("Respuesta incorrecta")
    if edad >= 18:
        oficial = str(input("¿Tienes identificación oficial? (s/n) "))
        if oficial == "s":
            print("Trámite de licencia concedido")
        else:
            print("No cumples requisitos")
    else:
        print("No cumples requisitos")

if __name__ == '__main__':
    main()

#Falta saber qué pasa cuando el dato no es válido