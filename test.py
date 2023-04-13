# 导入必要的库
from selenium import webdriver
import time
import base64
import re
from pyzbar.pyzbar import decode
from PIL import Image

# 创建浏览器对象
driver = webdriver.Chrome()

# 打开指定的网页
url = 'https://www.youtube.com/watch?v=RCp9hnp7r6Q'
driver.get(url)

# 暂停等待页面加载完成
time.sleep(5)

# 定位二维码元素并截图
qrcode_element = driver.find_element_by_xpath(
    '//img[contains(@class, "qr-image") and contains(@src, "data:image/png;base64")]'
)
qrcode_src = qrcode_element.get_attribute('src')
qrcode_data = re.sub('^data:image/.+;base64,', '', qrcode_src)
qrcode_bytes = base64.b64decode(qrcode_data)
with open('qrcode.png', 'wb') as f:
    f.write(qrcode_bytes)

# 解析二维码图片并显示结果
qrcode_image = Image.open('qrcode.png')
qrcode_info = decode(qrcode_image)[0].data.decode('utf-8')
print(qrcode_info)

# 关闭浏览器
driver.quit()
