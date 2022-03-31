import requests
import json


def foo(host, port, **turners):
    # req = requests.get('http://' + host + ':' + str(port))

    with open('pepe.json', 'r', encoding='utf-8') as en:
        js = json.load(en)
        # print(js)
    dict_with_count = {}
    for i in js:
        ct = 0
        if type(js[i]) == list:

            for j in js[i]:
                if j.split('.')[1] != '1900':
                    ct += 1

        else:
            if js[i].split('.')[1] != '1900':
                ct += 1

        dict_with_count[i] = ct

    games = []
    for key in turners:
        elem = turners[key]
        for znach in dict_with_count:
            if znach in turners.keys() and dict_with_count[znach] == elem:

                games.append(znach)
    print(*games)

foo("127.0.0.1", 8800, Hawaii=2, Win=3)
