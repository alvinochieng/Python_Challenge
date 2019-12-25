import os 
import csv

#loading the file
path = os.path.join ('Resources', 'budget_data.csv')
output_path = os.path.join('PyBank.txt')

#Variables that will be used throughout the h/work
Date = []
Profit_Losses = []
sum_months = 0
net_prolo = 0

#Reading the csv file
with open (path, newline='') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
 
#creating a loop to collect data    
    for row in csvreader:
        
        Date.append(str(row[0]))
        Profit_Losses.append(int(row[1]))

#formula for calculating total of the months                
        sum_months+= 1
        
#formula for net total of profit/losses(prolo)
        net_prolo = net_prolo + (int(row[1]))
        
        output_results = (
            f"Total Months: {str(sum_months)}\n"
            f"Net Total Profit/Losses: {int(net_prolo)}")
        
        print(output_results)
        
with open(output_path, 'w', newline='') as txtfile:
    csvwriter = (txtfile)
    
    txtfile.write('Financial Analysis \n')
    txtfile.write('----------------------------- \n')
    csvwriter.write(output_results)
