import pymysql

db = pymysql.Connect("localhost","root","root","world")
cursor = db.cursor()

class Mysql:

    @classmethod
    def insert(cls,taxnumber,taxname,date,area):
       sql = '''
       select * from `world`.`countrytax` where `taxnumber`="%s" and `taxname`="%s" and `date`="%s" and `area`="%s"
       '''  % (
           taxnumber,
           taxname,
           date,
           area
       )

       if cursor.execute(sql):
           return False

       sql = '''
        insert into `world`.`countrytax` ( `taxnumber`,`taxname`,`date`,`area`) 
        values ( "%s","%s","%s","%s")
       ''' % (
           taxnumber,
           taxname,
           date,
           area
       )
       result=False
       try:
           result = cursor.execute(sql)
           db.commit()
       except:
           db.rollback()
       return result

