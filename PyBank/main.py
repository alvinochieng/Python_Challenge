import os 
import csv

#loading the file
path = os.path.join ('Resources', 'budget_data.csv')
output_path = os.path.join('PyBank.txt')

#Variables that will be used throughout the code
Date = []
Profit_Losses = []
sum_months = 1
net_prolo = 0
avg_change = 0
monthly_change = []
tot_change = 0
max_prolo = ["",-1000000000]
min_prolo = ["",100000000000]

#Reading the csv file
with open (path, newline='') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')

#skips the header row    
    header = next(csvreader)
 
    prev_row = next(csvreader)
    net_prolo += int(prev_row[1])
    Date.append(str(prev_row[0]))
    Profit_Losses.append(int(prev_row[1]))
    
#creating a loop to collect data    
    for row in csvreader:
        
        Date.append(str(row[0]))
        Profit_Losses.append(int(row[1]))
        
#calculate monthly change
        diff = int(row[1]) - int(prev_row[1])
        monthly_change.append(diff)
        prev_row = row
        
#formula for calculating total of the months                
        sum_months+= 1
        
#formula for net total of profit/losses(prolo)
        net_prolo = net_prolo + (int(row[1]))
        if diff < min_prolo[1]:
            min_prolo[1] = diff
            min_prolo[0] = row[0]
        elif diff > max_prolo[1]:   
            max_prolo[1] = diff
            max_prolo[0]= row[0]     
        
#formula for the average of changes in profit/losses
avg_change = sum(monthly_change) / len(monthly_change)
   
#Output the results to the terminal
#creating a dictionary output_results to prevent retyping when printing to the text file
output_results = (
    f"Total Months: {str(sum_months)}\n"
    f"Net Total Profit/Losses: ${int(net_prolo)}\n"
    f"Average Change: ${int(avg_change)}\n"
    f"Greatest Increase in Profits: {max_prolo}\n"
    f"Greatest Decrease in Losses: {min_prolo}")

print(output_results)

#output the results to a text file        
with open(output_path, 'w', newline='') as txtfile:
    csvwriter = (txtfile)
    
    txtfile.write('Financial Analysis \n')
    txtfile.write('----------------------------- \n')
    csvwriter.write(output_results)
