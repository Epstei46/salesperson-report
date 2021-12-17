"""Generate sales report showing total melons each salesperson sold."""
# Working on the exercise at https://ed.devmountain.com/materials/data-bp-1/exercises/salesperson-report/

def open_file(file_name):
    """This function opens the file and saves it to a variable."""
    return open(file_name)

def compiler (file_txt):
    """This function reads through a file and compiles it into 2 lists, one for salespople and one for melons_sold, with a direct relation between matching indexes, such as salespeople[2] and melons_sold[2]. Then returns both of those lists."""
    
    salespeople = []
    melons_sold = []

    for line in file_txt:
        salesperson, _, melons = line.rstrip().split('|')

        if salesperson in salespeople:
            position = salespeople.index(salesperson)

            melons_sold[position] += int(melons)
        else:
            salespeople.append(salesperson)
            melons_sold.append(int(melons))
    return salespeople, melons_sold

def printer(salespeople, items_sold):
    """This function takes 2 lists as a parameter, salespeople and items sold, and then prints that information in a more readalbe format in the terminal."""
    for i in range(len(salespeople)):
        print(f'{salespeople[i]} sold {items_sold[i]} melons')


file_txt = open_file('sales-report.txt')

salespeople, melons_sold = compiler(file_txt)

printer(salespeople, melons_sold)