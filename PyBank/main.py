import os
import csv

# open file path
budget_path = os.path.join('budget_data.csv')
with open(budget_path, 'r') as budget:
    budget_reader = csv.reader(budget, delimiter=",")
# skip headers
    next (budget_reader)
# create lists for date, profit and changes 
    date = []
    profit_losses =[]
    changes_list =[]
    
    for row  in budget_reader:
# add rows into lists
        date.append(row[0])
        profit_losses.append(float(row[1]))
# Count numbers of months
        total_month = len(date)
# calculate total of profit/losses
        total_budget = sum(profit_losses)
# loop through row[1] then calculate the changes between rows
    for x in range(1, len(profit_losses)):
        changes =(profit_losses[x] - profit_losses[x-1])
# add results to the list
        changes_list.append(changes)
# calculate average of changes
        changes_avg = round(sum(changes_list)/len(changes_list))
# find the min and max of changes
        changes_min = round(min(changes_list))
        changes_max = round(max(changes_list))
# find the dates of max and min values in changes list
        min_date = str(date[changes_list.index(min(changes_list))])
        max_date = str(date[changes_list.index(max(changes_list))])
# Report
#export to txt file
analysis_report = os.path.join("..", "Analysis/PyBankReport.txt")
with open(analysis_report, "w") as pybankreport:
    pybankreport.writelines ("Financial Analysis")
    pybankreport.writelines('\n')
    pybankreport.writelines("-----------------------------")       
    pybankreport.writelines('\n')
    pybankreport.writelines("Total Months:" + " " + str(total_month))
    pybankreport.writelines('\n')
    pybankreport.writelines("Total:" + " " + "$" + str(total_budget))
    pybankreport.writelines('\n')
    pybankreport.writelines ("Average Change:" + " " + "$" + str(changes_avg))
    pybankreport.writelines('\n')
    pybankreport.writelines ("Greatest Increase in Profits:" + " " 
                            + str(max_date) + " "+ "(" + "$"+ " " 
                            +str(changes_max)+ " "+ ")")
    pybankreport.writelines('\n')
    pybankreport.writelines("Greatest Decrease in Profits:" + " " 
                            + str(min_date) + " "+ "(" + "$"+ " " 
                            + str(changes_min)+ " "+ ")")
    

