#import modules
import os
import csv
#set local pc path to data csv file
election_csv = os.path.join("..", "..", "election_data.csv")
#create votes dictionary
votes = {}
#open and read csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header row
    csv_header = next(csvfile)
    #run through the file
    for row in csvreader:
        #define candidate column
        candidate = row[2]
        #if candidate not in dictionary, add with first vote
        if candidate not in votes:
            votes[candidate] = 1
        #if candidate already in dictionary, add a vote
        else:
            votes[candidate] += 1
#check the results
#for key, value in votes.items():
    #print(f'{key} : {value}')

#add the dictionary keys for vote total
values = votes.values()
voteTotal = sum(values)
#print (voteTotal)

#print to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {voteTotal}")
print(f"-------------------------")
for key, value in votes.items():
    print(f"{key}: {value / voteTotal:.3%} ({value})")
print(f"-------------------------")
print(f"Winner: {max(votes, key=votes.get)}")
print(f"-------------------------")

#output the same results to a text file
output_path = os.path.join("..", "analysis", "electionResults.txt")
with open(output_path, "w", newline='') as datafile:
    datafile.write(
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {voteTotal}\n"
    f"-------------------------\n")
    #note for loop has to be left out of datafile.write parenthesis to run
    for key, value in votes.items():
        #add a datafile.write line for results alone
        datafile.write(f"{key}: {value / voteTotal:.3%} ({value})\n")
    datafile.write(f"-------------------------\n"
    f"Winner: {max(votes, key=votes.get)}\n"
    f"-------------------------")