import requests
import xml.etree.ElementTree as ET
from data import work_days_calendar
import csv
import pandas as pd

kursy_dolara = []
table_no = "001"
date_no = "210104"
valid_calendar = work_days_calendar()
for tab in range(1, 507):  
    if tab < 255:  
        if tab < 10:
            URL_template = f"https://static.nbp.pl/dane/kursy/xml/a00{tab}z{valid_calendar[tab-1]}.xml"
        elif tab < 100:
            URL_template = f"https://static.nbp.pl/dane/kursy/xml/a0{tab}z{valid_calendar[tab-1]}.xml"
        else:
            URL_template = f"https://static.nbp.pl/dane/kursy/xml/a{tab}z{valid_calendar[tab-1]}.xml"
    else:
        if tab-254 < 10:
            URL_template = f"https://static.nbp.pl/dane/kursy/xml/a00{tab-254}z{valid_calendar[tab-1]}.xml"
        elif tab-254 < 100:
            URL_template = f"https://static.nbp.pl/dane/kursy/xml/a0{tab-254}z{valid_calendar[tab-1]}.xml"
        else:
            URL_template = f"https://static.nbp.pl/dane/kursy/xml/a{tab-254}z{valid_calendar[tab-1]}.xml"       

# URL_template = f"https://static.nbp.pl/dane/kursy/xml/a{table_no}z{date_no}.xml"4.4100
    # response = requests.get(URL_template)
    # with open(f'data/{tab}.xml', 'wb') as f:
    #     f.write(response.content)
    tree = ET.parse(f'data/{tab}.xml')
    root = tree.getroot()
    usd1 = root[3][3].text
    usd1_dot = usd1.replace(',', '.')
    kursy_dolara.append(usd1_dot)
    header = ['USD to PLN']
    # print(root[3][3].text)
print(f">>>{kursy_dolara}")

with open("USD_PLN_courses.txt", "w") as f:
    for i in kursy_dolara:
        f.write(i)
        f.write(', ')

kursy_dolara_float = []
for i in kursy_dolara:
    kursy_dolara_float.append(float(i))

df = pd.DataFrame(kursy_dolara_float)
df.to_csv("file2.csv", index=False, header=False)