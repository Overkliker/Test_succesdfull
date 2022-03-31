import argparse
import csv

from flask import Flask, jsonify

parser = argparse.ArgumentParser()
parser.add_argument('--server', type=str)
parser.add_argument('--port', type=str)
parser.add_argument('--file', type=str)
res = parser.parse_args()


app = Flask(__name__)


def dict_spawner(f_name):
    with open('name.csv', 'r') as reader:
        crabs = csv.DictReader(reader, delimiter=';')
        crabs_spells = {}
        for i in crabs:
            print(i)
            if i["color"] not in crabs_spells:
                crabs_spells[i["color"]] = [[int(i["size"]), int(i['shell thickness'])]]

            else:
                crabs_spells[i["color"]] += [[int(i["size"]), int(i['shell thickness'])]]

        for i in crabs_spells:
            crabs_spells[i] = sorted(crabs_spells[i], key=lambda x: (-x[0], -x[1]))

    return crabs_spells

@app.route('/firecrab')
def index():
    dt = dict_spawner(res.file)
    return jsonify(dt)


if __name__ == '__main__':
    app.run(host=res.server, port=res.port)