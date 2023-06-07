from model import *
from dao_interface import illness


class IllnessDAO(illness.IllnessIDAO):
    def __init__(self, connection_pool):
        self.connection_object = connection_pool.get_connection()
        self.mycursor = self.connection_object.cursor()

    def write(self, query, vals):
        self.mycursor.execute(query, vals)
        self.connection_object.commit()
        return self.mycursor.lastrowid

    def read(self, query, vals):
        self.mycursor.execute(query, vals)
        result = self.mycursor.fetchone()
        return result

    def insert(self, illness: Illness):
        query = "INSERT INTO illness (illness_name, illness_type, illness_description, user_id, price)" \
                " VALUES (%s, %s, %s, %s, %s)"
        vals = (
            illness.illness_name, illness.illness_type, illness.illness_description, illness.user_id, illness.price)
        self.write(query, vals)

    def select(self, illness_id):
        query = "select * from illness where id=%s"
        vals = (illness_id,)
        return self.read(query, vals)

    def update_all(self, illness: Illness):
        query = 'UPDATE illness SET illness_name=%s, illness_type=%s, illness_description=%s,' \
                ' status=%s, user_id=%s, price=%s  WHERE id=%s'
        vals = (illness.illness_name, illness.illness_type, illness.illness_description, illness.status,
                illness.user_id, illness.price, illness.id)
        self.write(query, vals)

    def update_status(self, illness_id, status):
        query = 'UPDATE illness SET status=%s WHERE id=%s'
        vals = (status, illness_id)
        self.write(query, vals)

    def delete(self, illness_id):
        query = 'DELETE FROM illness WHERE id=%s'
        vals = (illness_id,)
        self.write(query, vals)

    def read_all(self):
        query = "select * from illness"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def read_by_status(self, status):
        query = "select * from illness WHERE status=%s"
        vals = (status, )
        self.mycursor.execute(query, vals)
        return self.mycursor.fetchall()

    def read_by_user_id(self, user_id):
        query = "select * from requests WHERE user_id=%s"
        vals = (user_id,)
        self.mycursor.execute(query, vals)
        return self.mycursor.fetchall()

    def read_healed(self, user_id):
        query = "SELECT * FROM illness WHERE user_id=%s AND status='healed'"
        vals = (user_id, )
        self.mycursor.execute(query, vals)
        return self.mycursor.fetchall()
