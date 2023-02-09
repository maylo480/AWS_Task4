import csv
import os
import pprint
from data import work_days_calendar

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

pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(res_dict)
for i in res_list:
    print(i)
print(len(res_list))

with open('date_btcinusd.csv', 'w') as f:
    writer = csv.writer(f)
    for item in res_dict['2021']:
        # print(item)
        writer.writerow(item)
    for item in res_dict['2022']:
        writer.writerow(item)
