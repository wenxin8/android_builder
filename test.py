from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com")

time.sleep(8)
driver.save_screenshot('screenshot.png')

# 关闭浏览器并退出
driver.quit()
