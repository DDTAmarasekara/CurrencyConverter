from zeep import Client


class Conversion:
    
    def __init__(self):
        self.client = Client(wsdl="http://localhost:8080/convert?wsdl")
    
    
    def convert(self,sourceCurrency,sourceAmount,targetCurrency):
        return self.client.service.converter(sourceCurrency,sourceAmount,targetCurrency)