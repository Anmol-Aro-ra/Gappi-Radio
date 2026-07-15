import csv
import os
from datetime import datetime
from dataclasses import dataclass


from core.base_skill import BaseSkill

@dataclass
class Expense:
            amount : float
            category : str
            date : str
            description : str


class ExpenseSkill(BaseSkill):

    def __init__(self, speaker):
         self.speaker = speaker
         self.filepath = "data/expenses.csv"
         self._setup_file()

    def _setup_file(self):
         os.makedirs("data", exist_ok = True)
         if not os.path.exists(self.filepath):
              with open(self.filepath, 'w', newline='')as f:
                   writer = csv.writer(f)
                   writer.writerow(["amount","category","date","description"])
                   

    def handle(self, command: str):
        if "add" in command:
            self.add_expense(command)
        elif "show" in command:
            self.view_expenses()
    
    def get_keywords(self):
        return ["expense","spend","cost","खर्च"]
     
    def add_expense(self,command):
         parts = command.split()
         amount = float(parts[2])
         category =  parts[3]
         date = datetime.now().strftime("%Y-%m-%d")
         expense = Expense(amount,category,date,"")
         with open(self.filepath,'a',newline='')as f:
              writer = csv.writer(f)
              writer.writerow([expense.amount,expense.category,expense.date,expense.description])
         print(f"Added:{amount} for {category}")
     
    def view_expenses(self):
         with open(self.filepath,'r') as f:
              reader = csv.reader(f)
              next(reader)
              for row in reader:
                   print(f"Amount: {row[0]} | Category: {row[1]} | Date: {row[2]}")