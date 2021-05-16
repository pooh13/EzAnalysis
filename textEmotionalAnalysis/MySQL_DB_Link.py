import pyodbc

# print(pyodbc.drivers())

class MySQL_DB_Link(object):

    def __init__(self, host, port, database, user, password):
        connectInfo = 'Driver={MySQL ODBC 8.0 Unicode Driver};Server=%s; Port=%s; Database=%s; User=%s; Password=%s; Option=3;' % (
        host, port, database, user, password)

        self.connection = pyodbc.connect(connectInfo, unicode_results=True)
        self.cursor = self.connection.cursor()


# def __del__(self):
#     if self.cursor:
#         self.cursor.close()
#
#         self.cursor = None
#
#     if self.connection:
#         self.connection.close()
#
#         self.connection = None


# def destroy(self):
#     if self.cursor:
#         print(self.cursor, 'destroy cursor closed')
#
#         self.cursor.close()
#
#         self.cursor = None
#
#     if self.connection:
#         self.connection.close()
#
#         self.connection = None

    # 獲取全部查詢結果
    def query(self, sql):
        self.cursor.execute(sql)

        return self.cursor.fetchall()


    # 獲取查詢條數
    def count(self, sql):
        self.cursor.execute(sql)

        return self.cursor.fetchone()[0]


    def execute(self, sql):
        count = self.cursor.execute(sql).rowcount
        self.connection.commit()

        return count

# MySQL_localtest
MySQLConnectInfo = MySQL_DB_Link('localhost', '3306', 'localtest', 'root', 'mysql')
MySQLConnectInfoStr = ['localhost', '3306', 'localtest', 'root', 'mysql']

# MySQL_localDjango
# MySQLConnectInfo = MySQL_DB_Link('localhost', '3306', 'diary', 'root', 'mysql')

# test
# list = MySQLConnectInfo.query('select * from localtest.test')
# list = MySQLConnectInfo.count('select * from localtest.test')

# print(list)
