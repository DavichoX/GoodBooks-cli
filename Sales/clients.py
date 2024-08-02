import csv
import string

class Client:
    def __init__(self,documento,nombre,apellido,direccion) -> None:
        self.document = documento
        self.name = nombre
        self.surname = apellido
        self.adress = direccion

    def add_client(self):
        self.name = input("Primer Nombre: ")
        if string.digits in self.name:
            print("ingrese un nombre correcto...")
        self.surname = input("Primer Apellido: ")
        if string.digits in self.surname:
            print("ingrese un nombre correcto...")
        select_document = input("Tipo de documento (dni: d, extranjeria: e, ruc: r): ")
        match select_document:
            case "d":
                dni = int(input("DNI: "))
                if self.document > 8:
                    print("ingrese un dni valido...")
                self.document = f"C{dni}"
            case "e":
                extr = int(input("Extranjeria: "))
                if self.document > 6:
                    print("ingrese un documento de extranjeria valido...")
                self.document = f"C{extr}"                
            case "r":
                ruc = int(input("Ruc: "))
                if self.document > 10:
                    print("ingrese un ruc valido...")                
                self.document = f"C{ruc}"
        self.adress = input("Direccion: ")

        