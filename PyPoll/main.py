# Modules
import os
import csv

#Declare lists that you will need to analyze data from CSV file.

total_votes = []
list_of_candidates = []

#Initialize vote count for the three contestants:
Charles_Casper_Stockham_vote_count = 0
Diana_DeGette_vote_count = 0
Raymon_Anthony_Doane_vote_count = 0

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

   #Read the header first
    csv_header = next(csvreader)   

     #This loop iterates through every record and calculates total number of votes
     # and also calculates votes a specific contestant has gained.  

    for record in csvreader:
        total_votes.append(record[1])
        num_of_votes = len(total_votes)

        if record[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham_vote_count += 1

        elif record[2] == "Diana DeGette":
            Diana_DeGette_vote_count += 1
        
        elif record[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_vote_count += 1

    
#Determine %age of votes each contestant has won.

Charles_vote_percentage = (Charles_Casper_Stockham_vote_count/num_of_votes)*100
Dianna_vote_percentage = (Diana_DeGette_vote_count/num_of_votes)*100
Raymon_vote_percentage = (Raymon_Anthony_Doane_vote_count/num_of_votes)*100

#Create a dictionary that can store votes for the three contestants
contestant_votes = {"Charles Casper Stockham": Charles_Casper_Stockham_vote_count, "Diana DeGette": Diana_DeGette_vote_count, "Raymon Anthony Doane": Raymon_Anthony_Doane_vote_count }

winnner = max(contestant_votes, key=contestant_votes.get)

# Print values on the terminal
electiona_results_data = (
print(f"Election Results \n"),
print(f"------------------- \n"),
print(f"Total Votes:  {num_of_votes} \n"),
print(f"------------------- \n"),
print(f"Charles_Casper_Stockham:  ${Charles_vote_percentage:.3f}% ({Charles_Casper_Stockham_vote_count}) \n" ),
print(f"Dianne DeGette:  ${Dianna_vote_percentage:.3f}%  ({Diana_DeGette_vote_count} ) \n" ),
print(f"Raymon Anthony Doane:  ${Raymon_vote_percentage:.3f}% ({Raymon_Anthony_Doane_vote_count}) \n" ),
print(f"------------------- \n"),
print(f"Winner:  {winnner}  \n" ),

)

# Write values to an output text file called "Election_Results" under "Analysis" folder.
election_results_file = os.path.join("Analysis", "Election_Results.txt")

writefile = open(election_results_file, 'w')

writefile.write("E;ection Results\n")
writefile.write("-------------------\n")
writefile.write(f"Total Votes:  {num_of_votes} \n")
writefile.write(f"------------------- \n")
writefile.write(f"Charles_Casper_Stockham:  ${Charles_vote_percentage:.3f}% ({Charles_Casper_Stockham_vote_count})\n")
writefile.write(f"Dianne DeGette:  ${Dianna_vote_percentage:.3f}%  ({Diana_DeGette_vote_count} ) \n")
writefile.write(f"Raymon Anthony Doane:  ${Raymon_vote_percentage:.3f}% ({Raymon_Anthony_Doane_vote_count}) \n")
writefile.write("-------------------\n")
writefile.write(f"Winner:  {winnner}  \n")
writefile.close()