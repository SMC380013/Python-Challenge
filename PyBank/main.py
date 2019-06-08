import os, csv

csv_path = os.path.join("Resources", "budget_data.csv")

date=[]
profitloss=[]

with open(csv_path, newline="", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

csv_header = next(csv_reader)

    for row in csv_reader:
        date.append(row[0])
        profitloss.append(row[1])

#def data (bank_data):
    #date = bank_data[0]
    #profitandloss = int(bank_data[1])

    total_months= len(date)
    net= sum(profitandloss)
    average=
    dateincrease=
    datedecrease=
    amtincrease=
    amtdecrease=

print("Financial Analysis")
print("-" * 12)


print(f"Total Months: {total_months}")
print(f"Total: {net}")
print(f"Average Change: {average}")
print(f"Greatest Increase in profits: {dateincrease} {amtincrease}")
print(f"Greatest Decrease in profits: {datedecrease} {amtdecrease}")

final= all print statements


output_file = os.path.join("bankoutput.csv")

with open(output_file, "w", newline="", encoding="utf8") as csv_file:
    
    csv_writer = csv.writer(csv_file, delimiter=",")

    csv_writer.writerows(final)

