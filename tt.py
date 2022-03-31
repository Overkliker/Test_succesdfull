import csv

with open('name.csv', 'r') as reader:
    crabs = csv.DictReader(reader, delimiter=';')
    crabs_spells = {}
    for i in crabs:
        print(i)
        if i["color"] not in crabs_spells:
            crabs_spells[i["color"]] = [[int(i["size"]), int(i['shell thickness'])]]

        else:
            crabs_spells[i["color"]] += [[int(i["size"]), int(i['shell thickness'])]]

    print(crabs_spells)

    for i in crabs_spells:
        print(crabs_spells[i])
        crabs_spells[i] = sorted(crabs_spells[i], key=lambda x: (-x[0], -x[1]))

    print(crabs_spells)