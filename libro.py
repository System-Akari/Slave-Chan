class libro:
    def __init__(self,fecha,link):
        self.fecha = fecha
        self.link = link
    
    def toCollection(self):
        return {
            "fecha": self.fecha,
            "link": self.link
        }
        