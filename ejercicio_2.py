def main():

    palabra = input("Escriba una palabra: ")

    palabra1 = input("Ingrese otra palabra: ")

    if palabra[-3:] == palabra1[-3:]:
        print("Sus palabras si riman.")

    elif palabra[-2:] == palabra1[-2:]:
        print("Sus palabras no riman mucho.")

    else:
        print("Sus palabras no riman en lo absoluto.")
        