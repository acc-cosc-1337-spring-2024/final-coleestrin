from question_b import stock_purchase_history

def main():

    print("""
    1 - Display stock purchase history
    2 - Exit
          """)
    
    userChoice = int(input("Your choice? (1-2)"))

    if (userChoice == 2):
        return
    
    if (userChoice == 1):
        stock_purchase_history()

    main()
main()