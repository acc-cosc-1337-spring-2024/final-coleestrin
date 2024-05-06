from question_c import Stock

def main():

    stock = Stock("AAPL", "Apple Inc")

    print(f"The symbol is {stock.get_symbol()} and the company name is {stock.get_company_name()}")

main()