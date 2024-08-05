class Client:
    def __init__(self,document,name,surname,adress) -> None:
        self.document = document
        self.name = name
        self.surname = surname
        self.adress = adress
    
    def client(self):
        return [f"{self.document}", f"{self.name}", f"{self.surname}",f"{self.adress}"]