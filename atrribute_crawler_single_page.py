import pickle
import urllib3
from bs4 import BeautifulSoup

condcol = ['押金', '車 位', '管理費', '最短租期', '身份要求', '開伙', '養寵物', '身分要求', '性別要求', '朝向', '格局', '產權登記']


rentDf = pickle.load(open("./data/rent_table.dat", "rb"))
http = urllib3.PoolManager()

url_list = "https://rent.591.com.tw/rent-detail-6247236.html"

response = http.request('GET', url_list)
soup = BeautifulSoup(response.data, "lxml")

print("---------------------------------------------------------------")

try:
    price_box = soup.find('div', attrs={'class': 'price clearfix'})
    price_box = price_box.get_text().strip()
    print(price_box)
except AttributeError:
    print("None")

try:
    explain_box = soup.find('ul', attrs={'class': 'attr'})
    explain = explain_box.findAll('li')
    # for item in explain:
    #     item = item.get_text()
    #     item_name = item.split('：')[0]
    #     item_explain = item.split('：')[1]
    #     print(item)

    explain_box = explain_box.get_text().strip()
    print(explain_box)
except AttributeError:
    print("None")

try:
    address_box = soup.find('span', attrs={'class': 'addr'})
    address_box = address_box.get_text().strip()
    print(address_box)
except AttributeError:
    print("None")

try:
    condition_box = soup.find('ul', attrs={'class': 'clearfix labelList labelList-1'})
    condition = condition_box.findAll('li')
    for item in condition:
        item = item.get_text()
        item_name = item.split('：')[0]
        item_content = item.split('：')[1]
        print(item)
        if item_name in condcol:
            rentDf.ix[0,item_name]=item_content

except AttributeError:
    print("None")

try:
    facility_box = soup.find('ul', attrs={'class': 'facility clearfix'})
    facility_box = facility_box.find_all('li', class_='clearfix')
    for i in range(0, len(facility_box)):
        li = []
        if 'no' in str(facility_box[i]):
            print(facility_box[i].get_text())
        else:
            li.append(i)
        print(li)
except AttributeError:
    print("None")

try:
    life_box = soup.find('div', attrs={'class': 'lifeBox'})
    life_box = life_box.get_text().strip()
    print(life_box)
except AttributeError:
    print("None")


def transportation_box():
    MRT = "捷運站"
    TRAIN = "火車站"
    transportation = [life_box.find(MRT), life_box.find(TRAIN)]
    print(transportation)


transportation_box()
