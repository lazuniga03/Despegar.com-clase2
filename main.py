""""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.us.despegar.com/flights/UIO/AGP?from=SB&di=1-0&reSearch=true")
#driver.get("http://www.python.org")
fligths_panel=driver.find_element(Byc¿.CLASS_NAME, "cluster-container")

for f in fligths:
    airline_name = f.find_element(by=By.CLASS_NAME, value="img").accessible_name
    departure = f.find_element(by=By.CLASS_NAME, value="cluster-part-0").text
    arrival = f.find_element(by=By.CLASS_NAME, value="cluster-part-1").text
    days = f.find_element(by=By.CLASS_NAME, value="quantity-days").text

    print(airline_name)
    print(departure)
    print(days)
    print('=')


assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from mongo import MongoConnection


db_client = MongoConnection().client
db = db_client.get_database('despegar')
col = db.get_collection('flights')

driver = webdriver.Chrome()
driver.get("https://www.us.despegar.com/flights/UIO/AGP?from=SB&di=1-0&reSearch=true")
flights = driver.find_elements(By.CLASS_NAME, "cluster-container")
for f in flights:
    airline_name = f.find_element(by=By.TAG_NAME, value="img").accessible_name
    departure = f.find_element(by=By.CLASS_NAME, value="cluster-part-0").text
    arrival = f.find_element(by=By.CLASS_NAME, value="cluster-part-1").text
    days = f.find_element(by=By.CLASS_NAME, value="quantity-days").text
    price = f.find_element(by=By.CLASS_NAME, value="price").text

    document = {
        "airline": airline_name,
        "depature": departure,
        "arrival": arrival,
        "days": days,
        "price": price
    }

    col.insert_one(document=document)


    print(airline_name)
    print(departure)
    print(arrival)
    print(days)
    print(price)
    print('=' * 40)


driver.close()