from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from PIL import Image
from pyzbar.pyzbar import decode
import time
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get("https://www.youtube.com/watch?v=RCp9hnp7r6Q")

time.sleep(10)
player = driver.find_element_by_xpath('//*[@id="movie_player"]/div[1]/video')

action_chains = ActionChains(driver)
action_chains.move_to_element(player).perform()
action_chains.send_keys('k').perform()


time.sleep(10)

driver.save_screenshot('screenshot.png')
qrcode_image = Image.open('screenshot.png')
qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
print(qrcode_info)


# 关闭浏览器并退出
driver.quit()
