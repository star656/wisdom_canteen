from time import localtime, strftime
class sys_operation:
    # 实现获取时间戳的方法
    def get_shijianchuo(self):
        #获取当前系统时间
        sys_time = localtime()
        shijianchuo = strftime("%Y%m%d%H%M%S", sys_time)
        return shijianchuo


if __name__=="__main__":
    shijianchuo = sys_operation().get_shijianchuo()
    print(shijianchuo)