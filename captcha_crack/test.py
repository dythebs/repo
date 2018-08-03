import requests
import crack

print('start')
code_url = 'http://gongxianghoutai.aptdev.cn/ashx/createimg.ashx?id=htvalcode'
code_image = requests.get(code_url).content
print('ok')
print(crack.crack(code_image))