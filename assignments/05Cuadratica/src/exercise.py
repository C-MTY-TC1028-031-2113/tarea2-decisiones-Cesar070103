import math

def main():
    a = int(input("Da el valor de a: "))
    b = int(input("Da el valor de b: "))
    c = int(input("Da el valor de c: "))

    if a == 0 and b == 0:
        print("No tiene solucion")
    elif a == 0 and b != 0:
        x = -c/b
        print(x)
    elif a != 0 and b != 0:
        ecuacion1 = (b**2) - (4*a*c)
        if ecuacion1 < 0:
            print("Raices complejas")
        elif ecuacion1 > 0:
            x1 = (-b + math.sqrt(ecuacion1)) / 2*a
            x2 = (-b - math.sqrt(ecuacion1)) / 2*a
            print(x1)
            print(x2)
        else:
            x = -b/(2*a)
            print(x)
    else:
        print("Incorrecto")

if __name__ == '__main__':
    main()
