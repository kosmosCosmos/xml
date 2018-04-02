import requests
import xmltodict
import json
from collections import Counter

aid = 21410363
req = requests.get('http://www.bilibili.com/widget/getPageList?aid=' + str(aid))
for cid in json.loads(req.text):
    tm = []
    if cid['page'] < 89:
        print(cid['page'])
        comments_page_url = 'http://comment.bilibili.com/' + str(cid['cid']) + '.xml'
        request = requests.get(comments_page_url)
        xml = xmltodict.parse(request.text)
        for data in xml['i']['d']:
            arr = data['@p'].split(",")[0]
            a = float(arr) // 60.0
            tm.append(int(a))
        counts = Counter(tm)
        data = sorted(counts.most_common(len(tm)))
        for x in range(1, len(data) - 1):
            if data[x][1] / data[x - 1][1] > 2 and data[x][1] / data[x + 1][1] > 2:
                print(x, data[x - 1][1], data[x][1], data[x + 1][1])
