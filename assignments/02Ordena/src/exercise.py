def main():
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x < y < z:
        print(x)
        print(y)
        print(z)
    elif y < x < z:
        print(y)
        print(x)
        print(z)
    elif z < x < y:
        print(z)
        print(x)
        print(y)
    elif z < y < x:
        print(z)
        print(y)
        print(x)
    elif x < z < y:
        print(x)
        print(z)
        print(y)
    else:
        print(y)
        print(z)
        print(x)



if __name__=='__main__':
    main()
