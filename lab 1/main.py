
from dao import *
from dao.doctor_assignement import DoctorAssignementDAO
from dao.illness import IllnessDAO
from model import *
import mysql.connector

connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pool",
                                                              pool_size=5,
                                                              host='localhost',
                                                              user='root',
                                                              password='password',
                                                              database='Hospital'
                                                              )

roles_dao = RoleDAO(connection_pool)
roles_dao.insert('user')
roles_dao.insert('admin')
roles_dao.insert('doctor')


user_dao = UserDAO(connection_pool)
user = User()
user.login = 'user'
user.password = 'qwerty'
user.role = 1
user_dao.insert(user)

user.login = 'admin'
user.password = 'qwerty'
user.role = 2
user_dao.insert(user)

user.login = 'doctor'
user.password = 'qwerty'
user.role = 3
user_dao.insert(user)

illness_dao = IllnessDAO(connection_pool)
illness = Illness()
illness.illness_name = 'injury'
illness.illness_type = '123'
illness.illness_description = 'Broken leg'
illness.user_id = 2
illness_dao.insert(illness)

illness.status = 'accepted'
illness.price = 120
illness.id = 1
illness_dao.update(illness)

illness.status = 'in-process'
illness_dao.update(illness)
works_dao = DoctorAssignementDAO(connection_pool)
works_dao.insert(3, 1)

feedback_dao = FeedbackDAO(connection_pool)
feedback = Feedback()
feedback.illness_id = 1
feedback.text = 'Leg works fine'
feedback.doctor_id = 3
feedback_dao.insert(feedback)

illness.status = 'healed'
illness_dao.update(illness)


