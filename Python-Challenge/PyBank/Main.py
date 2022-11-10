# import the os module to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join("Resources","budget_data.csv")


# open file in read mode and check the number of records
with open(csvpath, 'r') as fp:
    for count, line in enumerate(fp):
        pass


# process the file and data
with open (csvpath, "r") as csv_file:

    csv_reader = csv.reader(csv_file)

    
    
    #Store the headers
    for line in csv_reader:
        head1 = str(line[0])
        head2 = str(line[1])
        break



    
    #Set Lists
    lst = []
    lst2 = []
    lst3 = []
    
    totprofloss = 0 
    openval = int()

    n = 1

    for line in csv_reader:


        period = str(line[0])
        temppl = int(line[1])

        
        
        #determine the opening value
        if n == 1:
            openval = temppl
        else: exit

        #Process the data
        profloss = temppl
        lst.append(temppl)
        deltap = profloss - totprofloss
        lst2.append(deltap)
        totprofloss = profloss
        lst3.append(period)

        n=n+1

   
sumlist = sum(lst)
sumlist2 = sum(lst2)
maxlist = max(lst2)
minlist = min(lst2)
length2 = len(lst2)

locate = lst2.index(maxlist)
maxmonth = lst3[locate]
locate2 = lst2.index(minlist)
minmonth = lst3[locate2]

finalsum2 = sumlist2 - openval
totalcount = count
avglist2 = finalsum2 / (length2 - 1)

print(" ")
print("Financial Analysis")
print(" ")
print("-------------------------")
print(" ")
print("Total Months:    ", count)
print(" ")
print("Total:", "$", sumlist)
print(" ")
print("Average Change:", "$", "%.2f"%avglist2)
print(" ")
print("Greatest Increase in Profits:", maxmonth, "(","$", maxlist, ")")
print(" ")
print("Greatest Decrease in Profits:", minmonth,"(","$", minlist, ")")
print(" ")
print(" ")



