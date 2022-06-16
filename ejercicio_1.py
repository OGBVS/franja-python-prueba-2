def palabra_mas_larga(palabra):
    longitud = []
    for i in palabra:
        longitud.append((len(i), i))


    longitud.sort()
    return longitud[-1][1]

def main():
    palabra = ['imbecilidad' , 'informabilidad' , ' inhabilitado' , 'injusticia']    
    print(palabra_mas_larga(palabra))
main()
