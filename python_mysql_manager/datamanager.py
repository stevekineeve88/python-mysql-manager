import mysql.connector

# Manages MySQL queries to database with container result
from python_mysql_manager.datacontainer import DataContainer


class DataManager:
    __SELECT = "Select"
    __INSERT = "Insert"
    __UPDATE = "Update"
    __DELETE = "Delete"
    __QUERY = "Query"

    def __init__(self, config):
        self.__mysql = mysql.connector.connect(
            host=config["host"],
            port=config["port"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

    def select(self, sql: str, values: tuple = ()) -> DataContainer:
        return self.__query(sql, values, self.__SELECT)

    def insert(self, sql: str, values: tuple = ()) -> DataContainer:
        return self.__query(sql, values, self.__INSERT)

    def update(self, sql: str, values: tuple = ()) -> DataContainer:
        return self.__query(sql, values, self.__UPDATE)

    def delete(self, sql: str, values: tuple = ()) -> DataContainer:
        return self.__query(sql, values, self.__DELETE)

    def getConnection(self) -> mysql.connector:
        return self.__mysql

    def __query(self, sql: str, values: tuple, query: str = __QUERY) -> DataContainer:
        cursor = self.__mysql.cursor()
        try:
            cursor.execute(sql, values)
            if query != self.__SELECT:
                self.__mysql.commit()
            container = DataContainer(True)
            if query == self.__SELECT:
                container.setData(cursor.fetchall())
            if query == self.__INSERT:
                container.setLastInsertId(cursor.lastrowid)
            cursor.close()
            return container
        except mysql.connector.Error as err:
            cursor.close()
            return DataContainer(False, err.msg, err.errno)
