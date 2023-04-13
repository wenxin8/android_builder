import requests
from PIL import Image
from io import BytesIO

# 获取网页内容
url = "https://www.youtube.com/watch?v=RCp9hnp7r6Q"
response = requests.get(url)

# 将网页内容转为二进制流
stream = BytesIO(response.content)

# 打开图片并创建 Image 对象
img = Image.open(stream)

# 裁剪、缩放等操作（可选）

# 保存图片
img.save("screenshot.png")
