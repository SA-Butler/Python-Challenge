# import the os module to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "election_data.csv")


# open file in read mode and check the number of records
with open(csvpath, 'r') as fp:
    for count, line in enumerate(fp):
        pass

# process the data
with open (csvpath, "r") as csv_file:

    csv_reader = csv.reader(csv_file)

    
    #Store the headers
    for line in csv_reader:
        head1 = str(line[0])
        head2 = str(line[1])
        head3 = str(line[2])

        break

    #Set the lists
    candidate1lst = []
    candidate2lst = []
    candidate3lst = []

    
    for line in csv_reader:


        ballotid = int(line[0])
        county = str(line[1])
        candidate = str(line[2])

        #let the candidate determine where the value is placed

        if candidate == "Charles Casper Stockham":
            candidate1lst.append(ballotid)

        elif candidate == "Diana DeGette":
            candidate2lst.append(ballotid)

        elif candidate == "Raymon Anthony Doane":
            candidate3lst.append(ballotid)
        
        else: exit


#Determine Result from lists
candidate1 = "Charles Casper Stockham"
candidate2 = "Diana DeGette"
candidate3 = "Raymon Anthony Doane"

votescan1 = len(candidate1lst)
votescan2 = len(candidate2lst)
votescan3 = len(candidate3lst)

percent1 = (votescan1 / count) * 100
percent2 = (votescan2 / count) * 100
percent3 = (votescan3 / count) * 100

resultlst = [votescan1,votescan2,votescan3]

winres = max(resultlst)

if votescan1 == winres:
        winname = candidate1
    
elif votescan2 == winres:
        winname = candidate2

elif votescan3 == winres:
        winname = candidate3
    
else: winname = "Not found"

#Screen Output

print(" ")
print("Election Results")
print(" ")
print("------------------------------")
print(" ")
print("Total Votes:    ", count)
print(" ")
print("------------------------------")
print(" ")
print(candidate1,":", "%.3f"% percent1,"%", "(",votescan1,")")
print(candidate2,":", "%.3f"% percent2,"%", "(",votescan2,")")
print(candidate3,":", "%.3f"% percent3,"%", "(",votescan3,")")
print(" ")
print("------------------------------")
print("Winner: ", winname)
print("------------------------------")
print(" ")

#Output to a csv results file

winrow = ("Total Votes", (count))
row1 = str(candidate1) , str(votescan1), str(percent1)
row2 = str(candidate2) , str(votescan2), str(percent2)
row3 = str(candidate3) , str(votescan3), str(percent3)
row4 = ("Winner : ",winname)

data_output = os.path.join("Analysis", "results.csv")

with open(data_output, 'w',newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(winrow)
    writer.writerow(row1)
    writer.writerow(row2)
    writer.writerow(row3)
    writer.writerow(row4)







