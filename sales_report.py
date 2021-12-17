"""Generate sales report showing total melons each salesperson sold."""
# Working on the exercise at https://ed.devmountain.com/materials/data-bp-1/exercises/salesperson-report/

def compiler (file_name):
    """This function opens and reads through a file and compiles it into 2 lists, one for salespople and one for melons_sold, with a direct relation between matching indexes, such as salespeople[2] and melons_sold[2].
    
    Argument:
        file_name (str) - name of the .txt file to work with
    
    Returns:
        salespeople (list)
        melons_sold (list)
    """
    
    salespeople = []
    melons_sold = []

    f = open(file_name)
    for line in f:
        salesperson, _, melons = line.rstrip().split('|')

        if salesperson in salespeople:
            position = salespeople.index(salesperson)

            melons_sold[position] += int(melons)
        else:
            salespeople.append(salesperson)
            melons_sold.append(int(melons))
    return salespeople, melons_sold

def printer(salespeople, items_sold):
    """This function takes 2 lists as a parameter, salespeople and items sold, and then prints that information in a more readalbe format in the terminal.
    
    Arguments:
        salespeople (list)
        items_sold (list)
    """
    for i in range(len(salespeople)):
        print(f'{salespeople[i]} sold {items_sold[i]} melons')


salespeople, melons_sold = compiler('sales-report.txt')

printer(salespeople, melons_sold)