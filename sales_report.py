"""Generate sales report showing total melons each salesperson sold."""
# Working on the exercise at https://ed.devmountain.com/materials/data-bp-1/exercises/salesperson-report/

def compiler (file_name):
    """This function opens and reads through a file and compiles it into 2 lists, one for salespeople and one for total_melons_sold, with a direct relation between matching indexes, such as salespeople[2] and total_melons_sold[2].
    
    Argument:
        file_name (str) - name of the .txt file to work with
    
    Returns:
        salespeople (list)
        total_melons_sold (list)
    """
    
    salespeople = [] # creating empty list to add to
    total_melons_sold = [] # creating empty list to add to

    # with open(file_name) as f: # could be used instead of the below line
    f = open(file_name) # opens the file and stores it in an object
    for line in f: # iterates through each line
        salesperson, _, melons_sold = line.rstrip().split('|') # splits each line into a list and stores each value in an object, except the second value (total sale?) is not saved

        if salesperson in salespeople: # if this salesperson's name is already in salespeople list
            position = salespeople.index(salesperson) # check what index in the salespeople list that salesperson's name is at
            total_melons_sold[position] += int(melons_sold) # at the matching index in the total_melons_sold list, add the amount of melons_sold
        else: # if first time seeing salesperson's name
            salespeople.append(salesperson) # save their name to the salespeople list
            total_melons_sold.append(int(melons_sold)) # save their number of melons_sold to the total_melons_sold list
    return salespeople, total_melons_sold # returning the completed lists, salespeople and total_melons_sold

def printer(salespeople, items_sold):
    """This function takes 2 lists as a parameter, salespeople and items sold, and then prints that information in a more readalbe format in the terminal.
    
    Arguments:
        salespeople (list)
        items_sold (list)
    """
    for i in range(len(salespeople)): # length of both lists are the same, so making a range using the length of one of the lists to iterate through
        print(f'{salespeople[i]} sold {items_sold[i]} melons') # printing paired indexes from salespeople (list) and items_sold (list), in a readable format.


salespeople, total_melons_sold = compiler('sales-report.txt') # calling the compiler function with a .txt file to read as the parameter, and saving both returns from the function to an object

printer(salespeople, total_melons_sold) # calling the printer function using both objects from the compiler function as the parameters