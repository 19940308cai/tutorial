import pymysql,os
from configparser import ConfigParser

class BaseModel:

    db=None
    tableName=None

    def __init__(self,table):
        configer = ConfigParser()
        configer.read("/Users/caijiang/tutorial/tutorial/db.ini")
        self.tableName = table
        self.database  = configer.get("db", "database")
        self.db = pymysql.Connect(
                             configer.get("db", "host"),
                             configer.get("db", "dbusername"),
                             configer.get("db", "dbpassword"),
                             self.database)
        self.handle=self.db.cursor()

    def insert(self,element):
        keyTmp=""
        valueTmp=""

        for key in element:
            keyTmp += "`"+str(key)+"`,"
            valueTmp += "'"+str(element[key])+"',"

        keyTmp  = keyTmp.rstrip(",")
        valueTmp=valueTmp.rstrip(",")

        sql = '''
        INSERT INTO `%s`.`%s` ( %s ) values ( %s )
        ''' % (
            self.database,
            self.tableName,
            keyTmp,
            valueTmp
        )
        try:
            self.handle.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False


    def selectAllDataByCondition(self, condition=[], limit=[]):
        if not condition:
            sql = '''
            SELECT * FROM `%s`.`%s`
            ''' % (
                self.database,
                self.tableName,
            )
        else:
            where = " WHERE "
            for value in condition:
                where += "`" + str(value[0]) + "`" + str(value[1]) + "'" + str(value[2]) + "' AND "
            where = where.rstrip().rstrip("AND")
            sql = '''
            SELECT * FROM `%s`.`%s` %s
            ''' % (
                self.database,
                self.tableName,
                where
            )
        if limit:
            if len(limit) > 1:
                sql+=" LIMIT "+str(limit[0])+","+str(limit[1])
            else:
                sql += " LIMIT " +str(limit[0])
        self.handle.execute(sql)
        return self.handle.fetchall()


    def selectOneDataByCondition(self, condition=[]):
        if not condition:
            sql = '''
            SELECT * FROM `%s`.`%s`
            ''' % (
                self.database,
                self.tableName,
            )
        else:
            where = " WHERE "
            for value in condition:
                where += "`" + str(value[0]) + "`" + str(value[1]) + "'" + str(value[2]) + "' AND "
            where = where.rstrip().rstrip("AND")
            sql = '''
            SELECT * FROM `%s`.`%s` %s
            ''' % (
                self.database,
                self.tableName,
                where
            )
        self.handle.execute(sql)
        return self.handle.fetchone()
