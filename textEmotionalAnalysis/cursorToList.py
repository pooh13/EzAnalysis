import MySQL_DB_Link
import toList

def cursorToList(cursorToListResult):
    cursorToListResult = MySQL_DB_Link.MySQL_DB_Link(MySQL_DB_Link.MySQLConnectInfoStr[0],
                                                     MySQL_DB_Link.MySQLConnectInfoStr[1],
                                                     MySQL_DB_Link.MySQLConnectInfoStr[2],
                                                     MySQL_DB_Link.MySQLConnectInfoStr[3],
                                                     MySQL_DB_Link.MySQLConnectInfoStr[4],).query(cursorToListResult)

    cursorToList = toList.toList(cursorToListResult)

    return cursorToList
