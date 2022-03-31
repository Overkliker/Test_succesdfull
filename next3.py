import sqlite3


conn = sqlite3.connect('places.db')


class Attraction:
    def __init__(self, city):
        self.city = city
        cur = conn.cursor()
        self.id = cur.execute(f'SELECT id FROM towns WHERE towns.town = "{city}"').fetchone()[0]

    def count_att(self):
        cur = conn.cursor()
        cur.execute(f'SELECT name FROM registry WHERE registry.town_id = {self.id}')
        return [i[0] for i in cur.fetchall()]

    def get_att(self, type):
        cur = conn.cursor()
        id_temp = cur.execute(f'SELECT id FROM attractions WHERE attractions.type = "{type}"').fetchone()[0]
        cur.execute(f'SELECT name FROM registry WHERE (registry.town_id = {self.id}) and (registry.type_id = {id_temp})')
        return [i[0] for i in cur.fetchall()]

    def get_ex(self, price):
        cur = conn.cursor()
        cur.execute(f'SELECT name, cost, duration FROM registry WHERE registry.cost <= {price}')
        return sorted([i for i in cur.fetchall()], key=lambda x: (x[1], -x[2]))


at = Attraction('Delhi')
print(at.count_att())
print(at.get_att('building'))
print(at.get_ex(200))