from dao_interface import RoleIDAO


class RoleDAO(RoleIDAO):
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

    def insert(self, role_name):
        query = "INSERT INTO roles (name)" \
                " VALUES (%s)"
        vals = (role_name,)
        self.write(query, vals)

    def select(self, role_id):
        query = "select * from roles where id=%s"
        vals = (role_id,)
        return self.read(query, vals)

    def update(self, role_name, role_id):
        query = 'UPDATE roles SET name=%s WHERE id=%s'
        vals = (role_name, role_id)
        self.write(query, vals)

    def delete(self, role_id):
        query = 'DELETE FROM roles WHERE id=%s'
        vals = (role_id,)
        self.write(query, vals)
