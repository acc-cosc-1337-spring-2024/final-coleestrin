class Stock:

    def __init__(self, symbol, company_name) -> None:
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self) -> str:
        return self.__symbol
    
    def get_company_name(self) -> str:
        return self.__company_name
    
def stock_purchase_history():

    companies = {
        "AAPL": "Apple Inc",
        "CAT": "Caterpillar",
        "EK": "Eastman Kodak",
        "GOOG": "Google",
        "MSFT": "Microsoft"
    }

    stock_dict = {}

    for company in companies:
        stock_dict[company] = Stock(company, companies[company])
    
    print("Symbol | Company Name")

    for stock in stock_dict:
        stockObject = stock_dict[stock]

        print(stockObject.get_symbol(), stockObject.get_company_name())
