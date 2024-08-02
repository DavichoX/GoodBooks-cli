from Sales import clients
def register():
        name = input("Primer Nombre: ")
        if string.digits in name:
            print("ingrese un nombre correcto...")
        surname = input("Primer Apellido: ")
        if string.digits in surname:
            print("ingrese un nombre correcto...")
        select_document = input("Tipo de documento (dni: d, extranjeria: e, ruc: r): ")
        match select_document:
            case "d":
                dni = int(input("DNI: "))
                if document > 8:
                    print("ingrese un dni valido...")
                document = f"C{dni}"
            case "e":
                extr = int(input("Extranjeria: "))
                if document > 6:
                    print("ingrese un documento de extranjeria valido...")
                document = f"C{extr}"                
            case "r":
                ruc = int(input("Ruc: "))
                if document > 10:
                    print("ingrese un ruc valido...")                
                document = f"C{ruc}"
        adress = input("Direccion: ")