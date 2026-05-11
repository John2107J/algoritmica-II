def intercalar(cad1,cad2):
    long = min(len(cad1),len(cad2))
    cad3= ""
    for i in range(long):
        cad3 += cad1[i] + cad2[i]
    
    cad3 += cad1[long:] + cad2[long:]
    return cad3

#Programa principal
def main():
    cad1 = input("Ingrese la primera cadena: ")
    cad2 = input("Ingrese la segunda cadena: ")

    cad3 = intercalar(cad1, cad2)
    print("La cadena intercalada es: ", cad3)

if __name__ == "__main__":
    main()