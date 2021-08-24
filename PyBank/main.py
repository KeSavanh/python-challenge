import os
import csv
from typing import Counter

budget_csv = os.path.join('budget_data.csv')
with open(budget_csv, 'r') as budget:
    budget_reader = csv.reader(budget, delimiter=",")
    next (budget_reader, None)
    #Total_month = 0
    total_budget = 0
    for row in budget_reader:
        Date = [row[0]]
        #Total_month = 
        #total_budget += int(row[1])
        print(Total_month)