import pymysql

from Src.Common.CSV import csv


class mysql:
    # 连接 mysql数据库，执行sql语句
    def connect_mysql_and_execute_sql(self, ip, port_number, username,password, database_name, sql):
       #连接数据
        db = pymysql.connect(host=ip, port=port_number, user=username,
                        password=password, database=database_name, charset="utf8")
        # 创建一个游标
        cur = db.cursor()
        cur.execute(sql)  # 执行sql语句
        db.commit()  # 语句执行后生效
        data = cur.fetchall()  # 接受所有返回的数据
        cur.close()  # 关闭游标
        db.close()  # 关闭数据可
        return data


if __name__=="__main__":
    database_info = csv().get_info_from_csv_to_dict('../../Conf/DataBaseConf.csv')
    print(database_info)
    sql = "SELECT * FROM access_record_temp WHERE employee_name = '薛博兴'"
    # sql = 'update oa_tbl_employee set 8password="MD50B1A732C1DF34A6A" where LoginID = "sup" '
    r = mysql().connect_mysql_and_execute_sql(ip=database_info["Host_IP"], port_number=int(database_info['Port']),
                                          username=database_info["UserName"],password=database_info['Password'],
                                          database_name=database_info["DataBase_name"],sql=sql)
    print(r)
    print(r[0])
    print(r[0][2])
