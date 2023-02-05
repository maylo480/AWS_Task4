import requests
import xml.etree.ElementTree as ET
from data import work_days_calendar

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

# URL_template = f"https://static.nbp.pl/dane/kursy/xml/a{table_no}z{date_no}.xml"
    response = requests.get(URL_template)
    with open(f'data/{tab}.xml', 'wb') as f:
        f.write(response.content)
    tree = ET.parse(f'data/{tab}.xml')
    root = tree.getroot()
    usd1 = root[3][3].text
    kursy_dolara.append(usd1)
    # print(root[3][3].text)
print(f">>>{kursy_dolara}")