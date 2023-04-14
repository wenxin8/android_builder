from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

from PIL import Image
from pyzbar.pyzbar import decode
import time
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get("https://www.youtube.com/watch?v=RCp9hnp7r6Q")

time.sleep(15)


action_chains = ActionChains(driver)

action_chains.send_keys('k').perform()


time.sleep(15)
#1
driver.save_screenshot('screenshot.png')
qrcode_image = Image.open('screenshot.png')
try:
    qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
except IndexError:
    qrcode_info = ''  # 可以将 qrcode_info 设置为空字符串或其他默认值
    print('QR码图像处理失败')  # 打印一条错误信息
#qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
# 将 qrcode_info 写入到文本文件
with open('qrcode.txt', 'w', encoding='utf-8') as f:
    f.write(qrcode_info+ '\n')
#2
time.sleep(33)
driver.save_screenshot('screenshot.png')
qrcode_image = Image.open('screenshot.png')
try:
    qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
except IndexError:
    qrcode_info = ''  # 可以将 qrcode_info 设置为空字符串或其他默认值
    print('QR码图像处理失败')  # 打印一条错误信息
#qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
# 将 qrcode_info 写入到文本文件
with open('qrcode.txt', 'a', encoding='utf-8') as f:
    f.write(qrcode_info + '\n')
#3
time.sleep(33)
driver.save_screenshot('screenshot.png')
qrcode_image = Image.open('screenshot.png')
try:
    qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
except IndexError:
    qrcode_info = ''  # 可以将 qrcode_info 设置为空字符串或其他默认值
    print('QR码图像处理失败')  # 打印一条错误信息
#qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
# 将 qrcode_info 写入到文本文件
with open('qrcode.txt', 'a', encoding='utf-8') as f:
    f.write(qrcode_info + '\n')
#4
time.sleep(33)
driver.save_screenshot('screenshot.png')
qrcode_image = Image.open('screenshot.png')
try:
    qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
except IndexError:
    qrcode_info = ''  # 可以将 qrcode_info 设置为空字符串或其他默认值
    print('QR码图像处理失败')  # 打印一条错误信息
#qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
# 将 qrcode_info 写入到文本文件
with open('qrcode.txt', 'a', encoding='utf-8') as f:
    f.write(qrcode_info + '\n')
#5
time.sleep(33)
driver.save_screenshot('screenshot.png')
qrcode_image = Image.open('screenshot.png')
try:
    qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
except IndexError:
    qrcode_info = ''  # 可以将 qrcode_info 设置为空字符串或其他默认值
    print('QR码图像处理失败')  # 打印一条错误信息
#qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
# 将 qrcode_info 写入到文本文件
with open('qrcode.txt', 'a', encoding='utf-8') as f:
    f.write(qrcode_info + '\n')



with open('qrcode.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
#print(qrcode_info)


# 关闭浏览器并退出
driver.quit()
