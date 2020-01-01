import os 
import csv

votes_path = os.path.join ('Resources', 'election_data.csv')
votes_output = os.path.join ('PyPoll.txt')

totalvotes = 0
candidate_list = []

#loading the file.
with open (votes_path, newline='') as csvfile:
        csvvotes = csv.reader(csvfile, delimiter = ',')
            
        header = next(csvvotes)   
    
        for row in csvvotes: 
               
#finding the unique candidate list.                 
                if row[2] not in candidate_list:
                        
                        totalvotes += 1
                        
                        candidate_list.append(row[2])
                else:
                        totalvotes += 1

#declaring a variable i.                       
i = 0

#creating a new list with a value 
list = len(candidate_list)
cand_votes = [0] * list

#reloading the file again
with open (votes_path, newline='') as csvfile:
        csvvotes = csv.reader(csvfile, delimiter = ',')
            
        header = next(csvvotes)   
    
        for row in csvvotes: 

                for i in range(list):
                        if row[2] == candidate_list[i]:
                                cand_votes[i] += 1

#creating a variable for each candidate percentage                
k = 0
percentage = []

for k in range(list):
        candidate_percent = round(cand_votes[k] / totalvotes * 100, 2)
        percentage.append(candidate_percent)

winning_vote = max(cand_votes)
winning_index = cand_votes.index(winning_vote)
win_candidate = candidate_list[winning_index]

print(candidate_percent)
#print(f'{str(candidate_list)}' + f'{str(cand_votes)}')
                
electiondata = (f"Total Votes Cast: {str(totalvotes)} \n")

with open(votes_output, 'w', newline='') as electiontxtfile:
        csvwriter = (electiontxtfile)
        
        electiontxtfile.write("Election Results \n")
        electiontxtfile.write("--------------------- \n")
        electiontxtfile.write(f"{str(electiondata)} \n")
        electiontxtfile.write("----------------------\n")
        electiontxtfile.write(f"Winner: {str(win_candidate)}")
    
