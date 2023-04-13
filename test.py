from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# 创建 Chrome 浏览器 Headless 实例
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # 禁用 GPU 加速
driver = webdriver.Chrome(chrome_options=chrome_options)

# 创建 Firefox 浏览器 Headless 实例
firefox_options = FirefoxOptions()
firefox_options.add_argument('-headless')  # 注意这里是单破折号
driver = webdriver.Firefox(firefox_options=firefox_options)

# 访问目标网页并保存截图
driver.get('https://www.example.com')
driver.save_screenshot('screenshot.png')

# 关闭浏览器并退出
driver.quit()
