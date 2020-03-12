from urllib.request import urlopen

url = 'https://github.com/fanfly/py-algo/raw/master/hw/judge.py'

res = urlopen(url)
with open(__file__, 'wb') as f:
    data = res.read()
    f.write(data)
