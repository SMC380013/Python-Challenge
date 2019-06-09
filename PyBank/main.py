import os, csv

csv_path = os.path.join("..", "Resources", "budget_data.csv")

date=[]
profitloss=[]

with open(csv_path, newline="", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print (csv_reader)

    csv_header = next(csv_reader)

    for row in csv_reader:
        date.append(row[0])
        profitloss.append(row[1])
#print(date)
#print(profitloss)

total_months= len(date) 
max_profit= max(profitloss)
min_profit= min(profitloss)

totalprofit=0
totalloss=0
profitcalc=0
totalprofitloss=0

increase_date=0
greatestincrease=0
decreate_date=0
greatestdecrease=0

#for row in csv_reader
profitcalc = int(row[1])
if profitcalc > 0:
    totalprofit += profitcalc
elif profitcalc < 0:
    totalloss += profitcalc
totalprofitloss = totalprofit - totalloss

#for greatest increase date
# increase_date= (row[0])
# if row[1] = max_profit:
#     greatestincrease= increase_date
# else increase_date=0

# #for greatest decreate date
# decrease_date=(row[0])
# if row[1] = min_profit:
#     greatestdecrease= decrease_date
# else decrease_date=0


print("Financial Analysis")
print("-" * 20)
print(f"Total Months: {total_months}")
print(f"Total: {totalprofitloss}")
print(f"Greatest increase in profits: {max_profit}")
print(f"Greatest decrease in profits: {min_profit}")
# print(f"Greatest Increase in profits: {greatestincrease} {max_profit}")
# print(f"Greatest Decrease in profits: {greatestdecrease} {amtdecrease}")


# output_file = os.path.join("bankoutput.csv")

# with open(output_file, "w", newline="", encoding="utf8") as csv_file:
    
#     csv_writer = csv.writer(csv_file, delimiter=",")

#     csv_writer.writerows(f"inal)

