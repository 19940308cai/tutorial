from tutorial.model.basemodel import BaseModel
import requests

class iptable(BaseModel):

    def __init__(self):
        super(iptable, self).__init__("iptable")

    def getProxy(self):
        sql = """ 
                     SELECT * FROM `%s`.`%s` ORDER BY RAND() LIMIT 1 
                     """ \
                     % (
            self.database,
            self.tableName,
        )
        self.handle.execute(sql)
        data   = self.handle.fetchone()
        if data is None:
            return False
        result = self._jup(data[1],data[2],data[3])
        print("hahah:",result)
        if result is False:
            self.getProxy()
        else:
            print("hahah1:", result)
            return result

    def _jup(self,ip,schema,port):
        result=False
        try:
            proxy=schema + "://" + ip + ":" + port
            proxy_dict = {"http":proxy}
            response = requests.get("http://47.92.119.35/service/window/index", proxies=proxy_dict,timeout=15)
            if response.status_code == 200:
                if response.text != ip :
                    self._deleteProxy(ip, schema, port)
                else:
                    return proxy
            else:
                self._deleteProxy(ip, schema, port)
        except:
            self._deleteProxy(ip,schema,port)
        return result


    def _deleteProxy(self,ip,schema,port):
        #从数据库中删除无效的ip
        delete_sql = """
            DELETE FROM `%s`.`%s` WHERE `ip`="%s" AND `schema`="%s" AND `port`="%s"
        """ % (
            self.database,
            self.tableName,
            ip,
            schema,
            port,
        )
        self.handle.execute(delete_sql)
        self.db.commit()
        return True



if __name__ == '__main__':
    m = iptable()
    data = m.getProxy()
    print(data)
    pass
