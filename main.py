import json
import csv

cat_dct = {}
with open('nn.csv') as dr:
    nn = list(csv.reader(dr))
    k = set(nn[0][0])

    for symbol in k:
        l1 = []
        for slov in nn[1:]:

            if symbol.lower() in slov[0].lower():

                l1.append(slov[0])
        l1 = sorted(l1, key=lambda x: (x.count(symbol), x))
        cat_dct[symbol] = l1

print(cat_dct)
with open('pepega.json', 'w', encoding='utf-8') as pp:
    json.dump(cat_dct, pp)


