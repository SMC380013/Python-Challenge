import os, csv

csv_path = os.path.join("..", "Resources", "budget_data.csv")

date=[]
profitloss=[]

with open(csv_path, newline="", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #print (csv_reader)

    csv_header = next(csv_reader)
    previous_value_row = next(csv_reader)
    #print(previous_value_row)
    date.append(previous_value_row[0])
    previous_value = previous_value_row[1]
    greatest_profit = 0
    greatest_loss = 0
    best_month = ""
    worst_month = ""
    totalprofit= 0
    totalloss= 0
    profitcalc= 0
    totalprofitloss= 0

    for row in csv_reader:
# to calculate change in p/l month over month
        date.append(row[0])
        value= int(row[1])-int(previous_value)
        profitloss.append(value)
        previous_value = (row[1])

#print(date)
#print(profitloss)
#below is to get the greatest profit and loss date and change
        if value>greatest_profit:
            greatest_profit = value
            best_month = row[0]
        elif value<greatest_loss:
            greatest_loss = value
            worst_month = row[0]
#print(best_month, worst_month)

#for totalprofitloss
        profitcalc = int(row[1])
        if profitcalc > 0:
            totalprofit += profitcalc
        elif profitcalc < 0:
            totalloss += profitcalc
        totalprofitloss = totalprofit + totalloss 

finaltotalpl= totalprofitloss+ int(row[1])     
#print(finaltotalpl)   

total_months= len(date) 
max_profit= max(profitloss)
min_profit= min(profitloss)
average= sum(profitloss)/(total_months - 1)

print("Financial Analysis")
print("-" * 20)
print(f"Total Months: {total_months}")
print(f"Total: {finaltotalpl}")
print(f"Average: {average}")
print(f"Greatest increase in profits: {best_month} ({max_profit})")
print(f"Greatest decrease in profits: {worst_month} ({min_profit})")


# with open("Output.txt", "w", newline="") as output:
    
