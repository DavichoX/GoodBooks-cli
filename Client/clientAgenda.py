import clients
import csv
import os

class ClientAgenda:
    def __init__(self) -> None:
        self.path = os.path.join("/",'Users', 'davidrengifolozano', 'Desktop', 'RoadToBusiness', 'languages', 'PYTHON', 'PROYECTS', 'Bookkeeping Project', 'Client', 'client_list.csv') 
        self.clientes = []
    def save_clients(self):
         with open(self.path,'a',newline='') as write_csv:
            writer = csv.writer(write_csv,delimiter=",")
            writer.writerow(self.clientes)

    def add_client(self,document,name,surname,adress):
        new_client = clients.Client(document,name,surname,adress)
        self.clientes = new_client.client()
        self.save_clients()

asdad = ClientAgenda()

asdad.add_client(76069822,"David","Rengifo","Manantay")
asdad.add_client(73032715,"Lia","Diaz","Manantay")
asdad.add_client(11117686,"Marcelo","Rengifo","Manantay")
asdad.add_client(11105127,"Tania","Lozano","Manantay")