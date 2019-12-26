import os 
import csv

votes_path = os.path.join ('Resources', 'election_data.csv')
votes_output = os.path.join ('PyPoll.txt')

voterid = 0
county = 0
candidate = 0
totalvotes = 0

#def print_votes(votes_data):

    #voterid = int(votes_data[0])
    #county = str(votes_data[1])
    #candidate = str(votes_data[2])

with open (votes_path, newline='') as csvfile:
    csvvotes = csv.reader(csvfile, delimiter = ',')
    
    header = next(csvvotes)
    
    for row in csvvotes:
        totalvotes += 1
        
        electiondata =(f"Total Votes Cast: {str(totalvotes)}")

with open(votes_output, 'w', newline='') as electiontxtfile:
    csvwriter = (electiontxtfile)
    
    electiontxtfile.write("Election Results \n")
    electiontxtfile.write("--------------------- \n")
    electiontxtfile.write(electiondata)
    
