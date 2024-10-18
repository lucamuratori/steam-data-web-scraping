from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


PATH = r"C:/Users/luca/Desktop/python code/chromedriver-win64/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

ser = Service(PATH)

driver = webdriver.Chrome(service=ser, options=chrome_options)
driver.get(url="https://steamdb.info/")
time.sleep(5)


most_played_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/table/thead/tr/th[2]/a/span')
most_played_button.click()
time.sleep(3)

#grab the whole list
complete_table = driver.find_element(By.CLASS_NAME, "table-responsive")

#find the title of the list
table_title = complete_table.find_element(By.CLASS_NAME, "flex-grow").text

inner_table = complete_table.find_element(By.TAG_NAME, "tbody")
game_list = inner_table.find_elements(By.TAG_NAME, "tr")

game_dict_list = {
    "position": [],
    "name": [],
    "current users": [],
    "peak users 24": [],
    "peak users all time": []
}

#loop through games to get the position, name, current users, peak users in the last 24h and peak users of all time
for game in game_list:
    tds = game.find_elements(By.TAG_NAME, "td")
    game_dict_list["position"].append(tds[0].text)
    game_dict_list["name"].append(tds[2].find_element(By.TAG_NAME, "a").text)
    game_dict_list["current users"].append(tds[3].text)
    game_dict_list["peak users 24"].append(tds[4].text)
    game_dict_list["peak users all time"].append(tds[5].text)

df = pd.DataFrame(game_dict_list)
df.to_csv("games_csv.csv", index=False)

print("Proccess completed")



        
    