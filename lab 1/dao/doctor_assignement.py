from dao_interface import doctor_assignement


class DoctorAssignementDAO(doctor_assignement.DoctorAssignementIDAO):
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

    def insert(self, user_id, request_id):
        query = "INSERT INTO doctor_assignements(user_id, illness_id) VALUES (%s, %s)"
        vals = (user_id, request_id)
        self.write(query, vals)

    def select(self, work_id):
        query = "select * from doctor_assignements where id=%s"
        vals = (work_id,)
        return self.read(query, vals)

    def update(self, user_id, request_id):
        query = 'UPDATE doctor_assignements SET user_id=%s, illness_id=%s WHERE id=%s'
        vals = (user_id, request_id)
        self.write(query, vals)

    def delete(self, work_id):
        query = 'DELETE FROM roles WHERE id=%s'
        vals = (work_id,)
        self.write(query, vals)
