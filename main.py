# coding:utf-8
# Python抓取QQ空间留言板内容
# 运行文件
# 引入爬取说说文件

from shuoshuo import get_shuoshuo
# 引入爬取留言板文件
from liuyanban import get_liuyanban

# 需要爬取的QQ号码
select_qq = ******
# QQ号
qq = ******
# QQ密码
passwrod = "******"
# phantomjs路径
path="D:\\phantomjs\\bin\\phantomjs.exe"

# 执行爬取说说方法
get_shuoshuo(select_qq,qq,passwrod,path)
# 执行爬取留言板方法
get_liuyanban(select_qq,qq,passwrod,path)
