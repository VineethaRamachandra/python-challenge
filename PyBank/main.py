# Modules
import os
import csv

#Declare lists that you will need to analyze data from CSV file.
month_list = []
net_profit_loss_list = []
profit_loss_change = []
#Declare variables for calculating total number of months and net total amount of Profit/Losses over entire period
total_num_months = 0
net_total_amount = 0

# Set path for file
csvpath = os.path.join( "Resources", "budget_data.csv")

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
   
     #This loop iterates through every record and calculates total number of months and net total amount of Profit/Losses.
    for record in csvreader:
        
        # Keeps a tab on number of months/records.
        total_num_months +=1
       
        #Total of Profit/Loss
        net_total_amount += int(record[1])

        #Append every date record to the month list.
        month_list.append(record[0])

        #Append every profit_loss amount record to the profit_loss list.
        net_profit_loss_list.append(int(record[1]))

        profit_loss_change.append(net_profit_loss_list[total_num_months - 1] - net_profit_loss_list[total_num_months - 2])

        #net_change is sum of all profit/loss changes
        net_change = sum(profit_loss_change)

    #Determine length of profit_loss_change_list
    len_proft_loss_change_list = len(profit_loss_change)

    #avg_change is sum of net_change divided by (length of profit_loss_change list - 1). We need to subtract
    #by 1 as the number of changes would be one less than the length of record
    avg_change = net_change/(len_proft_loss_change_list - 1)
           
    # Finally, calculate change in profit_loss, the greatest increase and decrease in profits plus associated months and
    # # average change.

    # Greatest increase in profits
    greatest_increase_in_profits = max(profit_loss_change)

    #Find the month associated with greatest increase in profits
    month_profit_increased = profit_loss_change.index(greatest_increase_in_profits)

    # Greatest decrease in profits
    greatest_decrease_in_profits = min(profit_loss_change)

    # Find the month associated with greatest decrease in profits
    month_profit_decreased = profit_loss_change.index(greatest_decrease_in_profits)

# Print values on the terminal
financial_analysis_data = (
print(f"Fiancial Analysis \n"),
print(f"------------------- \n"),
print(f"Total Months:  {total_num_months} \n"),
print (f"Total:  ${net_total_amount} \n" ),
print (f"Average Change:  {avg_change:.2f} \n" ),
print (f"Greatest Increase in Profits:  {month_list[month_profit_increased]}  ({greatest_increase_in_profits}) \n" ),
print (f"Greatest Decrease in Profits:  {month_list[month_profit_decreased]}  ({greatest_decrease_in_profits}) \n" ),

)

# Write values to an output text file called "Financial_Analysis_Output" under "Analysis" folder.
financial_analysis_output_file = os.path.join("Analysis", "Financial_Analysis_output.txt")

writefile = open(financial_analysis_output_file, 'w')

writefile.write("Financial Analysis\n")
writefile.write("-------------------\n")
writefile.write(f"Total Months: {total_num_months}\n")
writefile.write(f"Total: ${net_total_amount}\n")
writefile.write(f"Average Change: ${avg_change:.2f}\n")
writefile.write(f"Greatest Increase in Profits: {month_list[month_profit_increased]} (${greatest_increase_in_profits}) \n")
writefile.write(f"Greatest Decrease in Profits: {month_list[month_profit_decreased]} (${ greatest_decrease_in_profits})\n")

writefile.close()






