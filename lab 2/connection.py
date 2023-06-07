import mysql.connector
import os


def get_pool():
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pool",
                                                                  pool_size=5,
                                                                  host='localhost',
                                                                  user='root',
                                                                  password='password',
                                                                  database='Hospital'
                                                                  )
    return connection_pool
