import csv
import os
from data import work_days_calendar
from copy import deepcopy

cwd = os.getcwd()
marketdata_path = '/monthly_data/marketdata'
csv_path = os.path.join(cwd+marketdata_path)
print(csv_path)
month = 0
day = 0
res_dict = {
    '2021': [],
    '2022': []
}
res_list = []
csv_files = os.listdir(csv_path) 
print(sorted(csv_files))
for file in sorted(csv_files):
    month += 1
    day = 0
    with open (f"{csv_path}/{file}") as f:
        reader = csv.reader(f)
        for row in reader:
            day += 1
            if month <= 12:
                res_dict['2021'].append((f'21{month:02}{day:02}', (row[1])))
                res_list.append((f'21{month:02}{day:02}', (row[1])))
            else:
                res_dict['2022'].append((f'22{month-12:02}{day:02}', (row[1])))
                res_list.append((f'22{month-12:02}{day:02}', (row[1])))

with open('date_btcinusd.csv', 'w') as f:
    writer = csv.writer(f)

    for item in res_dict['2021']:
        # print(item)
        writer.writerow(item)
    for item in res_dict['2022']:
        writer.writerow(item)

#===========================================================================================================

valid_calendar = work_days_calendar()
for j in valid_calendar:
    print(j)

our_days_btcinusd = []
with open ('date_btcinusd.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] in valid_calendar:
            our_days_btcinusd.append([row[0], row[1]])

for i in our_days_btcinusd:
    print(i)
print(len(our_days_btcinusd))

def multiply_two_strings(a,b):
   product = float(a) * float(b)
   return(product)

our_days_btcinpln = deepcopy(our_days_btcinusd)
with open ('USD_PLN_courses.csv', 'r') as f:
    i = 0
    reader = csv.reader(f)
    for row in reader:
        print(f"Row = {row[0]}, list = {our_days_btcinpln[i][1]}")
        our_days_btcinpln[i][1] = multiply_two_strings(row[0], our_days_btcinpln[i][1])
        i += 1

for i in our_days_btcinusd:
    i[0] = '20'+i[0]

for i in our_days_btcinpln:
    i[0] = '20'+i[0]

with open('valid_date_btc_to_usd.csv', 'w') as f:
    writer = csv.writer(f)
    for item in our_days_btcinusd:
        writer.writerow(item)

with open('valid_date_btc_to_pln.csv', 'w') as f:
    writer = csv.writer(f)
    for item in our_days_btcinpln:
        writer.writerow(item)

for i in our_days_btcinpln:
    i[0] = '20'.join(i[0])
    