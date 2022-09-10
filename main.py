
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

url = 'https://app.prizepicks.com/board'

driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="getting-started-sounds-good-btn"]')))
button = driver.find_element(By.XPATH, '//*[@id="getting-started-sounds-good-btn"]')
button.click()
button = driver.find_element(By.XPATH, '//*[@id="board"]/div[2]/div/div[2]/div/div[1]')
button.click()

stats = driver.find_elements(By.CLASS_NAME, 'stat ')
prop_list = []

for stat in stats:
    stat.click()
    props = driver.find_elements(By.CLASS_NAME, 'proj-container')

    for prop in props:
        playerName = prop.find_element(By.CLASS_NAME, 'name').text
        score = prop.find_element(By.CLASS_NAME, 'score').text
        category = prop.find_element(By.CLASS_NAME, 'text').text
        prop_item = {
            'Player Name': playerName,
            'Line': score,
            'Category': category
        }
        prop_list.append(prop_item)

df = pd.DataFrame(prop_list)
print(df)
df.to_csv("prizepicks.csv", index=False)
quit()