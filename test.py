from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com")


driver.save_screenshot('screenshot.png')

# 关闭浏览器并退出
driver.quit()
