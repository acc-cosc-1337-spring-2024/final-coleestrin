from question_d import create_multiplication_table, display_multiplication_table

def main():

    print(""" 
    1) Display multiplication table
    2) Exit
    """)

    user_choice = int(input("Your choice? (1-2)"))

    if (user_choice == 1):
        table = create_multiplication_table()
        display_multiplication_table(table)
    
    if (user_choice == 2):
        return
    
    main()
main()

