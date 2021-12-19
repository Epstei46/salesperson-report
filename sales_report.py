"""Generate sales report showing total melons each salesperson sold."""
# Working on the exercise at https://ed.devmountain.com/materials/data-bp-1/exercises/salesperson-report/

salespeople = [] # creating empty list to add to
melons_sold = [] # creating empty list to add to

f = open('sales-report.txt') # opens the file and stores it in an object
for line in f: # iterates through each line
    line = line.rstrip() # strips white space and new line (\n) off the right/end of the line
    entries = line.split('|') # splits each line into a list

    salesperson = entries[0] # stores first value in salesperson object
    melons = int(entries[2])# stores third value (as an integer) in melons object

    if salesperson in salespeople: # if this salesperson's name is already in salespeople list
        position = salespeople.index(salesperson) # check what index in the salespeople list that salesperson's name is at
        melons_sold[position] += melons # at the matching index in the melons_sold list, add the amount of melons sold
    else: # if first time seeing salesperson's name
        salespeople.append(salesperson) # save their name to the salespeople list
        melons_sold.append(melons) # save their number of melons sold to the melons_sold list


for i in range(len(salespeople)): # length of both lists are the same, so making a range using the length of one of the lists to iterate through
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') # printing paired indexes from salespeople (list) and melons_sold (list), in a readable format.