import os 
import csv

#loading the file
path = os.path.join ('Resources', 'budget_data.csv')
output_path = os.path.join('PyBank.txt')

#Variables that will be used throughout the code
Date = []
Profit_Losses = ()
sum_months = 0
net_prolo = 0
avg_change = 0
monthly_change = 0
tot_change = 0

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
        
#formula for the average of changes in profit/losses
        avg_change = net_prolo / sum_months
        
#Getting the greatest profit increase/ greatest loss decrease
max_prolo = int(Profit_Losses[sum_months-1][1])-int(Profit_Losses[sum_months-2][1])
min_prolo = int(Profit_Losses[sum_months-1][1])-int(Profit_Losses[sum_months-2][1])

for i in range(sum_months,1,-1):
    monthly_change = int(Profit_Losses[i-1][1]) - int(Profit_Losses[i-2][1])
    
    if monthly_change < min_prolo:
        min_change = Profit_Losses[i-1][0]
        min_prolo = monthly_change
    elif monthly_change > max_prolo:   
        max_prolo = monthly_change
        max_change = Profit_Losses[i-1][0]
        
        prolo_change = tot_change + monthly_change
        
        print(min_change + max_change)
   
#Output the results to the terminal        
        output_results = (
            f"Total Months: {str(sum_months)}\n"
            f"Net Total Profit/Losses: ${int(net_prolo)}\n"
            f"Average Change: ${int(avg_change)}\n")

print(output_results)

#output the results to a text file        
with open(output_path, 'w', newline='') as txtfile:
    csvwriter = (txtfile)
    
    txtfile.write('Financial Analysis \n')
    txtfile.write('----------------------------- \n')
    csvwriter.write(output_results)
