import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#variables
totalvotes = 0

#dictionary
candidates = {}

#total votes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1

individualcandidatename = candidates.keys()
individualvotes = candidates.values()
percentagevotes = [f'{(i/totalvotes*100):.3f}%' for i in candidates.values()]
winnername = max(candidates, key=candidates.get)

print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalvotes}')
print('-------------------------')
i = 0
for candloop, totalloop in candidates.items():
    print(f"{candloop}: {percentagevotes[i]} ({totalloop})")
    i = i + 1
print('-------------------------')
print(f'Winner: {winnername}')
print('-------------------------')

textoutput = os.path.join("PyPoll.txt")
 
with open(textoutput, "w") as textfile:
    textfile.write('Election Results')
    textfile.write('\n')
    textfile.write('-------------------------')
    textfile.write('\n')
    textfile.write(f'Total Votes: {totalvotes}')
    textfile.write('\n')
    textfile.write('-------------------------')
    textfile.write('\n')
    i = 0
    for candloop, totalloop in candidates.items():
        textfile.write(f"{candloop}: {percentagevotes[i]} ({totalloop})")
        i = i + 1
        textfile.write('\n')
    textfile.write('-------------------------')
    textfile.write('\n')
    textfile.write(f'Winner: {winnername}')
    textfile.write('\n')
    textfile.write('-------------------------')