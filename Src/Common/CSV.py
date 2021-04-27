
class csv():
   # 读取csv文件中的数据，filepath参数表示csv文件的路径名称及格式组成的字符串
    def  get_info_from_csv(self,filepath):
        with open(filepath, 'r') as f:
            # f = open(filepath, "r")  # 以读的方式打开文件
            info = f.readlines()  # 读取文件内所有内容
            f.close()
            return info

   # 读取csv文件中的数据并转换为字典
    def  get_info_from_csv_to_dict(self, filepath):
        info_list = self.get_info_from_csv(filepath)  # 读取了文件中的数据，得到一个列表
        info_dict ={}  # 定义空字典
        for info in info_list:  # 遍历数据列表
            i_list = info.strip("\n").split(",")  # 去除列表中字符串的换行符再以逗号分隔字符串得到一个列表
            info_dict[i_list[0]] = i_list[1]  # 将i_list 中的第一个元素和第二个元素作为键值对添加到字典中
        return info_dict

   # 按照键读取数据中的值
    def get_info_from_csv_by_key(self, filepath, key):
        info_dict = self.get_info_from_csv_to_dict(filepath)
        return info_dict[key]

   # 从测试数据文件中按照用例编号读取测试数据，得到测试数据字典
    def get_testdata_from_csv_by_testcase_number(self,filepath, testcase_number):
        td_list = self.get_info_from_csv(filepath)  # 读取测试数据得到测试数据列表
        title_line =  td_list.pop(0)  #弹出测试数据中的输入项那一行,弹出的数据用变量title_line表示
        title_list = title_line.strip('\n').split(",")  #将测试数据中的输入项哪一行分隔为一个列表
        td_dict = {}  # 定义空字典
        # 遍历测试数据列表
        for td in td_list:
            if testcase_number in td:  # 判断用例编号是否在测试数据中
                td_list_number = td.strip("\n").split(",")  # 将测试数据分隔为列表，使用td_list_number表示
                for input_data_index in range(1,len(td_list_number)):  #input_data_index表示td_list_number列表的索引
                    td_dict[title_list[input_data_index]]= td_list_number[input_data_index]
                break  # 终止测试数据列表遍历
        return td_dict










if __name__=="__main__":
    l = csv().get_info_from_csv('../../Conf/TestEnvironmentConf.csv')
    print(l)
    info = csv().get_info_from_csv_to_dict('../../Conf/TestEnvironmentConf.csv')
    print(info)
    # v = csv().get_info_from_csv_by_key('../../Conf/TestEnvironmentConf.csv', "UserName")
    # print(v)
    # td_dict = csv().get_testdata_from_csv_by_testcase_number("../Modules/QT/TestData/FBGGTestData.csv", "FBGG_001")
    # print(td_dict)