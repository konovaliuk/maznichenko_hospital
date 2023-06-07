from model import *
from dao_interface import illness


class IllnessDAO(illness.IllnessIDAO):
    def __init__(self, connection_pool):
        self.connection_object = connection_pool.get_connection()
        self.mycursor = self.connection_object.cursor()

    def write(self, query, vals):
        try:
            self.mycursor.execute(query, vals)
            self.connection_object.commit()
        except Exception as e:
            print(e)
            print('Write error')

    def read(self, query, vals):
        try:
            self.mycursor.execute(query, vals)
            result = self.mycursor.fetchone()
            return result
        except Exception as e:
            print(e)
            print('Read error')

    def insert(self, illness: Illness):
        query = "INSERT INTO illness (illness_name, illness_type, illness_description, user_id, price)" \
                " VALUES (%s, %s, %s, %s, %s)"
        vals = (
            illness.illness_name, illness.illness_type, illness.illness_description, illness.user_id, illness.price)
        self.write(query, vals)

    def select(self, illness_id):
        query = "select * from users where login = %s and password = %s"
        vals = (illness_id,)
        return self.read(query, vals)

    def update(self, illness: Illness):
        query = 'UPDATE illness SET illness_name=%s, illness_type=%s, illness_description=%s,' \
                ' status=%s, user_id=%s, price=%s  WHERE id=%s'
        vals = (illness.illness_name, illness.illness_type, illness.illness_description, illness.status,
                illness.user_id, illness.price, illness.id)
        self.write(query, vals)

    def delete(self, illness_id):
        query = 'DELETE FROM illness WHERE id=%s'
        vals = (illness_id,)
        self.write(query, vals)
