def main():
    grados = int(input("Introduce los grados: "))
    if grados > 0 and grados < 90:
        print("cuadrante 1")
    elif grados > 90 and grados < 180:
        print("cuadrante 2")
    elif grados > 180 and grados < 270:
        print("cuadrante 3")
    elif grados > 270 and grados < 360:
        print("cuadrante 4")
    elif grados == 90:
        print("eje")
    elif grados == 180:
        print("eje")
    elif grados == 270:
        print("eje")
    elif grados == 360:
        print("eje")
    else:
        print("excede")

if __name__ == '__main__':
    main()
