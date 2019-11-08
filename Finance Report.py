import csv
import os

#A debit is an accounting entry that either increases an asset or expense account (checking),
#or decreases a liability or equity account (credit card)


#A credit is an accounting entry that either increases a liability or equity account (credit card),
#or decreases an asset or expense account (checking).


bankPath = "./Banks"
slash = "./"

class Date:
    def __init__(self, date):
        self.month = 1
        self.day = 1
        self.year = 2000
        self.stringValue = date
        self.Parse()
        
    def Parse(self):
        values = self.stringValue.split("/")
        self.month = values[0]
        self.day = values[1]
        self.year = values [2]

    def Print(self):
        print("Date: " + self.stringValue) 
        

class Transaction:
    def __init__(self, dt, amnt, typ, dec, td):
        self.date = Date(dt)
        self.amount = amnt
        self.type = typ
        self.desc = dec
        self.typeDetails = td
        
    def Print(self):
        print("Transaction: ")
        self.date.Print()
        print(self.amount)
        print("Type: " + self.type)
        print("Description: " + self.desc)


class Account:
    def __init__(self, typ):
        self.type = typ
        self.transactions = []


class Bank:
    def __init__(self, n):
        self.name = n
        self.files = []
        self.accounts = []
        

    def ParseForInput(self):
        if self.name == "Chase":
            self.ParseChase()
        elif self.name == "Citi":
            self.ParseCiti()

    def ParseChase(self):
        for file in self.files:
            with open(bankPath+slash+self.name+ slash + file, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:
                        self.transactions.append(Transaction(row[1], row[3], row[0], row[2], row[4]))
                    line_count += 1
    
    def ParseCiti(self):
        for file in self.files:
            with open(bankPath+slash+self.name+ slash + file, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:
                        amount = 0
                        typ = "NOT SET"
                        
                        if row[3] != "":
                            amount == row[3]
                            typ = "DEBIT"
                        elif row[3] == "" and row[4] != "":
                            amount = row[4]
                            typ = "CREDIT"
                        self.transactions.append(Transaction(row[1], row[3], row[0], row[2], "n/a"))
                    line_count += 1

                    
    def PrintTransactions(self):
        for t in self.transactions:
            t.Print()
            print(" ")

            
def main():
    print("Collecting data!")
    banks = os.listdir(bankPath )
    bankList = []
    for bank in banks:
        tmp = Bank(bank)
        tmp.files = os.listdir(bankPath + "/" + bank)
        bankList.append(tmp)

    for bank in bankList:
        if bank.name == "Citi":
            bank.ParseForInput()
            #bank.PrintTransactions()
            
    

  


main()
