import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os

from Src.Common.CSV import csv


class send_email(csv):

    # #设置登录邮箱数据
    # smtp_server = 'smtp.163.com'
    # sender = '18829789573@163.com'
    # pwd = 'ZFSRZZXLCZEFMRVO'
    # receivers = ['18829789573@163.com','1056538894@qq.com']


    def upload_HTML_file(self,email_title,filepath):
        txt = MIMEMultipart()
        txt['Subject'] = email_title
        files = os.listdir(filepath)
        file = files[-1]
        # for file in files:
        if file.endswith('.html'):
            file_name = filepath+'/'+file
            with open(file_name, 'rb') as f:
                email_content = MIMEText(f.read(), 'html', 'utf-8')
                #将需要发送的内容添加到邮件主体中
                txt.attach(email_content)
            with open(file_name, 'rb') as e:
                attachment = MIMEText(e.read(), 'base64', 'utf-8')
                attachment["Content-Type"] = 'application/octet-stream'
                attachment["Content-Disposition"] = 'attachment; filename=%s'%file
                txt.attach(attachment)
        return txt


    #登录并发送
    def login_and_send_email(self,email_title,filepath,conffile):
        txt = self.upload_HTML_file(email_title,filepath)
        SMTPserver_dict = self.get_info_from_csv_to_dict(conffile)
        receivers_list = SMTPserver_dict['收件人'].split("，")
        for receivers in receivers_list:
            try:
                smtpObj = smtplib.SMTP()
                smtpObj.connect(SMTPserver_dict['SMTPServer'],25)
                smtpObj.login(SMTPserver_dict['发件人'],SMTPserver_dict['密码'])
                smtpObj.sendmail(SMTPserver_dict['发件人'],receivers,txt.as_string())
                print('测试结果发送成功')
                smtpObj.quit()
            except:
                print('测试结果发送失败')



if __name__=='__main__':
    send_email().login_and_send_email('自动化执行结果结果','../Modules/Common/TestReport','../../Conf/TestEmailServerConf.csv')

