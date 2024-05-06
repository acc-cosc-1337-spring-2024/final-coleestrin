class Stock:

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_company_name(self):
        return self.__company_name
    
    def get_symbol(self):
        return self.__symbol
    