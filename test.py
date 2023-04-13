from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image
from pyzbar.pyzbar import decode
import time
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get("https://youtu.be/RCp9hnp7r6Q")

time.sleep(8)
driver.save_screenshot('screenshot.png')
qrcode_image = Image.open('screenshot.png')
qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
print(qrcode_info)
# 关闭浏览器并退出
driver.quit()
