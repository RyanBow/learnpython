import urllib.request


# 注意 1056,修改这个数字得到其他视频集
jsonurl = "https://bangumi.bilibili.com/jsonp/seasoninfo/1056.ver?callback=seasonListCallback&jsonp=jsonp"

data = urllib.request.urlopen(jsonurl).read()

first = str(data).index("{")

last = str(data).rindex("}")
json_data = data[first:last+1]

print(json_data)

# j = json.loads(json_data)
# list = j['result']['episodes']
#
# for item in list:
#     print(item['index']," ",item['index_title']," ",item['webplay_url'])