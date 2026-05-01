import csv
from datetime import datetime

FILE_NAME="expenses.csv"

def add_expense():
        amount=input("Enter Amount:")
        category=input("Enter category: ")
        date= datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, mode="a",newline="")as file:
            writer=csv.writer(file)
            writer.writerow([category,amount,date])

        print("Expense added successfully!\n")

def view_expenses():
    try:
        with open(FILE_NAME,mode="r") as file:
            reader=csv.reader(file)
            print("\n----Expenses----")
            for row in reader:
                print(f"Category: {row[0]}, Amount: ₹{row[1]}, Date: {row[2]}")
    except FileNotFoundError:
        print("No expenses found.\n")

def total_spent():
    total=0
    try:
        with open(FILE_NAME, mode="r") as file:
            reader=csv.reader(file)
            total+=float(row[1])
            print("\nTotal Spent: ₹ {total}\n")
    except FileNotFoundError:
        print("No expenses to calculate.\n")

def main():

    while True:
        print("\nWelcome to Expense Tracker \n")
        print("Main Menu:")
        print("1.Add Expenses")
        print("2.View Expenses")
        print("3.Total Spent")
        print("4.Exit")

        choice=input("Choose an option:")

        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            total_spent()
        elif choice=="4":
            break
        else:
            print("invalid choice \n")

if __name__=="__main__":
    main()