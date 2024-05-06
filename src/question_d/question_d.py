def create_multiplication_table() -> list:

    table = []

    for i in range(1,6):

        row = []

        for k in range(1,11):
            row.append(k * i)
    
        table.append(row)
    
    return table

def display_multiplication_table(table: list):
    for row in table:
        str = ""

        for number in row:
            str += f"{number} "

        print(str)
