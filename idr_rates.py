import requests

#json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.8354476434761e-5,"date":"Sat, 31 Oct 2020 11:00:01 GMT","inverseRate":14629.619772663},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.8505225223501e-5,"date":"Sat, 31 Oct 2020 11:00:01 GMT","inverseRate":17092.490391752}}

#print(json_data.json())
print(json_data)

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
