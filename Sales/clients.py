import csv
import string

class Client:
    def __init__(self,documento,nombre,apellido,direccion) -> None:
        self.document = documento
        self.name = nombre
        self.surname = apellido
        self.adress = direccion

    def add_client(self):
        with open('client_list.csv','w',newline='') as write_csv:
            pass

        